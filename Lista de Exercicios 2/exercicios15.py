#Faça um programa que leia um número indeterminado de valores, correspondentes a notas,
#encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser
#armazenado). Após esta entrada de dados, faça:
#a. Mostre a quantidade de valores que foram lidos;
#b. Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
#c. Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
#d. Calcule e mostre a soma dos valores;
#e. Calcule e mostre a média dos valores;
#f. Calcule e mostre a quantidade de valores acima da média calculada;
#g. Calcule e mostre a quantidade de valores abaixo de sete;
#h. Encerre o programa com uma mensagem;

# --- FASE 1: Coleta de Dados ---

# Inicializa uma lista vazia para armazenar as notas
notas = []

print("--- Entrada de Notas ---")
print("Digite as notas dos alunos. Digite '-1' para encerrar a entrada.")

while True:
    try:
        # Pede ao usuário para digitar um valor
        entrada_str = input(f"Digite a {len(notas) + 1}ª nota (ou -1 para parar): ").replace(',', '.')
        valor = float(entrada_str)

        # Verifica a condição de parada
        if valor == -1:
            break  # Encerra o loop 'while'

        # Se não for -1, armazena o valor na lista
        notas.append(valor)

    except ValueError:
        print("Entrada inválida. Por favor, digite um número.")

# --- FASE 2: Análise e Exibição dos Dados ---
print("\n=============================================")
print("           RELATÓRIO DAS NOTAS")
print("=============================================")

# Verifica se alguma nota foi inserida para evitar erros
if not notas:
    print("Nenhuma nota foi inserida.")
else:
    # a. Mostra a quantidade de valores que foram lidos
    quantidade = len(notas)
    print(f"a. Quantidade de valores lidos: {quantidade}")

    # b. Exibe todos os valores na ordem em que foram informados
    print("\nb. Valores informados (lado a lado):")
    for nota in notas:
        print(nota, end=" | ")
    print("\n") # Pula uma linha no final

    # c. Exibe todos os valores na ordem inversa
    print("c. Valores na ordem inversa (um abaixo do outro):")
    for nota in reversed(notas):
        print(nota)

    # d. Calcule e mostre a soma dos valores
    soma = sum(notas)
    print(f"\nd. Soma dos valores: {soma:.2f}")

    # e. Calcule e mostre a média dos valores
    media = soma / quantidade
    print(f"e. Média dos valores: {media:.2f}")

    # f. Calcule e mostre a quantidade de valores acima da média
    acima_da_media = 0
    for nota in notas:
        if nota > media:
            acima_da_media += 1
    print(f"f. Quantidade de valores acima da média: {acima_da_media}")

    # g. Calcule e mostre a quantidade de valores abaixo de sete
    abaixo_de_sete = 0
    for nota in notas:
        if nota < 7:
            abaixo_de_sete += 1
    print(f"g. Quantidade de valores abaixo de sete: {abaixo_de_sete}")

print("\n=============================================")
# h. Encerre o programa com uma mensagem
print("h. Programa encerrado com sucesso!")
print("=============================================")