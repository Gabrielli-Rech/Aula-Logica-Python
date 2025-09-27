# Desafio 3
# Crie um código que imprima o triangulo abaixo.
# lendo a quantidade de linhas.


         #
        ###
       #####
      #######
     #########
    ###########
   #############
  ###############
 #################
###################


linhas = int(input("Digite a quantidade de linhas: "))

for i in range(1, linhas + 1):
    print(" " * (linhas - i) + "#" * (2 * i - 1))

#Explicação:
#O loop for percorre os números de 1 até a quantidade de linhas.
#A cada iteração, imprime uma linha com espaços em branco e "#" para formar um triângulo.
#(linhas - i) → Calcula a quantidade de espaços em branco antes dos "#".
#"#" * (2 * i - 1) → Multiplica a string "#" pelo valor de (2 * i - 1), criando a forma do triângulo.
#O usuário escolhe linhas.
#" " * (linhas - i) → Espaços à esquerda para alinhar à direita.
#"#" * (2 * i - 1) → Adiciona os #.
#Exemplo com linhas = 5:
#i=1 → " " * 4 + #
#i=2 → " " * 3 + ###
#i=5 → " " * 0 + #########
#2 * i - 1 → Garante números ímpares (1, 3, 5, 7...).
#Quando i = 1 → imprime 1 #.
#Quando i = 2 → imprime 3 #.
#Quando i = 3 → imprime 5 #.