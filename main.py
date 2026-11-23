"""
Gerenciador de Notas Escolares
Aplicativo de linha de comando feito em Python usando funções.
"""

alunos = []  # lista de dicionários: {"nome": str, "notas": [float, ...], "media": float}


def exibir_menu():
    print("\n===== GERENCIADOR DE NOTAS =====")
    print("1 - Cadastrar aluno")
    print("2 - Listar alunos")
    print("3 - Consultar situação de um aluno")
    print("4 - Ver aluno com maior média")
    print("0 - Sair")


def ler_nota(mensagem):
    """Lê uma nota entre 0 e 10 e devolve como float."""
    while True:
        try:
            nota = float(input(mensagem).replace(",", "."))
            if 0 <= nota <= 10:
                return nota
            print("A nota deve estar entre 0 e 10.")
        except ValueError:
            print("Digite um número válido.")


def calcular_media(notas):
    """Recebe uma lista de notas e retorna a média."""
    return sum(notas) / len(notas)


def verificar_situacao(media):
    """Recebe a média e retorna a situação do aluno."""
    if media >= 7:
        return "Aprovado"
    elif media >= 5:
        return "Em recuperação"
    else:
        return "Reprovado"


def cadastrar_aluno(lista):
    nome = input("Nome do aluno: ").strip()
    if nome == "":
        print("O nome não pode ficar vazio.")
        return

    notas = []
    for i in range(1, 4):
        notas.append(ler_nota(f"Digite a nota {i}: "))

    media = calcular_media(notas)
    lista.append({"nome": nome, "notas": notas, "media": media})
    print(f"Aluno {nome} cadastrado! Média: {media:.2f}")


def listar_alunos(lista):
    if len(lista) == 0:
        print("Nenhum aluno cadastrado.")
        return

    print("\n--- Lista de alunos ---")
    for aluno in lista:
        situacao = verificar_situacao(aluno["media"])
        print(f"{aluno['nome']} | Média: {aluno['media']:.2f} | {situacao}")


def consultar_aluno(lista):
    nome = input("Nome do aluno a consultar: ").strip().lower()
    for aluno in lista:
        if aluno["nome"].lower() == nome:
            print(f"\nAluno: {aluno['nome']}")
            print(f"Notas: {aluno['notas']}")
            print(f"Média: {aluno['media']:.2f}")
            print(f"Situação: {verificar_situacao(aluno['media'])}")
            return
    print("Aluno não encontrado.")


def melhor_aluno(lista):
    if len(lista) == 0:
        print("Nenhum aluno cadastrado.")
        return

    melhor = lista[0]
    for aluno in lista:
        if aluno["media"] > melhor["media"]:
            melhor = aluno
    print(f"Maior média: {melhor['nome']} com {melhor['media']:.2f}")


def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_aluno(alunos)
        elif opcao == "2":
            listar_alunos(alunos)
        elif opcao == "3":
            consultar_aluno(alunos)
        elif opcao == "4":
            melhor_aluno(alunos)
        elif opcao == "0":
            print("Encerrando o programa. Até logo!")
            break
        else:
            print("Opção inválida! Tente novamente.")


main()
