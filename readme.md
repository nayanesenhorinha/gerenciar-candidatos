# Aplicativo de Gerenciamento de Candidatos
Este aplicativo foi desenvolvido como parte do curso de Analista de Dados oferecido pelo Senac Rio, em parceria com a Prefeitura do Rio de Janeiro e a CNseg, no programa "Programadores Cariocas no Mercado Segurador".

## Sobre o projeto
O aplicativo em Python foi desenvolvido para gerenciar candidatos e suas notas em um processo seletivo. Ele permite buscar candidatos por critérios de nota em diferentes etapas e também cadastrar novos candidatos.

## Contexto
Uma startup está desenvolvendo um **aplicativo** que **verifica a compatibilidade de um candidato com uma vaga** de acordo com seu resultado nas etapas do processo seletivo.
Para isso foi criado um teste que devolve uma string no seguinte formato: **eX_tX_pX_sX** (sendo que cada X é substituído pela avaliação da pessoa em uma das etapas do processo - entrevista, teste teórico, teste prático e avaliação de soft skills).

### O que é para fazer?
**Criar com Python uma lista para armazenar esses resultados** (e outros resultados que quiser no mesmo formato, o código precisa funcionar para qualquer lista que seja inserida nesse formato) e depois **uma função que busca o candidato de acordo com os critérios digitados pelo usuário**.

### Como fazer?
Você deve criar com Python uma lista para armazenar esses resultados (e outros resultados que quiser no mesmo formato, o código precisa funcionar para qualquer lista que seja inserida nesse formato) e depois uma função que busca o candidato de acordo com os critérios digitados pelo usuário. O usuário vai informar qual a nota mínima de e, t, p e s que ele deseja buscar, nossa aplicação deve listar quem são os candidatos disponíveis com nota maior ou igual a essas informadas pelo usuário.
Ao buscar por alguém com resultados 4,4,8,8 por exemplo vamos receber que os candidatos 1 e 5 atendem esse critério, foram bem no teste prático e apresentaram um ótimo nível de soft skills!

Temos a seguinte lista de candidatos como exemplo e os resultados:

|Candidato             |Resultado          |                       
|----------------------|-------------------|
| Candidato 1          | e5_t10_p8_s8      |
| Candidato 2          | e10_t7_p7_s8      |
| Candidato 3          | e8_t5_p4_s9       |
| Candidato 4          | e2_t2_p2_s1       |
| Candidato 5          | e10_t10_p8_s9     |

## Funcionalidade
### Buscar candidatos por critérios
- **Busca por nota no formato "eX_tX_pX_sX"**: o usuário pode inserir uma nota no formato 'eX_tX_pX_sX' e o aplicativo retornará os candidatos que possuem exatamente essa nota em todas as etapas do processo seletivo.
- **Busca por notas individuais**: o usuário pode inserir as notas mínimas desejadas para cada etapa do processo seletivo (entrevista, teste teórico, teste prático e avaliação de soft skills) e o aplicativo retornará os candidatos que atendem a esses critérios.
### Cadastrar novo candidato
- **Cadastrar com nota no formato "eX_tX_pX_sX"**: o usuário pode inserir o nome do candidato e sua nota no formato "eX_tX_pX_sX" para cadastrá-lo no sistema.
- **Cadastrar com notas individuais**: o usuário pode inserir o nome do candidato e suas notas individuais para cada etapa do processo seletivo para cadastrá-lo no sistema.
### Outras Funcionalidades
O aplicativo também possui funções para descompactar as notas no formato 'eX_tX_pX_sX' e exibir os candidatos classificados na tela.
## Como Usar
1. Clone ou baixe este repositório para sua máquina.
2. Execute o arquivo index.py em um ambiente Python.
3. Siga as instruções do menu para buscar candidatos por critérios ou cadastrar novos candidatos.

