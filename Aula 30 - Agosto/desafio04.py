# Desafio 4
# Crie um código que imprima o retângulo abaixo.
# lendo a quantidade de linhas e colunas.
# Utilize o comando for

##########
#        #
# ###### #
# #    # #
# #    # #
# #    # #
# #    # #
# #    # #
# ###### #
#        #
##########

linhas = 10
colunas = 10

for i in range(linhas):
    for j in range(colunas):
        # Bordas externas
        if i == 0 or i == linhas - 1 or j == 0 or j == colunas - 1:
            print("#", end="")
        # Segunda camada (linhas 2 e linhas -3 ou colunas 2 e colunas -3)
        elif (i == 2 or i == linhas - 3) and (j > 1 and j < colunas - 2):
            print("#", end="")
        # Camadas internas
        elif (j == 2 or j == colunas - 3) and (i > 1 and i < linhas - 2):
            print("#", end="")
        else:
            print(" ", end="")
    print()

# Explicação:
# O loop for percorre as linhas e colunas para imprimir o padrão.
# As bordas externas são sempre impressas.
# A segunda camada é impressa nas linhas 2 e linhas - 3, e colunas 2 e colunas - 3.
# As camadas internas são impressas nas colunas 2 e colunas - 3, e linhas > 1 e linhas < linhas - 2.
#Loop duplo (for i e for j) → percorre linhas e colunas.
#Condições:
#Primeira e última linha ou primeira e última coluna → imprime #.
#Segunda camada horizontal (i == 2 ou i == linhas-3) → imprime # entre os limites internos.
#Segunda camada vertical (j == 2 ou j == colunas-3) → imprime # nas laterais internas.
#Caso contrário, imprime espaço " ".