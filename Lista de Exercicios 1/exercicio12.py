
# Maria quer saber quantos litros de gasolina precisa colocar
# em seu carro e quanto vai gastar para fazer
# uma viagem até a casa de sua irmã.
# Dados extras:
# - Distância da casa de Maria até sua irmã : 520 km
# - Seu carro consome 12 Km/litro de combustível.
# - Ela abastece sempre no mesmo posto, onde o preço da
#   gasolina é R$ 4,50 o litro.
#
# Desenvolva um algoritmo onde o usuário digite a distância,
# o consumo e o valor do litro de
# combustível, com estes dados o algoritmo deverá calcular a
# quantidade de litros de combustível para a
# viagem e o custo da viagem.

distancia = float(input("Entre com a distância desejada: "))
consumo = float(input("Entre com o consumo de seu carro: "))
val_litro = float(input("Entre o valor do litro: "))

qt_litros = distancia / consumo
custo = qt_litros * val_litro

print(f"Para percorrer {distancia}Km, "
      f"serão necessários {qt_litros} de combustível,"
      f"portanto, serão necessários R${custo} para viagem.")
