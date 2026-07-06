#!/usr/bin/env python3
"""
Gerador de Notas de Alterações — Pratic RH Desktop / Nuvem (Sercod 40 e 60)
Roda automaticamente via GitHub Actions.
"""

import json
import os
import re
import sys
from collections import defaultdict
from datetime import date, datetime, timedelta
from html.parser import HTMLParser
from pathlib import Path
import urllib.request

# ─── Config ───────────────────────────────────────────────────────────────────

API_URL = "https://praticsite.com.br/PraticSite/PraticService"
REPO_ROOT = Path(__file__).parent.parent
RELEASE_DIR = REPO_ROOT / "release-notes"
CONTROL_FILE = RELEASE_DIR / ".os_processadas.json"
ICONS = {"Novo": "🆕", "Melhoria": "🔧", "Correção": "✅"}

# ─── HTML → texto puro ────────────────────────────────────────────────────────

# Só tags de bloco quebram linha — tags inline (b, font, a, span...) não podem
# fragmentar uma frase em várias linhas.
_BLOCK_TAGS = {"p", "div", "br", "li", "tr", "h1", "h2", "h3", "h4", "h5", "h6"}

class _TextExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self._parts = []
    def handle_starttag(self, tag, attrs):
        if tag in _BLOCK_TAGS:
            self._parts.append("\n")
    def handle_endtag(self, tag):
        if tag in _BLOCK_TAGS:
            self._parts.append("\n")
    def handle_data(self, data):
        self._parts.append(data)
    def get_text(self):
        return "".join(self._parts)

def html_to_text(html):
    p = _TextExtractor()
    p.feed(html)
    t = p.get_text()
    t = t.replace("\xa0", " ")          # &nbsp;
    t = re.sub(r"[ \t]+", " ", t)
    t = re.sub(r"\n[ \t]*\n+", "\n", t)
    return t.strip()

# ─── Padrões ──────────────────────────────────────────────────────────────────

OK_PAT = re.compile(r"\[\s*OK\s*\]", re.IGNORECASE)

# Texto padrão de instrução ("Indique com o [ OK ] os itens que devem
# aparecer nas Notas da Versão") contém a marcação [ OK ] apenas como
# exemplo — não pode ser confundido com um item de fato concluído.
LEMBRETE_PAT = re.compile(
    r"indique\s+com\s+o\s*\[\s*ok\s*\][\s\S]{0,120}?vers[aã]o",
    re.IGNORECASE,
)

# Linha que é só numeração/referência de print, sem descrição real
# (ex.: "01 - (print) -", "(print)", "1 e 2 (print)")
_PRINT_PAT = re.compile(r"\(print[^)]*\)", re.IGNORECASE)
_ITEM_WORD_PAT = re.compile(r"\bitem\b", re.IGNORECASE)
_SHORT_TOKEN_PAT = re.compile(r"\b\w{1,2}\b", re.UNICODE)
_LABEL_CHARS_PAT = re.compile(r"[\d\s\-–.,]")

def _eh_apenas_rotulo(linha):
    l = _PRINT_PAT.sub("", linha)
    l = _ITEM_WORD_PAT.sub("", l)
    l = _SHORT_TOKEN_PAT.sub("", l)
    l = _LABEL_CHARS_PAT.sub("", l)
    return l == ""

NUMBERED_PAT = re.compile(r"^\s*(\d{2})\s*[-–]\s*(.+)", re.MULTILINE)

ANEXO_PAT = re.compile(r"^\s*anexo\s*\d", re.IGNORECASE)

JUNK_PAT = re.compile(
    r"\d+\s*(?:e\s*\d+\s*)?\(print[^)]*\)\s*[-–]?\s*"
    r"|\[Arquivo[^\]]*\]"
    r"|API\s*->.*",
    re.IGNORECASE,
)

# Rótulo de numeração/print que sobra no início da descrição depois que o
# texto real já foi isolado (ex.: "01 - (print) - ", "ITEM 2 - Print 04 - ")
_LEADING_LABEL_PAT = re.compile(
    r"^(?:item\s*)?\d+\s*[-–]?\s*(?:\(print[^)]*\)\s*[-–]?\s*)?"
    r"|^print\s*\d+\s*[-–]?\s*",
    re.IGNORECASE,
)

def _remover_rotulo_inicial(desc):
    anterior = None
    while anterior != desc:
        anterior = desc
        desc = _LEADING_LABEL_PAT.sub("", desc, count=1)
    return desc

# Conteúdo puramente técnico/interno — não vai para as notas
INTERNO_PAT = re.compile(
    r"\b(procedure|trigger|campo\s+boolean|boolean\s+novo|"
    r"default\s*=\s*(true|false)|declare|APP_INC|APP_ALT|FP_EVENTOS|"
    r"excluir\s+a\s+cl[aá]usula|reposicionar\s+(a\s+s?\s*)?cl[aá]usula)\b",
    re.IGNORECASE,
)

