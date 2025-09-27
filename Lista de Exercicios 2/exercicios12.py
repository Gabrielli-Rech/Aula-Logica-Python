#Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos
#alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.

# 1. Inicializa as listas e o contador
lista_idades = []
lista_alturas = []
alunos_contados = 0
num_alunos = 30 # Para testes, você pode diminuir este número para 3 ou 5

print(f"--- Cadastro da Idade e Altura de {num_alunos} Alunos ---")

# --- FASE 1: Coleta de Dados ---
for i in range(num_alunos):
    print(f"\n--- Aluno {i+1}/{num_alunos} ---")
    
    # Pede e valida a IDADE
    while True:
        try:
            idade = int(input(f"Digite a idade do aluno {i+1}: "))
            if idade > 0:
                lista_idades.append(idade)
                break
            else:
                print("Por favor, digite uma idade válida (número positivo).")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro para a idade.")

    # Pede e valida a ALTURA
    while True:
        try:
            altura_str = input(f"Digite a altura (em metros) do aluno {i+1}: ").replace(',', '.')
            altura = float(altura_str)
            if altura > 0:
                lista_alturas.append(altura)
                break
            else:
                print("Por favor, digite uma altura válida (número positivo).")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número para a altura.")

# --- FASE 2: Cálculo da Média de Altura ---
# Verifica se a lista não está vazia para evitar erro de divisão por zero
if lista_alturas:
    soma_das_alturas = sum(lista_alturas)
    media_de_altura = soma_das_alturas / len(lista_alturas)
else:
    media_de_altura = 0

# --- FASE 3: Análise e Contagem ---
# Percorre as listas usando o índice para comparar idade e altura do mesmo aluno
for i in range(num_alunos):
    # Condição 1: Aluno tem mais de 13 anos
    condicao_idade = lista_idades[i] > 13
    
    # Condição 2: Altura do aluno é inferior à média da turma
    condicao_altura = lista_alturas[i] < media_de_altura
    
    # Se AMBAS as condições forem verdadeiras, incrementa o contador
    if condicao_idade and condicao_altura:
        alunos_contados += 1

# --- FASE 4: Exibição do Resultado ---
print("\n===================================================================")
print("Análise Concluída:")
print(f"A média de altura da turma é: {media_de_altura:.2f}m")
print("-------------------------------------------------------------------")
print(f"Resultado: {alunos_contados} alunos com mais de 13 anos possuem altura inferior à média.")
print("===================================================================")