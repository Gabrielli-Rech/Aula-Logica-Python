# Fazer um algoritmo para ler duas notas, os pesos de cada nota e
# mostrar a média ponderada.
#                                (nota 1 * peso da nota 1) + (nota 2 * peso da nota 2)
# Cálculo da Média Ponderada = ------------------------------------------------------------------------
#                                                          soma dos pesos


n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
p1 = float(input("Digite o peso para a 1a nota: "))
p2 = float(input("Digite o peso para a 2a nota: "))

result = (n1 * p1 + n2 * p2 ) / (p1 + p2)

print(f"A média ponderada para os valores digitado é: {result}")

