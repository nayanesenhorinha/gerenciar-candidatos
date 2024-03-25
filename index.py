# LISTAS 
lista_candidatos_nomes = [
    'Candidato 1',
    'Candidato 2',
    'Candidato 3',
    'Candidato 4',
    'Candidato 5'
]

lista_candidatos_notas = [
    'e5_t10_p8_s8',
    'e10_t7_p7_s8',
    'e8_t5_p4_s9',
    'e2_t2_p2_s1',
    'e10_t10_p8_s9'
]

# OPÇÃO 1: BUSCA CANDIDATOS POR CRITÉRIOS 
def descompactar_nota(nota):
    # Separar as notas por '_'
    notas_separadas = nota.split('_')
    # Converter cada parte para inteiro após remover a letra
    notas_int = [int(nota[1:]) for nota in notas_separadas]
    # Desempacotar as notas
    return notas_int

# OPÇÃO 2: CADASTRAR NOVO CANDIDATO 
def cadastrar_candidato(lista_candidatos_notas,lista_candidatos_nomes):
    #Inputs para entrada de dados
    nome = input("Informe o nome do candidato: ")
    nota_e = int(input('Digite a nota da entrevista: '))
    nota_t = int(input('Digite a nota do teste teórico: '))
    nota_p = int(input('Digite a nota do teste prático: '))
    nota_s = int(input('Digite a nota da avaliação de soft skills: '))
    #Formata as notas para a string, 'eX_tX_pX_sX'
    nota = f'e{nota_e}_t{nota_t}_p{nota_p}_s{nota_s}'
    #Adiciona o nome e a string com as notas nas listas
    lista_candidatos_nomes.append(nome)
    lista_candidatos_notas.append(nota)

# OPÇÃO 1.1: BUSCA OS CANDIDATOS NA LISTA NO FORMATO 'eX_tX_pX_sX'
def busca_candidatos_string(string):
    candidatos_classificados = []
    for nome, nota in zip(lista_candidatos_nomes, lista_candidatos_notas):
        if nota == string:
            candidatos_classificados.append((nome, nota))
    return candidatos_classificados

# OPÇÃO 1.2: BUSCA OS CANDIDATOS NA LISTA COM NOTAS INDIVIDUAIS
def busca_candidatos(nota_entrevista, nota_teorico, nota_pratica, nota_soft):
    #Lista que vai receber os candidatos classificados
    candidatos_classificados = []
    for nome, nota in zip(lista_candidatos_nomes, lista_candidatos_notas):
        # Verificar se atende aos critérios
        e, t, p, s = descompactar_nota(nota)
        if e >= nota_entrevista and t >= nota_teorico and p >= nota_pratica and s >= nota_soft:
            candidatos_classificados.append((nome, nota))
    return candidatos_classificados

# EXIBE OS CANDIDATOS CLASSIFICADOS NA TELA
def exibir_classificados(candidatos_classificados):
    if candidatos_classificados:
        print("\nOs seguintes candidatos atendem aos critérios especificados:")
        for nome, nota in candidatos_classificados:
            e, t, p, s = descompactar_nota(nota)
            print("----------------------------------------------")
            print(f"{nome}\nNota: {nota}\nEntrevista: {e}\nTeste Teórico: {t}\nTeste prático: {p}\nAvaliação de soft skills: {s}")
    else:
        print("\nNenhum candidato atende aos critérios especificados.")

# MENU 
while True:
    print("\nMENU:")
    print("1 - Buscar candidatos por critérios")
    print("2 - Cadastrar novo candidato")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        print("\nComo deseja inserir as notas?")
        print("1 - Formato 'eX_tX_pX_sX'")
        print("2 - Inserir notas individualmente")
        opcao2 = input("Escolha uma opção: ")

        if opcao2 == "1":
            nota = input("Digite a nota: ")
            candidatos_classificados = busca_candidatos_string(nota)
            exibir_classificados(candidatos_classificados)

        elif opcao2 == "2":
            nota_entrevista = int(input("Digite a nota mínima da entrevista: "))
            nota_teorico = int(input("Digite a nota mínima do teste teórico: "))
            nota_pratica = int(input("Digite a nota mínimia do teste prático: "))
            nota_soft = int(input("Digite a nota mínima da avaliação de soft skills: "))

            candidatos_classificados = busca_candidatos(nota_entrevista, nota_pratica, nota_teorico, nota_soft)
            exibir_classificados(candidatos_classificados)

        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

    elif opcao == "2":
        cadastrar_candidato(lista_candidatos_notas,lista_candidatos_nomes)
        print("\nNovo candidato cadastrado com sucesso.")

    elif opcao == "3":
        print("Encerrando o programa.")
        break

    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")