# Faça um Programa que leia uma lista A com 10 números inteiros, calcule e mostre a soma dos
#quadrados dos elementos do vetor.

# 1. Inicializa a lista e a variável para a soma
lista_A = []
soma_dos_quadrados = 0
num_elementos = 10

print(f"--- Leitura de {num_elementos} Números Inteiros ---")

# 2. Laço para ler os 10 números do usuário
for i in range(num_elementos):
    # Loop para garantir que a entrada seja um número inteiro válido
    while True:
        try:
            numero = int(input(f"Digite o {i+1}º número: "))
            lista_A.append(numero)
            break # Encerra o 'while' se a entrada for válida
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

# 3. Laço para calcular a soma dos quadrados
for numero in lista_A:
    # Eleva o número ao quadrado e adiciona à soma total
    soma_dos_quadrados += numero ** 2

# 4. Exibe os resultados
print("\n=======================================================")
print(f"O vetor lido foi: A = {lista_A}")
print(f"A soma dos quadrados dos seus elementos é: {soma_dos_quadrados}")
print("=======================================================")
