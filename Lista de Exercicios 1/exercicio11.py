# Escrever um algoritmo para ler uma temperatura em
# Fahrenheit e apresentá-la convertida em graus
# Centígrados.
#                            (Fahrenheit – 32) x 5
# Fórmula: Centígrados = ----------------------------
#                                       9

f = float(input("Digite a temperatura em Fahrenheit: "))

centigrados = ((f - 32) * 5 ) / 9

print(f"""
    A temperatura {f}Fahrenheit 
    equivale a {centigrados} graus centígrados. """)


