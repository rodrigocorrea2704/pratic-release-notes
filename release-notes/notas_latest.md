📋 Notas de Alterações — Pratic RH / Pratic SIP
Últimos 15 dias (05/07/2026 a 20/07/2026)

Atualizado em: 20/07/2026 09:39

---

🗂️ APP PRATIC RH  - CLOUD

✅ Correção | OS #19819 — CLIENTE REPORTANDO INCOSISTENCIA NO CADASTRO DE COLABORADORES / CONSULTA RESCISÃO

Cliente (RH_STAR_SHINE e RH_FUNDEC) Tenta gravar e não ta conseguindo gravar dados bancarios, não mostra data de nascimento, sexo ou a tela não esta mostrando no cadastro do
Cliente (RH_UNIDOS / RH_IVONE / RH_PRATICIA_CRISTINA) - Estão entrando em Processamentos / Rescisões / Consultar conforme o e não aparece nada "sumiu"

✅ Correção | OS #19807 — LOCAÇÃO TOMADOR - SOCIO

Ao preencher os dados para locação do socio 1 no tomador 42 da empresa 2092 e clicar em salvar na Nuvem o sistema nem grava informaçao e nem da mensagem de erro.

🔧 Melhoria | OS #19776 — CALCULO INTERMITENTE - SUB BASE (FERIAS E 13°)

⚠️ Em desenvolvimento...

🔧 Melhoria | OS #19767 — SOLICITAÇÃO / ENCERRAMENTO EM LOTE / FILA DE ESTABELECIMENTOS / FOLHA NUVEM

Solicitação do Cliente Delton-Escritório São José, para inclusão do encerramento automático no cálculo/fila estabelecimento:

🗂️ FOLHA DE PAGAMENTO - BANCO DE DADOS

✅ Correção | OS #19823 — GERAÇÃO DO S-2299 / EMPRÉSTIMO

Na geração do S-2299 (ID = 27968), o sistema não está gerando no xml o evento 196 com os valores/dados do empréstimo do funcionário, verifiquei que é devido ter os

🔧 Melhoria | OS #19805 — LISTAGEM FOLHA / RESCISÃO / 13º

Estou fazendo a listagem da folha, competência 05/2026, e no RESUMO DO INSS - o valor a recolher precisar ser R$ 192,44

🔧 Melhoria | OS #19809 — MAPA MEDIAS - PROVISAO FERIAS

⚠️ Em desenvolvimento...

🔧 Melhoria | OS #19791 — GERAÇÃO S-1210 / FUNCS + AUTONOMO

⚠️ Em desenvolvimento...

🔧 Melhoria | OS #19784 — S-1210 - TAG IDEDMDEV 13° SALARIO

⚠️ Em desenvolvimento...

🔧 Melhoria | OS #19787 — GERAÇÃO DO S-2500

Na geração do S-2500 (ID = 33101) a tag <codCateg>0</codCateg> o sistema está levando 0, nesse caso, foi informado "nenhum" então não podemos mandar essa TAG.

✅ Correção | OS #19773 — EMISSÃO HOLERITE COMPLETO

Erro na emissão dos Holerites Completos em Lote, modelo "holerite uma coluna":
Erro na emissão dos Holerites Completos em Lote, modelo "holerite duas colunas":

🔧 Melhoria | OS #19766 — GERAÇÃO DO S-2299 - RESCISÃO/FÉRIAS GOZADAS

Funcionário retornou das férias dia 12/06, e no dia 23/06 foi desligado da empresa, então na geração do S-2299 (ID = 1287) o sistema não pode gerar o evento 22 (2-40) na
Na geração do S-1210 (ID = 1286) o sistema precisa gerar o <tpPgto> da tag férias = 2
Na geração do S-1210 (ID = 1286) o sistema precisa gerar na tag das FÉRIAS, a tag <perRef> = 2026-06