CORRECAO_PAT = re.compile(
    r"\b(erro|bug|corrig|falha|n[aã]o\s+(est[aá]|fun|list|hab)|"
    r"apresenta\s+erro|mensagem\s+de\s+erro|p[aá]gina\s+n[aã]o\s+encontrada|"
    r"truncat|DATA\s+TRUNCAT|nada\s+a\s+relacion)\b",
    re.IGNORECASE,
)

NOVO_PAT = re.compile(
    r"\b(inclus[aã]o\s+de\s+tela|incluir\s+(tela|rotina|m[oó]dulo)|"
    r"disponibilizar|nova\s+(tela|rotina|funcionalidade))\b",
    re.IGNORECASE,
)

# ─── Extração e classificação ─────────────────────────────────────────────────

def extrair_itens_ok(texto):
    """Retorna lista de descrições após cada [ OK ]."""
    chunks = re.split(r"\[\s*OK\s*\]", texto, flags=re.IGNORECASE)
    itens = []
    for chunk in chunks[1:]:
        linhas = [ln.strip(" –-\t") for ln in chunk.split("\n") if ln.strip(" –-\t")]
        desc = next((ln for ln in linhas if not _eh_apenas_rotulo(ln)), None)
        if not desc:
            continue
        desc = re.sub(JUNK_PAT, "", desc).strip(" –-\t")
        desc = _remover_rotulo_inicial(desc).strip(" –-\t")
        if desc and len(desc) > 4:
            itens.append(desc)
    return itens

def classificar(assunto, texto, itens):
    """Retorna 'Novo', 'Melhoria', 'Correção' ou 'Interno'."""
    combinado = " ".join([assunto, texto] + itens)
    if INTERNO_PAT.search(combinado):
        return "Interno"
    if CORRECAO_PAT.search(combinado):
        return "Correção"
    if NOVO_PAT.search(assunto + " " + " ".join(itens)):
        return "Novo"
    return "Melhoria"

# ─── API ──────────────────────────────────────────────────────────────────────

DIAS_RETROATIVOS = 7

