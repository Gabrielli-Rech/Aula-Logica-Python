#Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus vendedores com base
#em comissões. O vendedor recebe $200 por semana mais 9 por cento de suas vendas brutas
#daquela semana. Por exemplo, um vendedor que teve vendas brutas de $3000 em uma semana
#recebe $200 mais 9 por cento de $3000, ou seja, um total de $470. Escreva um programa (usando
#um array de contadores) que determine quantos vendedores receberam salários nos seguintes
#intervalos de valores:
#a. $200 - $299
#b. $300 - $399
#c. $400 - $499
#d. $500 - $599
#e. $600 - $699
#f. $700 - $799
#g. $800 - $899
#h. $900 - $999
#i. $1000 em diante
#Desafio: Crie ma fórmula para chegar na posição da lista a partir do salário, sem fazer
#vários ifs aninhados.
#Exercícios Utilizando Listas

# --- FASE 1: Inicialização ---

# a. $200 - $299 (índice 0)
# b. $300 - $399 (índice 1)
# ...
# i. $1000+     (índice 8)
# Usamos uma lista de 9 posições, uma para cada faixa.
faixas_salariais = [0] * 9

# Lista com as descrições para a exibição final
descricoes_faixas = [
    "a. $200 - $299",
    "b. $300 - $399",
    "c. $400 - $499",
    "d. $500 - $599",
    "e. $600 - $699",
    "f. $700 - $799",
    "g. $800 - $899",
    "h. $900 - $999",
    "i. $1000 em diante"
]

print("--- Cálculo de Comissão de Vendedores ---")
print("Digite o valor das vendas brutas de cada vendedor.")
print("Digite um valor negativo (ex: -1) para encerrar e ver o relatório.")

# --- FASE 2: Coleta e Processamento dos Dados ---

while True:
    try:
        vendas_brutas = float(input("\nDigite o valor da venda bruta: $"))

        # Condição de parada do loop
        if vendas_brutas < 0:
            break

        # Calcula o salário do vendedor
        salario = 200 + (vendas_brutas * 0.09)
        
        # --- SOLUÇÃO DO DESAFIO ---
        # Fórmula para encontrar o índice da lista a partir do salário
        if salario < 1000:
            # Para salários abaixo de 1000, a fórmula é (salario / 100) - 2
            # Ex: Salário de $450 -> 450 // 100 = 4 -> 4 - 2 = 2. (Índice 2 -> faixa $400-$499)
            indice = int(salario // 100) - 2
        else:
            # Para qualquer salário a partir de 1000, o índice é sempre 8
            indice = 8
        
        # Incrementa o contador na faixa salarial correspondente
        # Verifica se o índice é válido (maior ou igual a 0)
        if indice >= 0:
            faixas_salariais[indice] += 1
        else:
            # Isso pode acontecer se o salário for menor que $200 (vendas negativas),
            # o que não é esperado, mas é bom tratar.
            print(f"Salário de ${salario:.2f} está abaixo da faixa mínima e não foi contado.")

    except ValueError:
        print("Entrada inválida. Por favor, digite um número.")

# --- FASE 3: Exibição do Relatório ---

print("\n=======================================================")
print("          RELATÓRIO DE SALÁRIOS SEMANAL")
print("-------------------------------------------------------")
print("Quantidade de vendedores por faixa salarial:")

for i in range(len(faixas_salariais)):
    descricao = descricoes_faixas[i]
    quantidade = faixas_salariais[i]
    print(f"{descricao}: {quantidade} vendedor(es)")

print("=======================================================")