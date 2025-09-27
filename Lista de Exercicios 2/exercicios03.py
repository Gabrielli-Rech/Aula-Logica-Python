#Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

# 1. Cria uma lista vazia para armazenar as notas.
notas = []

# Mensagem inicial para o usuário.
print("Por favor, digite as 4 notas.")

# 2. Laço de repetição para ler as 4 notas.
for i in range(4):
  # Loop para garantir que a entrada seja um número válido.
  while True:
    try:
      # Solicita a entrada e a converte para float (número com decimal).
      nota = float(input(f"Digite a {i+1}ª nota: "))
      # Adiciona a nota válida à lista.
      notas.append(nota)
      break # Encerra o loop 'while' se a nota for válida.
    except ValueError:
      # Mensagem de erro se a entrada não for um número.
      print("Entrada inválida. Por favor, digite um número (ex: 7.5).")

# 3. Mostra as notas que foram inseridas.
print("\n--------------------")
print("As notas digitadas foram:")
print(notas)

# 4. Calcula a média.
# A função sum() soma todos os itens da lista.
# A função len() retorna o número de itens na lista.
media = sum(notas) / len(notas)

# 5. Mostra a média formatada com uma casa decimal.
print(f"A média final é: {media:.1f}")
print("--------------------")

