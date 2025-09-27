# Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20
#elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros
#vetores.

# 1. Inicializa os três vetores
vetor_A = []
vetor_B = []
vetor_intercalado = []
tamanho = 10

# --- Leitura do primeiro vetor (Vetor A) ---
print(f"--- Digite os {tamanho} elementos do Vetor A ---")
for i in range(tamanho):
    while True:
        try:
            numero = int(input(f"Digite o {i+1}º número para o Vetor A: "))
            vetor_A.append(numero)
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

# --- Leitura do segundo vetor (Vetor B) ---
print(f"\n--- Digite os {tamanho} elementos do Vetor B ---")
for i in range(tamanho):
    while True:
        try:
            numero = int(input(f"Digite o {i+1}º número para o Vetor B: "))
            vetor_B.append(numero)
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

# 3. Gera o terceiro vetor intercalando os elementos
for i in range(tamanho):
    # Adiciona o elemento da posição 'i' do Vetor A
    vetor_intercalado.append(vetor_A[i])
    # Adiciona o elemento da posição 'i' do Vetor B
    vetor_intercalado.append(vetor_B[i])

# 4. Exibe os resultados
print("\n=============================================")
print("Resultado da Intercalação:")
print("---------------------------------------------")
print(f"Vetor A: {vetor_A}")
print(f"Vetor B: {vetor_B}")
print(f"Vetor Intercalado (A e B): {vetor_intercalado}")
print("=============================================")