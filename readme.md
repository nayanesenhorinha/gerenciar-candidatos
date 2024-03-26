﻿# Proj

Hi! I'm your first Markdown file in **StackEdit**. If you want to learn about StackEdit, you can read me. If you want to play with Markdown, you can edit me. Once you have finished with me, you can create new files by opening the **file explorer** on the left corner of the navigation bar.
Oi! Meu nome é Nayane e sou aluno do curso Programadores Cariocas no Mercado Segurador. 

# Contexto
Uma startup está desenvolvendo um **aplicativo** que **verifica a compatibilidade de um candidato com uma vaga** de acordo com seu resultado nas etapas do processo seletivo.
Para isso foi criado um teste que devolve uma string no seguinte formato: **eX_tX_pX_sX** (sendo que cada X é substituído pela avaliação da pessoa em uma das etapas do processo - entrevista, teste teórico, teste prático e avaliação de soft skills).

## O que é para fazer?
**Criar com Python uma lista para armazenar esses resultados** (e outros resultados que quiser no mesmo formato, o código precisa funcionar para qualquer lista que seja inserida nesse formato) e depois **uma função que busca o candidato de acordo com os critérios digitados pelo usuário**.

## Como fazer?
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

# Resultados
A aplicação exive um menu com três opções:
> Buscar candidatos por critérios: o usuário pode definir notas de corte, inserindo cada nota individualmente (entrevista, teste teórico, teste prático e avaliação de soft skills) ou no formato eX_tX_pX_sX.
> Cadastrar um novo candidato: o usuário pode consultar cada nota ndividualmente (entrevista, teste teórico, teste prático e avaliação de soft skills) ou no formato eX_tX_pX_sX.

As informações, notas e nomes, ficam armazenadas em listas na aplicação. A aplicação compacta (e4_t4_p8_s8) e descompacta (4,4,8,8) as notas para fornecer ao usuários opção de lidar com os dados da forma como ele quiser, mas nas listas, os dados são armazenados seguindo o padrão estabelecido (eX_tX_pX_sX)

## Instalação
A aplicação é simples e pode ser compilada em qualquer IDE para Python.