# Exercício 2
# Faça um algoritmo que leia um texto com até 20 caracteres, 
# e imprima esse texto de traz para frente.

texto = input("Digite um texto (até 20 caracteres): ")
print("Texto invertido:", texto[::-1])

#Explicação:
#texto[::-1] → fatiamento invertido da string (começa do fim até o início).
