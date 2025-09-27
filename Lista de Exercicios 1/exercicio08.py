# Faça um algoritmo que leia valores para as variáveis a, b e c e
# mostre o resultado da seguinte
# expressão:
# ( a – b ) * c

a = float(input("Digite um número: "))
b = float(input("Digite outro número: "))
c = float(input("Digite mais um número: "))

result = (a-b)*c
print(f"({a}-{b}) * {c} = {result}")