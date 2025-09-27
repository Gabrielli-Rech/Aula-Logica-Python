# Fazer um algoritmo para ler dois números e mostrar o maior deles.
# n1 = float(input("Digite um número: "))
# n2 = float(input("Digite outro número: "))
# if : elif : else:
# operadores relacionais: > < >= <= == !=
# Valor-verdade é True ou False
# print("antes do if")
# if n1 > n2:
#     print(f"O número {n1} é maior que {n2}")
# if n2 > n1:
#     print(f"O número {n2} é maior que {n1}")
# if n1 == n2:
#     print("Números iguais.")

# print("após o if")

# Operadores lógicos: or(ou). and(e). not(não)

for laco in range(8):
    n1 = float(input("Digite um número: "))
    # if n1 < 0:
    #     break # finaliza um loop (laço)

    n2 = float(input("Digite outro número: "))
    if not (not (n2 < 0) and not (n1 < 0)):
        break  # finaliza um loop (laço)

    # print("antes do if")
    if n1 > n2:
        print(f"O número {n1} é maior que {n2}")

    elif n2 > n1:
        print(f"O número {n2} é maior que {n1}")

    else:
        print("Números iguais.")

print("FIM do Código.")
#