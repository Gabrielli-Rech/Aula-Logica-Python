#Faça um programa que simule um lançamento de dados. Lance o dado 100 vezes e armazene os
#resultados em uma lista . Depois, mostre quantas vezes cada valor foi conseguido. Dica: use uma
#lista de contadores(1-6) e uma função para gerar numeros aleatórios, simulando os lançamentos
#dos dados.

# 1. Importa a função necessária para gerar números aleatórios
import random

# --- FASE 1: Simulação dos Lançamentos ---

# Lista para armazenar o resultado de cada um dos 100 lançamentos
resultados_dos_lancamentos = []
numero_de_lancamentos = 100

print(f"Simulando o lançamento de um dado {numero_de_lancamentos} vezes...")

# Laço para simular os 100 lançamentos
for _ in range(numero_de_lancamentos):
    # Gera um número aleatório inteiro entre 1 e 6 (simulando um dado)
    resultado = random.randint(1, 6)
    # Adiciona o resultado à nossa lista
    resultados_dos_lancamentos.append(resultado)

# --- FASE 2: Contagem dos Resultados ---

# Dica: Cria uma lista de contadores com 6 posições, todas iniciando em zero.
# O índice 0 contará o número 1, o índice 1 contará o número 2, e assim por diante.
contagem_valores = [0] * 6

# Laço para percorrer a lista de resultados e contar cada valor
for resultado in resultados_dos_lancamentos:
    # A mágica acontece aqui: se o resultado for 1, incrementamos o contador no índice 0.
    # Se for 2, incrementamos no índice 1, e assim sucessivamente.
    contagem_valores[resultado - 1] += 1

# --- FASE 3: Exibição do Relatório Final ---

print("\n--- Resultado da Simulação ---")
# print(f"Resultados obtidos: {resultados_dos_lancamentos}") # Linha opcional para ver todos os lançamentos

print("\nFrequência de cada valor:")
for i in range(6):
    # O valor do dado é (índice + 1)
    valor_dado = i + 1
    # A quantidade de vezes está no contador do índice 'i'
    quantidade = contagem_valores[i]
    
    print(f"O valor {valor_dado} foi obtido {quantidade} vezes.")