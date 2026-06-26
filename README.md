# Pratic RH — Notas de Alterações

Geração automática diária das notas de alterações do **Pratic RH Desktop** e **Pratic RH Nuvem** (serviços 40 e 60), via GitHub Actions.

## Como funciona

```
GitHub Actions (roda de seg a sáb às 09h BRT)
      ↓
Consulta API Pratic → filtra OSs novas → gera Markdown
      ↓
git commit + git push automático neste repositório
      ↓
Web (PrimeFaces) e Desktop (Java) leem a URL raw abaixo
```

## URLs de consumo

| Uso | URL |
|-----|-----|
| Última versão | `https://raw.githubusercontent.com/rodrigocorrea2704/pratic-release-notes/main/release-notes/notas_latest.md` |
| Data específica | `https://raw.githubusercontent.com/rodrigocorrea2704/pratic-release-notes/main/release-notes/notas_AAAAMMDD.md` |

## Setup (uma vez só)

### 1. Adicionar o secret `PRATIC_TOKEN`

Acesse: **Settings → Secrets and variables → Actions → New repository secret**

- Name: `PRATIC_TOKEN`
- Secret: _(seu token da API Pratic)_

### 2. Habilitar o workflow

Acesse a aba **Actions** do repositório e clique em **"I understand my workflows, go ahead and enable them"**.

Pronto — o workflow roda automaticamente todo dia útil às 09h.

## Estrutura

```
.github/workflows/gerar-notas.yml   # agendamento e CI
scripts/gerar_notas.py              # lógica de geração
release-notes/
  notas_AAAAMMDD.md                 # arquivo diário
  notas_latest.md                   # sempre o mais recente
  .os_processadas.json              # controle de deduplicação
```

## Integração Java

### Web — PrimeFaces

Adicione ao `pom.xml`:
```xml
<dependency>
    <groupId>com.vladsch.flexmark</groupId>
    <artifactId>flexmark-all</artifactId>
    <version>0.64.8</version>
</dependency>
```

Use `ReleaseNotesBean.java` + `release-notes.xhtml` (ver pasta `/docs/java/web/`).

### Desktop — Java 1.8

Use `ReleaseNotesDialog.java` (ver `/docs/java/desktop/`).
Chamada: `ReleaseNotesDialog.exibir(frameAtual);`
