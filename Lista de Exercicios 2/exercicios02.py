#Faça um Programa que leia uma lista de 10 números reais e mostre-os na ordem inversa.

# Cria uma lista vazia para armazenar os números.
numeros_reais = []

# Mensagem inicial para o usuário.
print("Por favor, digite 10 números reais.")

# Laço de repetição para ler os 10 números.
for i in range(10):
  # Loop para garantir que a entrada seja válida
  while True:
    try:
      # Solicita a entrada do usuário, usando f-string para numerar o pedido.
      entrada = input(f"Digite o {i+1}º número: ")
      # Converte a entrada para float (número real) e adiciona à lista.
      numero = float(entrada)
      numeros_reais.append(numero)
      break # Sai do loop 'while' se a conversão for bem-sucedida.
    except ValueError:
      # Caso o usuário digite algo que não seja um número.
      print("Entrada inválida. Por favor, digite um número real válido (ex: 15.5 ou -4).")

# Imprime uma linha em branco para melhor formatação.
print("\n-----------------------------------------")
# Mostra a lista na ordem inversa.
print("Os números na ordem inversa são:")
print(numeros_reais[::-1])