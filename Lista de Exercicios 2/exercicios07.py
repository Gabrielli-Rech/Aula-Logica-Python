#Faça um Programa que leia uma lista de 5 números inteiros, mostre a soma, a multiplicação e os
#números.

# 1. Inicializa a lista e as variáveis para os cálculos
numeros = []
soma = 0
multiplicacao = 1 # A multiplicação começa com 1 (elemento neutro)

print("Por favor, digite 5 números inteiros.")

# 2. Laço para ler os 5 números
for i in range(5):
    # Loop para garantir que a entrada seja um número inteiro válido
    while True:
        try:
            numero = int(input(f"Digite o {i+1}º número: "))
            numeros.append(numero)
            break # Encerra o 'while' se o número for válido
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

# 3. Calcula a soma dos números usando a função built-in sum()
soma = sum(numeros)

# 4. Calcula a multiplicação percorrendo a lista
for numero in numeros:
    multiplicacao = multiplicacao * numero

# 5. Exibe todos os resultados
print("\n==================================")
print("Resultados:")
print("----------------------------------")
print(f"Os números digitados foram: {numeros}")
print(f"A soma dos números é: {soma}")
print(f"A multiplicação dos números é: {multiplicacao}")
print("==================================")