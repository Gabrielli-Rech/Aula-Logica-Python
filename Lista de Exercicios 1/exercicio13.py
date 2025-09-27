
# Ler um número n e imprimir MENSAGEM 1, MENSAGEM 2 ou MENSAGEM 3,
# conforme a condição:
# se n <= 10 imprima MENSAGEM 1,
# se n > 10 e <= 100 imprima MENSAGEM 2
# se n >100 imprima MENSAGEM 3,

num = input("Digite um número qualquer: ")

if num <= 10:
    print("MENSAGEM 1")
elif num > 10 and num <= 100:
    print("MENSAGEM 2")
else:
    print("MENSAGEM 3")
