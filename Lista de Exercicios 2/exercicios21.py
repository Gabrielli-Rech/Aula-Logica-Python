#Faça um programa que carregue uma lista com os modelos de cinco carros (exemplo de modelos:
#FUSCA, GOL, VECTRA etc). Carregue uma outra lista com o consumo desses carros, isto é,
#quantos quilômetros cada um desses carros faz com um litro de combustível. Calcule e mostre:
#. O modelo do carro mais econômico;
#a. Quantos litros de combustível cada um dos carros cadastrados consome para percorrer
#uma distância de 1000 quilômetros e quanto isto custará, considerando um que a gasolina
#custe R$ 2,25 o litro. Abaixo segue uma tela de exemplo. O disposição das informações
#deve ser o mais próxima possível ao exemplo. Os dados são fictícios e podem mudar a
#cada execução do programa.
#Comparativo de Consumo de Combustível
#Veículo 1
#Nome: fusca
#Km por litro: 7
#Veículo 2
#Nome: gol
#Km por litro: 10
#Veículo 3
#Nome: uno
#Km por litro: 12.5
#Veículo 4
#Nome: Vectra
#Km por litro: 9
#Veículo 5
#Nome: Peugeout
#Km por litro: 14.5
#Relatório Final
#1 - fusca - 7.0 - 142.9 litros - R$ 321.43
#2 - gol - 10.0 - 100.0 litros - R$ 225.00
#3 - uno - 12.5 - 80.0 litros - R$ 180.00
#4 - vectra - 9.0 - 111.1 litros - R$ 250.00
#5 - peugeout - 14.5 - 69.0 litros - R$ 155.17
#O menor consumo é do peugeout.

# --- 1. Inicialização ---

# Listas para armazenar os dados dos carros
modelos = []
consumos = []

# Constantes para os cálculos
num_carros = 5
distancia_km = 1000
preco_gasolina_litro = 2.25

# --- 2. Coleta de Dados ---

print("Comparativo de Consumo de Combustível")

for i in range(num_carros):
    print(f"\nVeículo {i+1}")
    
    # Pede o nome do modelo e valida para não ser vazio
    while True:
        nome = input("Nome: ").strip()
        if nome:
            modelos.append(nome)
            break
        else:
            print("O nome não pode ser vazio. Tente novamente.")

    # Pede o consumo e valida para ser um número positivo
    while True:
        try:
            consumo_km_l = float(input("Km por litro: ").replace(',', '.'))
            if consumo_km_l > 0:
                consumos.append(consumo_km_l)
                break
            else:
                print("O consumo deve ser um número maior que zero.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

# --- 3. Geração do Relatório ---

print("\nRelatório Final")

# Variáveis para encontrar o carro mais econômico
melhor_consumo = 0
modelo_mais_economico = ""

for i in range(num_carros):
    # Pega os dados das listas
    modelo = modelos[i]
    consumo = consumos[i]
    
    # Calcula litros e custo para 1000 km
    litros_para_1000km = distancia_km / consumo
    custo_para_1000km = litros_para_1000km * preco_gasolina_litro
    
    # Imprime a linha formatada do relatório
    print(f"{i+1} - {modelo:<10} - {consumo:>5.1f} - {litros_para_1000km:>7.1f} litros - R$ {custo_para_1000km:>7.2f}")
    
    # --- 4. Análise Final (enquanto gera o relatório) ---
    # Verifica se o carro atual é o mais econômico encontrado até agora
    if consumo > melhor_consumo:
        melhor_consumo = consumo
        modelo_mais_economico = modelo

print(f"\nO menor consumo é do {modelo_mais_economico}.")