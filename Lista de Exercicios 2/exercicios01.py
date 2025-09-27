# Faça um Programa que leia uma lista de 5 números inteiros e mostre-os

# Cria uma lista vazia para armazenar os números
numeros = []

# Loop para ler os 5 números
print("Digite 5 números inteiros:")
for i in range(5):
  while True:
    try:
      # Lê a entrada do usuário e a converte para inteiro
      numero = int(input(f"Digite o {i+1}º número: "))
      # Adiciona o número à lista
      numeros.append(numero)
      break # Sai do loop 'while' se a conversão for bem-sucedida
    except ValueError:
      # Informa o usuário sobre o erro se a entrada não for um número inteiro válido
      print("Entrada inválida. Por favor, digite um número inteiro.")

# Mostra os números que foram inseridos
print("\nOs números que você digitou foram:")
print(numeros)