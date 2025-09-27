#Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma
#lista. Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da
#média anual, e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro,
#. . . ).

# 1. Inicializa as listas
temperaturas = []
meses_do_ano = [
    "1 - Janeiro", "2 - Fevereiro", "3 - Março", "4 - Abril", 
    "5 - Maio", "6 - Junho", "7 - Julho", "8 - Agosto",
    "9 - Setembro", "10 - Outubro", "11 - Novembro", "12 - Dezembro"
]

print("--- Digite a temperatura média de cada mês do ano (em ºC) ---")

# --- FASE 1: Coleta das Temperaturas ---
for i in range(12):
    # Loop para garantir que a entrada seja um número válido
    while True:
        try:
            # Pede a temperatura usando o nome do mês correspondente
            temp_str = input(f"Temperatura de {meses_do_ano[i].split(' - ')[1]}: ").replace(',', '.')
            temperatura_mes = float(temp_str)
            temperaturas.append(temperatura_mes)
            break # Encerra o 'while' se a entrada for válida
        except ValueError:
            print("Entrada inválida. Por favor, digite um número (ex: 25.5).")

# --- FASE 2: Cálculo da Média Anual ---
media_anual = sum(temperaturas) / len(temperaturas)

# --- FASE 3: Análise e Exibição dos Resultados ---
print("\n=======================================================")
print("Análise das Temperaturas Anuais")
print("-------------------------------------------------------")
print(f"A média anual de temperatura foi: {media_anual:.2f}ºC")
print("\nTemperaturas acima da média anual:")

# Variável para verificar se alguma temperatura ficou acima da média
acima_da_media = False

for i in range(12):
    # Verifica se a temperatura do mês 'i' é maior que a média
    if temperaturas[i] > media_anual:
        # Mostra o mês (por extenso) e a respectiva temperatura
        print(f" -> {meses_do_ano[i]}: {temperaturas[i]:.1f}ºC")
        acima_da_media = True

# Mensagem caso nenhuma temperatura tenha ficado acima da média
if not acima_da_media:
    print("Nenhuma temperatura registrada ficou acima da média anual.")

print("=======================================================")