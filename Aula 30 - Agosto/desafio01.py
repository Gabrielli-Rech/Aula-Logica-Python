# Desafio 1
# Crie um código que imprima o triangulo abaixo.
# Utilize o comando for.

#
##
###
####
#####
######
#######
########
#########
##########


for i in range(1, 11):
    print("#" * i)


#Explicação:
#O loop for percorre os números de 1 a 10.
#A cada iteração, imprime uma linha com "#" repetido i vezes.
#for i in range(1, 11) → Cria um loop que vai do 1 ao 10 (10 linhas).
#"#" * i → Multiplica a string "#" pelo valor de i.
#Quando i = 1 → #
#Quando i = 2 → ##
#Quando i = 3 → ###
#print() imprime cada linha.