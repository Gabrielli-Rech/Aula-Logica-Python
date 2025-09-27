turma = []


def mostrar_menu():
    print("\n--- Sistema de Gestão de Alunos ---")
    print("1. Adicionar Aluno e Notas")
    print("2. Listar Alunos (com média e status)")
    print("3. Sair")
    print("-----------------------------------")


def adicionar_aluno():

    print("\n[ Adicionando Novo Aluno ]")
    nome = input("Digite o nome do aluno: ")

    while True:
        try:
            notas_str = input(
                "Digite as notas do aluno, separadas por vírgula (ex: 7.5, 8, 9.2): ")

            notas = [float(nota.strip()) for nota in notas_str.split(',')]

            if not notas:
                print("Erro: Você precisa inserir pelo menos uma nota.")
                continue

            break
        except ValueError:
            print(
                "Erro: Formato de nota inválido. Por favor, use apenas números e vírgulas.")

    aluno = {
        'nome': nome,
        'notas': notas
    }
    turma.append(aluno)
    print(f"Aluno '{nome}' adicionado com sucesso!")


def listar_alunos():

    print("\n[ Lista de Alunos ]")

    if not turma:
        print("Nenhum aluno cadastrado ainda.")
        return

    for aluno in turma:
        nome = aluno['nome']
        notas = aluno['notas']

        if not notas:
            media = 0
        else:
            media = sum(notas) / len(notas)

        if media >= 7.0:
            status = "Aprovado"
        else:
            status = "Reprovado"

        print(f"- Nome: {nome}")
        print(f"  Notas: {notas}")
        print(f"  Média: {media:.2f}")
        print(f"  Status: {status}\n")


def main():

    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            adicionar_aluno()
        elif opcao == '2':
            listar_alunos()
        elif opcao == '3':
            print("Saindo do sistema. Até logo!")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção de 1 a 3.")


if __name__ == "__main__":
    main()
