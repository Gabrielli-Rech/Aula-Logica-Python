# # O que preciso saber sobre listas?
# # - O que é uma lista?
# # - Para quê serve uma lista?
# # - Métodos utilizados para listas?
# # - .
# lista = [1, 12, 3, 4, 5, 3, 2]
# # Métodos
# # lista.append()
# # lista.pop()
# # lista.index()
# # lista.insert()
# # lista.remove()
# # lista.clear()
# # lista.sort()
# # lista.copy()
# # lista.count()
# # lista.extend()
# # lista.reverse()
# """
# Manipulando uma lista
# ===================================================
# 1- Adicionar um número na lista
# 2- Retirar um elemento da lista
# 3- Retirar um elemento da lista pelo índice
# 4- Localizar a posição de um elemento da lista
# 5- Inserir um elemento em uma posição específica
# 6- Excluir todos elementos da lista
# 7- Mostrar os elementos da lista ordenados
# (Crescente e Decrescente)
# 8- Escolha um elemento e mostre quantos existem
# 9- sair
# """

def manipular_lista():
    """
    Função principal que executa o menu de manipulação de lista.
    """
    # Lista inicial para a manipulação
    lista = [1, 12, 3, 4, 5, 3, 2]

    # Loop infinito que mantém o menu ativo até o usuário escolher sair
    while True:
        # Imprime o cabeçalho e o menu de opções
        print("\n" + "="*51)
        print("Manipulando uma lista")
        print("="*51)
        print(f"Lista atual: {lista}")
        print("""
        1- Adicionar um número na lista
        2- Retirar um elemento da lista pelo valor
        3- Retirar um elemento da lista pelo índice
        4- Localizar a posição de um elemento da lista
        5- Inserir um elemento em uma posição específica
        6- Excluir todos os elementos da lista
        7- Mostrar os elementos da lista ordenados
        8- Contar ocorrências de um elemento
        9- Sair
        """)

        escolha = input("Escolha uma opção: ")

        # 1- Adicionar um número na lista (append)
        if escolha == '1':
            try:
                numero = int(input("Digite o número para adicionar: "))
                lista.append(numero)
                print(f"O número {numero} foi adicionado ao final da lista.")
            except ValueError:
                print("Erro: Por favor, digite um número inteiro válido.")

        # 2- Retirar um elemento da lista pelo valor (remove)
        elif escolha == '2':
            try:
                numero = int(input("Digite o número para remover: "))
                # O método .remove() causa um erro se o item não existir,
                # por isso verificamos primeiro.
                if numero in lista:
                    lista.remove(numero)
                    print(
                        f"A primeira ocorrência do número {numero} foi removida.")
                else:
                    print(f"O número {numero} não foi encontrado na lista.")
            except ValueError:
                print("Erro: Por favor, digite um número inteiro válido.")

        # 3- Retirar um elemento da lista pelo índice (pop)
        elif escolha == '3':
            try:
                indice = int(
                    input("Digite o índice do elemento para remover: "))
                elemento_removido = lista.pop(indice)
                print(
                    f"O elemento '{elemento_removido}' no índice {indice} foi removido.")
            except IndexError:
                print("Erro: Índice inválido. Está fora do alcance da lista.")
            except ValueError:
                print("Erro: Por favor, digite um número de índice válido.")

        # 4- Localizar a posição de um elemento da lista (index)
        elif escolha == '4':
            try:
                numero = int(
                    input("Digite o número para localizar o índice: "))
                if numero in lista:
                    posicao = lista.index(numero)
                    print(
                        f"A primeira ocorrência do número {numero} está no índice {posicao}.")
                else:
                    print(f"O número {numero} não foi encontrado na lista.")
            except ValueError:
                print("Erro: Por favor, digite um número inteiro válido.")

        # 5- Inserir um elemento em uma posição específica (insert)
        elif escolha == '5':
            try:
                indice = int(input("Digite o índice onde deseja inserir: "))
                numero = int(input("Digite o número para inserir: "))
                lista.insert(indice, numero)
                print(f"O número {numero} foi inserido no índice {indice}.")
            except ValueError:
                print(
                    "Erro: Por favor, digite números inteiros válidos para o índice e o valor.")

        # 6- Excluir todos os elementos da lista (clear)
        elif escolha == '6':
            lista.clear()
            print("Todos os elementos da lista foram excluídos.")

        # 7- Mostrar os elementos da lista ordenados (sort)
        elif escolha == '7':
            # Criamos uma cópia para não alterar a ordem original da lista principal
            lista_crescente = lista.copy()
            lista_crescente.sort()
            print(f"Lista em ordem crescente: {lista_crescente}")

            lista_decrescente = lista.copy()
            lista_decrescente.sort(reverse=True)
            print(f"Lista em ordem decrescente: {lista_decrescente}")

        # 8- Contar ocorrências de um elemento (count)
        elif escolha == '8':
            try:
                numero = int(
                    input("Digite o número para contar as ocorrências: "))
                ocorrencias = lista.count(numero)
                print(
                    f"O número {numero} aparece {ocorrencias} vez(es) na lista.")
            except ValueError:
                print("Erro: Por favor, digite um número inteiro válido.")

        # 9- Sair
        elif escolha == '9':
            print("Saindo do programa...")
            break

        else:
            print("Opção inválida! Por favor, escolha um número de 1 a 9.")


# A linha abaixo garante que a função só será executada se este arquivo for
# o programa principal, e não se for importado por outro script.
if __name__ == "__main__":
    manipular_lista()
