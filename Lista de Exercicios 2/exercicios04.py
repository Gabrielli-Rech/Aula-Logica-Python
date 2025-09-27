#Faça um Programa que leia uma lista de 10 caracteres, e diga quantas consoantes foram lidas.
#Imprima as consoantes.

# 1. Inicializa uma lista vazia para guardar as consoantes e um contador.
consoantes_encontradas = []
contador_consoantes = 0

# Define a lista de vogais para facilitar a verificação.
vogais = ['a', 'e', 'i', 'o', 'u']

print("Digite 10 caracteres.")

# 2. Laço de repetição para ler os 10 caracteres.
for i in range(10):
  # Loop para garantir que o usuário digite apenas um caractere.
  while True:
    caractere = input(f"Digite o {i+1}º caractere: ")
    if len(caractere) == 1:
      break # Se a entrada for válida (um caractere), sai do loop.
    else:
      print("Entrada inválida. Por favor, digite apenas um caractere.")

  # 3. Verifica se o caractere é uma consoante.
  # Condições:
  # - .isalpha()  -> Verdadeiro se for uma letra do alfabeto.
  # - .lower()    -> Converte o caractere para minúsculo para a verificação.
  # - not in vogais -> Verdadeiro se a letra não estiver na lista de vogais.
  if caractere.isalpha() and caractere.lower() not in vogais:
    # Se for uma consoante, adiciona à lista e incrementa o contador.
    consoantes_encontradas.append(caractere)
    contador_consoantes += 1

# 4. Exibe os resultados na tela.
print("\n------------------------------")
print(f"Total de consoantes lidas: {contador_consoantes}")
print(f"As consoantes são: {consoantes_encontradas}")
print("------------------------------")
