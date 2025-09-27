# Exercício 1
# Faça um algoritmo que leia uma frase e diga quantas
# vogais existem na frase digitada.(considerar apenas AaEeIiOoUu)


frase = input("Digite uma frase: ")
vogais = "aeiouAEIOU"
contador = sum(1 for letra in frase if letra in vogais)
print(f"Quantidade de vogais: {contador}")


#Explicação:
#vogais → contém todas as vogais maiúsculas e minúsculas.
#for letra in frase if letra in vogais → percorre a frase e só conta se for vogal.
#sum(1 for ...) → soma 1 para cada vogal encontrada.