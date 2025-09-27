# Exercício 3
# Faça um algoritmo que leia um texto e diga quantas
# palavras existem neste texto.

texto = input("Digite um texto: ")
palavras = texto.split()
print(f"Quantidade de palavras: {len(palavras)}")

#Explicação:
#texto.split() → divide o texto em palavras (usa espaço como delimitador).
#len(palavras) → conta quantas palavras foram encontradas.
