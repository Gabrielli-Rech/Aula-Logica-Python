# Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.

# 1. Inicializa os quatro vetores
vetor_A = []
vetor_B = []
vetor_C = []
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

# --- Leitura do terceiro vetor (Vetor C) ---
print(f"\n--- Digite os {tamanho} elementos do Vetor C ---")
for i in range(tamanho):
    while True:
        try:
            numero = int(input(f"Digite o {i+1}º número para o Vetor C: "))
            vetor_C.append(numero)
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

# 3. Gera o vetor final intercalando os elementos dos três vetores
for i in range(tamanho):
    # Adiciona o elemento da posição 'i' do Vetor A
    vetor_intercalado.append(vetor_A[i])
    # Adiciona o elemento da posição 'i' do Vetor B
    vetor_intercalado.append(vetor_B[i])
    # Adiciona o elemento da posição 'i' do Vetor C
    vetor_intercalado.append(vetor_C[i])

# 4. Exibe os resultados
print("\n=============================================")
print("Resultado da Intercalação:")
print("---------------------------------------------")
print(f"Vetor A: {vetor_A}")
print(f"Vetor B: {vetor_B}")
print(f"Vetor C: {vetor_C}")
print("---------------------------------------------")
print(f"Vetor Intercalado (A, B e C): {vetor_intercalado}")
print("=============================================")