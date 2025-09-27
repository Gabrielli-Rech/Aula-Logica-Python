# Ler um conjunto de 5 dados numéricos e imprimir sua soma e sua média.

# n1 = float(input("Digite um número: "))
# n2 = float(input("Digite outro número: "))
# n3 = float(input("Digite mais um número: "))
# n4 = float(input("Digite outro número: "))
# n5 = float(input("Digite mais um número: "))
# soma = n1 + n2 + n3 + n4 + n5
# media = soma / 5
# print(f"A soma dos valores é {soma} e a média é {round(media,2)}")



soma = 0
controle = int(input("Qual o número de interações? "))
for x in range(controle):
    n = float(input("Digite um número: "))
    soma = soma + n   # soma += n
media = soma / 5
print(f"A soma dos valores é {soma} e a média é {round(media,2)}")

