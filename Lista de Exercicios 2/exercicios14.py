#Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As
#perguntas são:
#a. "Telefonou para a vítima?"
#b. "Esteve no local do crime?"
#c. "Mora perto da vítima?"
#d. "Devia para a vítima?"
#e. "Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a
#participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela
#deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como
#"Assassino". Caso contrário, ele será classificado como "Inocente".

# 1. Utiliza uma lista para armazenar as perguntas
perguntas = [
    "Telefonou para a vítima?",
    "Esteve no local do crime?",
    "Mora perto da vítima?",
    "Devia para a vítima?",
    "Já trabalhou com a vítima?"
]

# Inicializa o contador de respostas positivas
respostas_positivas = 0

# --- FASE 1: Interrogatório ---
print("--- INTERROGATÓRIO ---")
print("Responda as perguntas com 'S' para Sim ou 'N' para Não.")
print("-------------------------------------------------------")

# 2. Faz as perguntas e conta as respostas positivas
for pergunta in perguntas:
    # Loop para garantir uma resposta válida (S ou N)
    while True:
        # .strip() remove espaços extras, .lower() converte para minúsculo
        resposta = input(f"{pergunta} (S/N): ").strip().lower()
        if resposta in ['s', 'n']:
            break # Sai do loop se a resposta for válida
        else:
            print("Resposta inválida. Por favor, digite apenas S ou N.")

    # Se a resposta for 's', incrementa o contador
    if resposta == 's':
        respostas_positivas += 1

# --- FASE 2: Classificação ---
print("\n=============================================")
print("Analisando as respostas...")

# 3. Determina a classificação com base no número de respostas positivas
if respostas_positivas == 5:
    classificacao = "Assassino"
elif respostas_positivas >= 3: # Abrange 3 ou 4 respostas positivas
    classificacao = "Cúmplice"
elif respostas_positivas == 2:
    classificacao = "Suspeita"
else: # Abrange 0 ou 1 resposta positiva
    classificacao = "Inocente"

# 4. Exibe o resultado final
print(f"Total de respostas positivas: {respostas_positivas}")
print(f"Classificação final: {classificacao}")
print("=============================================")