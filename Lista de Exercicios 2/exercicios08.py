# Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu
#respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida.

# 1. Inicializa as duas listas (vetores)
lista_idades = []
lista_alturas = []

# Define o número de pessoas
num_pessoas = 5

print(f"--- Cadastro de Idade e Altura de {num_pessoas} Pessoas ---")

# 2. Laço de repetição para ler os dados de cada pessoa
for i in range(num_pessoas):
    print(f"\n--- Dados da Pessoa {i+1} ---")
    
    # Pede e valida a IDADE
    while True:
        try:
            idade = int(input(f"Digite a idade da pessoa {i+1}: "))
            lista_idades.append(idade)
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro para a idade.")

    # Pede e valida a ALTURA
    while True:
        try:
            # Substitui vírgula por ponto para aceitar ambos os formatos (ex: 1,75 e 1.75)
            altura_str = input(f"Digite a altura (em metros) da pessoa {i+1}: ").replace(',', '.')
            altura = float(altura_str)
            lista_alturas.append(altura)
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número para a altura.")

# 3. Imprime os dados na ordem inversa
print("\n==================================================")
print("Idade e Altura na ORDEM INVERSA da leitura:")
print("--------------------------------------------------")

# O laço começa no último índice (num_pessoas - 1), vai até -1 (para incluir o 0),
# e decrementa 1 a cada passo (-1).
for i in range(num_pessoas - 1, -1, -1):
    # O índice 'i' irá de 4, 3, 2, 1, 0.
    # Acessamos os dados nessas posições para imprimir na ordem inversa.
    idade = lista_idades[i]
    altura = lista_alturas[i]
    print(f"Pessoa {i+1}: Idade = {idade} anos, Altura = {altura:.2f}m")
    
print("==================================================")