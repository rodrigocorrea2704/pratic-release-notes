📋 Notas de Alterações — Pratic RH / Pratic SIP
Últimos 15 dias (01/07/2026 a 16/07/2026)

Atualizado em: 16/07/2026 09:27

---

🗂️ APP PRATIC RH  - CLOUD

✅ Correção | OS #19807 — LOCAÇÃO TOMADOR - SOCIO

Ao preencher os dados para locação do socio 1 no tomador 42 da empresa 2092 e clicar em salvar na Nuvem o sistema nem grava informaçao e nem da mensagem de erro.

🔧 Melhoria | OS #19776 — CALCULO INTERMITENTE - SUB BASE (FERIAS E 13°)

⚠️ Em desenvolvimento...

🔧 Melhoria | OS #19775 — ERRO S-2299 - EMPRESA CLASSIFICAÇÃO TRIB 03

⚠️ Em desenvolvimento...

✅ Correção | OS #19769 — HOLERITE COMPLETO - DESCRIÇOES

Na listagem do Holerite Completo na Nuvem, esta faltando descrição das colinas de provento, desconto e descriçao dos eventos.

🗂️ FOLHA DE PAGAMENTO - BANCO DE DADOS

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

🔧 Melhoria | OS #19771 — CÁLCULO FOLHA / VALE TRANSPORTE

Estou fazendo o cálculo da folha, o valor correto do evento 164, precisa ser R$ 105,80 (Salário calculado no mês R$ 1.763,33*6% = R$ 105,80)

🔧 Melhoria | OS #19763 — GERAÇÃO DA FOLHA/FÉRIAS COM E-CONSIGNADO

Funcionário com férias Abono TD - saída dia: 22/06 - no cálculo da folha do mês 06/2026 o valor do evento 279 precisa ser R$ 693,40 (total do empréstimo) porque
Funcionário com férias Abono TD - saída dia: 22/06 - no cálculo da folha do mês 07/2026 o valor do evento 279 precisa ser R$ 231,13 (ref. a 10 dias),
