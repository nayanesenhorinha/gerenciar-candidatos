class Candidato:
    def __init__(self, nome, entrevista, teste_teórico, teste_prático, soft_skills):
        self.nome = nome
        self.entrevista = entrevista
        self.teste_teórico = teste_teórico
        self.teste_prático = teste_prático
        self.soft_skills = soft_skills

# Lista de candidatos
candidatos = [
    Candidato("Candidato 1", 5, 10, 8, 8),
    Candidato("Candidato 2", 10, 7, 7, 8),
    Candidato("Candidato 3", 8, 5, 4, 9),
    Candidato("Candidato 4", 2, 2, 2, 1),
    Candidato("Candidato 5", 10, 10, 8, 9)
]

def buscar_candidatos(min_entrevista, min_teste_teórico, min_teste_prático, min_soft_skills):
    candidatos_selecionados = []
    for candidato in candidatos:
        if (candidato.entrevista >= min_entrevista and
            candidato.teste_teórico >= min_teste_teórico and
            candidato.teste_prático >= min_teste_prático and
            candidato.soft_skills >= min_soft_skills):
            candidatos_selecionados.append(candidato)
    return candidatos_selecionados

def cadastrar_candidato():
    nome = input("Digite o nome do candidato: ")
    entrevista = int(input("Digite a nota na entrevista: "))
    teste_teórico = int(input("Digite a nota no teste teórico: "))
    teste_prático = int(input("Digite a nota no teste prático: "))
    soft_skills = int(input("Digite a nota em soft skills: "))
    candidatos.append(Candidato(nome, entrevista, teste_teórico, teste_prático, soft_skills))
    print("Candidato cadastrado com sucesso!")

def main():
    while True:
        print("\n1. Buscar candidatos")
        print("2. Cadastrar novo candidato")
        print("3. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            min_entrevista = int(input("Digite a nota mínima na entrevista: "))
            min_teste_teórico = int(input("Digite a nota mínima no teste teórico: "))
            min_teste_prático = int(input("Digite a nota mínima no teste prático: "))
            min_soft_skills = int(input("Digite a nota mínima em soft skills: "))

            candidatos_selecionados = buscar_candidatos(min_entrevista, min_teste_teórico, min_teste_prático, min_soft_skills)

            if len(candidatos_selecionados) == 0:
                print("Nenhum candidato atende aos critérios especificados.")
            else:
                print("Candidatos selecionados:")
                for candidato in candidatos_selecionados:
                    print(candidato.nome)

        elif opcao == "2":
            cadastrar_candidato()

        elif opcao == "3":
            print("Saindo...")
            break

        else:
            print("Opção inválida. Por favor, escolha novamente.")

if __name__ == "__main__":
    main()