def consultar_api(token, data_consulta):
    payload = json.dumps({
        "praticServiceValidarEntrada": {
            "tokenPraticIntegracaoAutenticacao": token
        },
        "selecionarOSPorServico": {
            "listaCodServico": "40,60",
            "dataInicioFinalizacaoOS": data_consulta,
        },
    }).encode("utf-8")

    req = urllib.request.Request(
        API_URL,
        data=payload,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        status = resp.status
        body = resp.read().decode("utf-8")
        data = json.loads(body)

    print(
        f"🔎 [debug] HTTP {status} | result={data.get('result')!r} | "
        f"mensagem={data.get('mensagem')!r} | ordens={len(data.get('ordens') or [])}"
    )

    if data.get("result") != 1 or not data.get("ordens"):
        return []
    return data["ordens"]

# ─── Main ─────────────────────────────────────────────────────────────────────

def main():
    token = os.environ.get("PRATIC_TOKEN")
    if not token:
        print("❌ Variável de ambiente PRATIC_TOKEN não definida. Abortando.")
        sys.exit(1)
    print(f"🔎 [debug] token com {len(token)} caracteres (repr das pontas: {token[:2]!r}...{token[-2:]!r})")
    if token != token.strip():
        print("⚠️  [debug] o token tem espaços/quebras de linha nas pontas!")

    hoje = date.today()
    if hoje.weekday() == 6:  # domingo = 6
        print("Rotina não executada — domingos são ignorados.")
        sys.exit(0)

    data_inicio      = hoje - timedelta(days=DIAS_RETROATIVOS)
    data_inicio_str  = data_inicio.strftime("%d/%m/%Y")
    data_hoje_str    = hoje.strftime("%d/%m/%Y")
    data_hoje_arq    = hoje.strftime("%Y%m%d")
    timestamp        = datetime.now().strftime("%d/%m/%Y %H:%M")
    periodo_str      = f"{data_inicio_str} a {data_hoje_str}"

    print(f"📅 Consultando OSs finalizadas entre {periodo_str}...")

    # Controle de deduplicação
    RELEASE_DIR.mkdir(parents=True, exist_ok=True)
    if CONTROL_FILE.exists():
        control = json.loads(CONTROL_FILE.read_text("utf-8"))
    else:
        control = {"processadas": []}
    already = {e["oseCod"] for e in control["processadas"]}

    # Consulta API — dataInicioFinalizacaoOS é "a partir de": uma única
    # chamada já retorna tudo desde essa data até agora.
    try:
        ordens = consultar_api(token, data_inicio_str)
    except Exception as exc:
        print(f"❌ Erro ao consultar API: {exc}")
        sys.exit(1)

    if not ordens:
        print(f"ℹ️  Nenhuma OS encontrada entre {periodo_str}.")
        sys.exit(0)

    print(f"📦 {len(ordens)} OS(s) retornada(s).")

    novas = [o for o in ordens if o["oseCod"] not in already]
    ignoradas_dedup = len(ordens) - len(novas)

    if not novas:
        print(f"ℹ️  Todas as OSs de {periodo_str} já foram processadas anteriormente.")
        sys.exit(0)

    # Processa cada OS nova
    new_entries = []
    to_include  = []

    for os_item in novas:
        cod     = os_item["oseCod"]
        assunto = os_item["assunto"]
        texto   = html_to_text(os_item["texto"])
        texto   = LEMBRETE_PAT.sub("", texto)
        has_ok  = bool(OK_PAT.search(texto))
        numbered = [
            m for m in NUMBERED_PAT.finditer(texto)
            if not ANEXO_PAT.match(m.group(0).strip())
        ]

        # Sem [OK] e sem itens numerados → suporte simples
        if not has_ok and not numbered:
            new_entries.append({
                "oseCod": cod, "dataProcessamento": timestamp,
                "incluida": False, "motivo": "suporte simples",
            })
            continue

        # Itens numerados mas sem [OK] → em desenvolvimento
        if not has_ok and numbered:
            to_include.append({
                "serCodDes": os_item["serCodDes"],
                "oseDat": os_item["oseDat"],
                "oseCod": cod, "assunto": assunto,
                "tipo": "Melhoria", "itens": ["⚠️ Em desenvolvimento..."],
            })
            new_entries.append({
                "oseCod": cod, "dataProcessamento": timestamp, "incluida": True,
            })
            continue

        # Tem [OK] — extrai itens e classifica
        itens = extrair_itens_ok(texto)
        tipo  = classificar(assunto, texto, itens)

        if tipo == "Interno":
            new_entries.append({
                "oseCod": cod, "dataProcessamento": timestamp,
                "incluida": False, "motivo": "interno",
            })
            continue

        # Fallback: usa o assunto se não extraiu descrição
        if not itens:
            itens = [assunto.capitalize()]

        to_include.append({
            "serCodDes": os_item["serCodDes"],
            "oseDat": os_item["oseDat"],
            "oseCod": cod, "assunto": assunto,
            "tipo": tipo, "itens": itens,
        })
        new_entries.append({
            "oseCod": cod, "dataProcessamento": timestamp, "incluida": True,
        })

    # Agrupa por serviço e ordena LIFO (mais recente primeiro)
    groups = defaultdict(list)
    for item in to_include:
        groups[item["serCodDes"]].append(item)
    for k in groups:
        groups[k].sort(
            key=lambda x: datetime.strptime(x["oseDat"], "%d/%m/%Y"),
            reverse=True,
        )

    # Monta o documento Markdown
    nota_path = RELEASE_DIR / f"notas_{data_hoje_arq}.md"
    modo = "a" if nota_path.exists() else "w"
    linhas = []

    if modo == "w":
        linhas += [
            "📋 Notas de Alterações — Pratic RH / Pratic SIP",
            f"Data de referência: {data_hoje_str}",
            "",
            f"Gerado em: {timestamp}",
            "",
            "---",
            "",
        ]

    for svc, items in sorted(groups.items()):
        linhas.append(f"🗂️ {svc}")
        linhas.append("")
        for item in items:
            icon = ICONS.get(item["tipo"], "🔧")
            linhas.append(f'{icon} {item["tipo"]} | OS #{item["oseCod"]} — {item["assunto"]}')
            linhas.append("")
            for desc in item["itens"]:
                linhas.append(desc)
            linhas.append("")

    with nota_path.open(modo, encoding="utf-8") as f:
        f.write("\n".join(linhas))

    # Atualiza notas_latest.md
    latest_path = RELEASE_DIR / "notas_latest.md"
    latest_path.write_text(nota_path.read_text("utf-8"), encoding="utf-8")

    # Persiste controle de deduplicação
    control["processadas"].extend(new_entries)
    CONTROL_FILE.write_text(
        json.dumps(control, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    # Resumo
    incluidas = sum(1 for e in new_entries if e["incluida"])
    ignoradas = sum(1 for e in new_entries if not e["incluida"])
    print(f"\n✅ Notas geradas: {nota_path.name}")
    print(f"\n📦 OSs novas processadas    : {len(novas)}")
    print(f"⏭️  OSs ignoradas (já vistas) : {ignoradas_dedup}")
    print(f"📝 OSs incluídas nas notas  : {incluidas}")
    print(f"🚫 OSs ignoradas (descarte) : {ignoradas}")

    if not to_include:
        print("\nℹ️  Nenhuma OS nova para incluir nas notas hoje.")

if __name__ == "__main__":
    main()
