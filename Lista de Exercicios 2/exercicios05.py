#Faça um Programa que leia 20 números inteiros e armazene-os numa lista. Armazene os números
#pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.

# 1. Inicialização das três listas (ou "vetores")
todos_os_numeros = []
numeros_pares = []
numeros_impares = []

print("Por favor, digite 20 números inteiros.")

# 2. Laço para ler os 20 números do usuário
for i in range(20):
  # Loop para garantir que a entrada seja um número inteiro válido
  while True:
    try:
      entrada = input(f"Digite o {i+1}º número: ")
      numero = int(entrada)
      todos_os_numeros.append(numero)
      break # Sai do loop 'while' se a conversão for bem-sucedida
    except ValueError:
      print("Entrada inválida. Por favor, digite um número inteiro.")

# 3. Laço para separar os números em pares e ímpares
for numero in todos_os_numeros:
  # A condição para um número ser par é o resto da divisão por 2 ser igual a 0
  if numero % 2 == 0:
    numeros_pares.append(numero)
  else:
    numeros_impares.append(numero)

# 4. Impressão dos três vetores
print("\n=============================================")
print("Impressão dos resultados:")
print("---------------------------------------------")

print(f"Vetor com todos os números ({len(todos_os_numeros)}):")
print(todos_os_numeros)

print("\n---------------------------------------------")
print(f"Vetor de números PARES ({len(numeros_pares)}):")
print(numeros_pares)

print("\n---------------------------------------------")
print(f"Vetor de números ÍMPARES ({len(numeros_impares)}):")
print(numeros_impares)
print("=============================================")
