📋 Notas de Alterações — Pratic RH / Pratic SIP
Últimos 15 dias (24/07/2026 a 08/08/2026)

Atualizado em: 08/08/2026 09:05

---

🗂️ APP PRATIC RH  - CLOUD

✅ Correção | OS #19883 — EVENTO MEDIAS FERIAS  DUPLICADO S-1200

O evento 33 - medias de ferias esta saindo duas vezes no xml do S-1200 (sai o proprio evento e tambem soma no cod evento 178 - ferias esocial)

🔧 Melhoria | OS #19870 — TAG DMDEV S-1210 MULTIPLO VINCULO

⚠️ Em desenvolvimento...

🔧 Melhoria | OS #19866 — EXCLUSÃO DA RESCISÃO DE ESTAGIÁRIO

Em Trabalhadores / Estagiários / Consulta-Cadastro - estou entrando no painel do estagiário, e clicando na opção "Exclusão do término de contrato" o sistema "trava" mostra uma tela

🔧 Melhoria | OS #19863 — SOLICITAÇÃO - CALCULO FOLHA / MENSAGENS DO AVISO FÉRIAS VENCIDAS

Em Processamentos / Mensais / Calcular Colaboradores >> Calcular em LOTE - no cálculo da folha, quando tem avisos ref. ao vencimento de Férias Vencidas, o sistema mostra apenas

🔧 Melhoria | OS #19842 — MIGRAÇÃO DE CLIENTE

Colocar o banco de dados na nuvem
Alessandra disse que o e-mail cadastrado para acesso a FOLHA NUVEM, está cadastrado errado. Trocar o e-mail para e-mail: escopacontabilidade2026@hotmail.com

🔧 Melhoria | OS #19813 — CAMPO DATA NASCIMENTO  - REGISTRO COLABORADOR NUVEM

⚠️ Em desenvolvimento...

🔧 Melhoria | OS #19798 — NOVO CLIENTE

⚠️ Em desenvolvimento...

🔧 Melhoria | OS #19752 — INCLUSÃO DE CONTRATO COM AUTOMAÇÃO

Após o Cadastramento de um Colaborador o cliente precisa de um gerador de relatorios específicos 

🔧 Melhoria | OS #18799 — LIMPESA DE ARQUIVOS TEMPORÁRIOS NA NUVEM

VERIFICAR EM QUE MOMENTO O SISTEMA EM NUVEM FAZ A LIMPESA DOS ARQUIVOS TEMPORÁRIOS 
EM UMA BASE DE CLIENTE FUI DELETAR O AUXDIV POR EXEMPLO E CONGELOU MEU PC, PENSEI QUE TAVA TRAVADO MAS ERA O ARQUIVO QUE TAVA MUITO GRANDE 

🗂️ FOLHA DE PAGAMENTO - BANCO DE DADOS

🔧 Melhoria | OS #19880 — CÁLCULO RESCISÃO / ADICIONAL NOTURNO

⚠️ Em desenvolvimento...

🔧 Melhoria | OS #19877 — ERRO CALCULO RESCISAO

⚠️ Em desenvolvimento...

🔧 Melhoria | OS #19875 — GERAÇÃO S-1210 / FOLHA + 13º + FÉRIAS

Estou fazendo a geração do S-1210 (ID =44534 ) e o sistema está gerando a data de pagamento da TAG da folha errada, data correta da Tag - <dtPgto> tem que ser 31/07/2026.

🔧 Melhoria | OS #19874 — CÁLCULO INTERMITENTE / SEM CONVOCAÇÃO

Funcionário Intermitente, no mês 07/2026 ele não foi convocado, então no digitado foi lançado o evento 002- Horas Normais com o valor zerado, e mesmo zerado o sistema

🔧 Melhoria | OS #19872 — RESCISÃO / FÉRIAS / IRRF ABAIXO DE 5 MIL

Em Processamentos / Rescisão / Calcular Rescisão: o sistema está calculando o evento 162 - IRRF s/ Férias, nesse caso a base ficou menor que 5mil

✅ Correção | OS #19867 — SOLCITAÇÃO / RELATÓRIO DE PROVENTOS E DESCONTOS

Em Relatórios / Colaboradores / Mensais / Relatórios para Conferência / Relação de Proventos e Descontos - estou informando em tela apenas o filtro da Seção 12, e a quebra

🔧 Melhoria | OS #19868 — FOLHA COM E-CONSIGNADO / RENDIMENTO EM OUTRAS EMPRESAS

⚠️ Em desenvolvimento...

🔧 Melhoria | OS #19862 — GERAÇÃO S-2299 / EMPRÉSTIMO

⚠️ Em desenvolvimento...

🔧 Melhoria | OS #19857 — GERAÇÃO DO S-2300 / ESTAGIÁRIO + ESTRANGEIRO

⚠️ Em desenvolvimento...

🔧 Melhoria | OS #19840 — RESCISÃO / 13º / IRRF ABAIXO DE 5MIL

⚠️ Em desenvolvimento...

🔧 Melhoria | OS #19838 — TELA AFASTAMENTO

Em Cadastro / Colaboradores / Funcionários - campo "situação" - fiz o lançamento do afastamento normalmente, sem erros, porém quando vou editar o afastamento lançado o sistema

🔧 Melhoria | OS #19816 — ENVIO S-1299 ESOCIAL / DIFERENÇAS DIRF COM CONVÊNIO

O Relatorio Conferencia Dirf aponta diferença no valor enviado de plano de saude da colaboradora Gabriela Duran das Neves,

🔧 Melhoria | OS #19804 — CONSULTA FUNCIONARIO (PESQUISA DIGITAÇAO)

⚠️ Em desenvolvimento...

✅ Correção | OS #19747 — NOVA API / IMPORTAÇÃO E-CONSIGNADO RESCISÃO

Nova API do eConsignador - temos que criar a rotina para consumir e importar os dados antes de calcular uma Rescisão
Alteração no Cálculo da Rescisão referente a montagem da base de calculo:
Criação dos Campos Novos: 
Em Movimentação / Colaboradores / Lançamentos do e-Consignado / Lançamentos Mensais: teste sendo aplicado em modo PRODUÇÃO, estou usando a opção "Importar por 
Em Movimentação / Colaboradores / Lançamentos do e-Consignado / Lançamentos Mensais: estou usando a opção "Importar por Funcionário" - selecionando a opção
Em Movimentação / Colaboradores / Lançamentos do e-Consignado / Lançamentos Mensais: estou usando a opção "Importar por Empregador" - selecionando a opção
Em Movimentação / Colaboradores / Lançamentos do e-Consignado / Lançamentos Mensais: estou usando a opção "Importar por Funcionário" - selecionando a opção

🔧 Melhoria | OS #19596 — TRANSFERÊNCIA / CÁLCULO FOLHA

Fiz uma transferência com data 30/04/2026, então na empresa de origem (2021) o funcionário precisa receber 29 DIAS de salário, no valor de R$ 4.350,00 e o sistema apurou um 
