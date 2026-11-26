📋 Notas de Alterações — Pratic RH / Pratic SIP
Últimos 15 dias (11/11/2026 a 26/11/2026)

Atualizado em: 26/11/2026 09:01

---

🗂️ APP PRATIC RH  - CLOUD

🔧 Melhoria | OS #20332 — Descrição: Quadro Horario Específico

Acrescentar no nome Quandro Horario (Específico), tanto no atalho como ao abrir a tela. [ 1 - colado-20261118-164229.png ]

🔧 Melhoria | OS #20335 — quadro especifico não aparece

⚠️ Em desenvolvimento...

✅ Correção | OS #20307 — Cálculo folha 13º Salário em Fila de Estabelecimento

Processamenos / Cálculos / 13º Salário / Calcular Colaboradores - estou usando a rotina CALCULAR FILA para calcular a 1ª parcela do 13º
Processamenos / Cálculos / 13º Salário / Calcular Colaboradores - implementar na rotina CALCULAR FILA a opção para calcular a 2ª parcela do 13º salário. (como é feito o cálculo no desktop - [ 3 - colado-20261112-164204.png ])
Ref. ao ITEN 01- Processamenos / Cálculos / 13º Salário / Calcular Colaboradores - estou usando a rotina calcular fila, e após o cálculo da 1ª parcela do 13º salário,[ 1 - colado-20261112-162356.png ] a lisgagem da folha que está sendo enviada no e-mail, precisamos arrumar os dizerez que aparece PARCELA COMPLEMENTO, [ 4 - colado-20261116-141124.png ] para 1ª parcela (conforme aparece quando é feito a listagem pela rotina da listagem da folha da 1ª parcela ) [ 5 - colado-20261116-141350.png ]
Ref. ao ITEN 02- Processamenos / Cálculos / 13º Salário / Calcular Colaboradores - estou usando a rotina calcular fila, e após o cálculo da 2ª parcela , [ 7 - colado-20261116-141731.png ] o PDF da listagem da folha que está sendo enviada no e-mail está em branco, [ 6 - colado-20261116-141634.png ] OBS: Os Holerites foram enviados corretos, o erro é apenas na folha de pagamento.

✅ Correção | OS #20293 — Geração do S-1200

O Evento ta marcado como Multiplos = N porem eu consigo colocar multiplos pelo sistema iteord =1 iteseq = 84 [ 3 - colado-20261111-081216.png ]

🔧 Melhoria | OS #20255 — Calculo de IR Adiantamento e PLR

Adicionar a rotina de apuração de adiantamento/plr na nuvem ... [ 1 - colado-20261030-155712.png ]
O Dashboard do calculo de folha não ta ataulizando o holerite e a conferencia da folha quando mexenos no digitado e nas férias [ 2 - colado-20261105-100646.png ]
na tela de contrato de trabalho padrão, o contrato de trabalho tem que passar o campo novo CONISG = false

🔧 Melhoria | OS #20151 — Solicitação Referencias - Holerite Completo

⚠️ Em desenvolvimento...

🗂️ FOLHA DE PAGAMENTO - BANCO DE DADOS

🔧 Melhoria | OS #20352 — RELATORIO DE BASES - EM EXCEL

Fazer o Gerador em Excel Nuvem - [ 2 - colado-20261124-152117.png ]

🔧 Melhoria | OS #20344 — Alterações LAYOUT - ESOCIAL

Na geração o S-1010 (ID = 33589 ) agora tem um tag <observacao> obrigatória somente para evento com tpRubr = 4, pensei ao invés de criar esse campo, mandar o nome da rubrica nesse campo automático, porque são poucos eventos usando esse tipo 4, caso não concordar, então criar o campo Observação em Cadastro / Tabelas / Eventos - [ 1 - colado-20261123-144204.png ]
Na geração o S-1000 (ID = 33588 ) agora a tag <indOptRegEletron> não pode preencher se iniValid for igual ou posterior a [2026-02]. [ 2 - colado-20261123-144726.png ] - T:\Layout\E-social\Layout_v. S-1.3\Layout_v.S-1.3 - nota 07.2026

🔧 Melhoria | OS #20319 — Cálculo/Eliminar Folha  Mensal

⚠️ Em desenvolvimento...

🔧 Melhoria | OS #20298 — CALCULO 13º - DIARISTA

⚠️ Em desenvolvimento...

🔧 Melhoria | OS #20301 — Importar Acumulado - Jose Roberto Dias

⚠️ Em desenvolvimento...

🔧 Melhoria | OS #20299 — Geração S-2200 e S-2205

⚠️ Em desenvolvimento...

🔧 Melhoria | OS #20302 — Erro  - Exclusão Transferencia

⚠️ Em desenvolvimento...

🔧 Melhoria | OS #20282 — Rescisão com Férias do Aviso Indenizado

⚠️ Em desenvolvimento...

✅ Correção | OS #20281 — S-2230 com afastamento anterior

Ferias (1010/1/10) deu certo tipo 15;
Afastamento inicial e mesmo motivo (O3 seguido de O2) deu certo (1010/1/5).
