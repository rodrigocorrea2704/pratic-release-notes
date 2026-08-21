📋 Notas de Alterações — Pratic RH / Pratic SIP
Últimos 15 dias (06/08/2026 a 21/08/2026)

Atualizado em: 21/08/2026 09:04

---

🗂️ APP PRATIC RH  - CLOUD

🔧 Melhoria | OS #19904 — E-CONSIGNADO / DADOS RESCISÓRIOS

Em Movimentos / e-Consignado / Lançamentos: fiz o lançamento de um novo contrato, e informei os campos novos, se "possui garantia FGTS", "saldo devedor" e o "% 
.1 - Incluir os campos novos no grid da consulta;
.2 - Adicionar uma opção para conseguir editar um contrato já lançado.

🔧 Melhoria | OS #19901 — TIRAR O OBRIGATORIEDADE DESSE CAMPO

Tirar a obrigatoriedade do campo pensão alimentícia sem adiantamento salario

🔧 Melhoria | OS #19894 — EXCLUSÃO DE EMPRESAS / ESCOPA

⚠️ Em desenvolvimento...

🔧 Melhoria | OS #19897 — RECIBO DE FERIAS - ESTAGIARIO

Existe férias calculadas com saida em 01/08/2026, porém na Nuvem não lista o recibo de ferias de estagiario.

✅ Correção | OS #19886 — BACKUP COM PROBLMEA NA NUVEM

Não ta funcionando o backup, corrigir

✅ Correção | OS #19883 — EVENTO MEDIAS FERIAS  DUPLICADO S-1200

O evento 33 - medias de ferias esta saindo duas vezes no xml do S-1200 (sai o proprio evento e tambem soma no cod evento 178 - ferias esocial)

🔧 Melhoria | OS #19881 — SOLICITAÇÃO / CÁLCULO RESCISÃO / BOTÃO FALTAS

⚠️ Em desenvolvimento...

🔧 Melhoria | OS #19870 — TAG DMDEV S-1210 MULTIPLO VINCULO

⚠️ Em desenvolvimento...

🔧 Melhoria | OS #19842 — MIGRAÇÃO DE CLIENTE

Colocar o banco de dados na nuvem
Alessandra disse que o e-mail cadastrado para acesso a FOLHA NUVEM, está cadastrado errado. Trocar o e-mail para e-mail: escopacontabilidade2026@hotmail.com

🔧 Melhoria | OS #19798 — NOVO CLIENTE

⚠️ Em desenvolvimento...

🔧 Melhoria | OS #19752 — INCLUSÃO DE CONTRATO COM AUTOMAÇÃO

Após o Cadastramento de um Colaborador o cliente precisa de um gerador de relatorios específicos 

🔧 Melhoria | OS #19032 — GERADOR DE CONTRATO / WEB

/ 2 / Em Relatórios / Contrato de Trabalho / Cadastro: estou editando apenas o TITULO do contrato, conforme no print já consta a borda preenchida porque esse contrato já veio

🔧 Melhoria | OS #18799 — LIMPESA DE ARQUIVOS TEMPORÁRIOS NA NUVEM

VERIFICAR EM QUE MOMENTO O SISTEMA EM NUVEM FAZ A LIMPESA DOS ARQUIVOS TEMPORÁRIOS 
EM UMA BASE DE CLIENTE FUI DELETAR O AUXDIV POR EXEMPLO E CONGELOU MEU PC, PENSEI QUE TAVA TRAVADO MAS ERA O ARQUIVO QUE TAVA MUITO GRANDE 

🗂️ FOLHA DE PAGAMENTO - BANCO DE DADOS

✅ Correção | OS #19928 — GERAÇÃO S-2299 COM FÉRIAS

Na geração do S-2299 (ID - 9424) o sistema está gerando somente o evento 1/3 de férias, os demais eventos 11-Férias Gozadas e 33-Médias de Férias não
Na geração do S-1210 (ID - 9408) da competência 08/2026 o sistema precisa gerar a TAG - FÉRIAS e a TAG = tpPgto = 2

🔧 Melhoria | OS #19919 — HOLERITE ELETRÔNICO - BRADESCO/BRADESCO 250 POS.

(Prints 1 e 2) - Em Processamentos / Eletrônicos / Holerite Eletrônico: cliente solicitou inlcuir nos bancos BRADESCO e BRADESCO 250 POS. as opções para gerar sobre:

✅ Correção | OS #19905 — GERAÇÃO S-1200 / TOMADOR POR RATEIO / FÉRIAS

Na geração do S-1200 (ID = 62138) o funcionário está de férias, e o sistema não está gerando na TAG - FÉRIAS o evento 347 - Férias e-Social (na tabela ele é o código 2-49).

✅ Correção | OS #19900 — GERAÇÃO DO S-1200 / AUTÔNOMO / POR RATEIO DE TOMADOR

Na geração do S-1200 (ID = 60522) o sistema não está gerando o evento 100 - INSS (na tabela ele é o código 1-39) para o Autônomo 0002.

✅ Correção | OS #19902 — GERAÇAÕ S-1200 / TOMADOR POR RATEIO

Estou tentando enviar o evento S-1200 (ID =16243 ) o sistema mostra um erro. ERRO em anexo.

🔧 Melhoria | OS #19895 — CONSULTA CADASTRO AUTONOMO

⚠️ Em desenvolvimento...

🔧 Melhoria | OS #19892 — GERAÇÃO S-1210 / PENSÃO DE 13º SALÁRIO

⚠️ Em desenvolvimento...

🔧 Melhoria | OS #19889 — E-SOCIAL / FÉRIAS / FALTAS

Funcionário com férias 30 dias dentro do mês 07/2026, porém o cliente quer descontar faltas/DSR, e lançar um auxilio, fazendo o holerite do funcionário gerar estouro, no holerite
Adcionar um campo novo na tabela de codigos especias na posição 1-84

🔧 Melhoria | OS #19880 — CÁLCULO RESCISÃO / ADICIONAL NOTURNO

⚠️ Em desenvolvimento...

🔧 Melhoria | OS #19877 — ERRO CALCULO RESCISAO

⚠️ Em desenvolvimento...

🔧 Melhoria | OS #19875 — GERAÇÃO S-1210 / FOLHA + 13º + FÉRIAS

Estou fazendo a geração do S-1210 (ID =44534 ) e o sistema está gerando a data de pagamento da TAG da folha errada, data correta da Tag - <dtPgto> tem que ser 31/07/2026.

🔧 Melhoria | OS #19874 — CÁLCULO INTERMITENTE / SEM CONVOCAÇÃO

Funcionário Intermitente, no mês 07/2026 ele não foi convocado, então no digitado foi lançado o evento 002- Horas Normais com o valor zerado, e mesmo zerado o sistema

✅ Correção | OS #19867 — SOLCITAÇÃO / RELATÓRIO DE PROVENTOS E DESCONTOS

Em Relatórios / Colaboradores / Mensais / Relatórios para Conferência / Relação de Proventos e Descontos - estou informando em tela apenas o filtro da Seção 12, e a quebra

🔧 Melhoria | OS #19596 — TRANSFERÊNCIA / CÁLCULO FOLHA

Fiz uma transferência com data 30/04/2026, então na empresa de origem (2021) o funcionário precisa receber 29 DIAS de salário, no valor de R$ 4.350,00 e o sistema apurou um 
