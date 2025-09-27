print("Digite um número: ")
num1 = int(input())
print("Digite um número: ")
num2 = int(input())
print(num1)
while True:
    n1 = int(input("Digite o primeiro número (0 para sair): "))
    if n1 == 0:
        print("Programa finalizado!")
        break
    if n1 <= 8:
        print("O primeiro número deve ser maior que 8!")
        continue
    n2 = int(input("Digite o segundo número: "))
    if n2 <= 8:
        print("O segundo número deve ser maior que 8!")
        continue
    soma = n1 + n2
    print(f"A soma de {n1} + {n2} é {soma}\n")
