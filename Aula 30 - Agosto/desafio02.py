
# Desafio 2
# Crie um código que imprima o triangulo abaixo.
# lendo a quantidade de linhas.


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

linhas = int(input("Digite a quantidade de linhas: "))

for i in range(1, linhas + 1):
    print(" " * (linhas - i) + "#" * i)

#Explicação:
#O loop for percorre os números de 1 até a quantidade de linhas.
#A cada iteração, imprime uma linha com espaços em branco e "#" para formar um triângulo.
#(linhas - i) → Calcula a quantidade de espaços em branco antes dos "#".
#"#" * i → Multiplica a string "#" pelo valor de i.
#O usuário escolhe linhas.
#" " * (linhas - i) → Espaços à esquerda para alinhar à direita.
#"#" * i → Adiciona os #.
#Exemplo com linhas = 5:
#i=1 → " " * 4 + #
#i=2 → " " * 3 + ##
#i=5 → " " * 0 + #####
