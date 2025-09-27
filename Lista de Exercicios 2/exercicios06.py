#Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene numa lista a média
#de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.

# 1. Inicializa a lista que vai armazenar as médias e o contador de alunos aprovados
lista_de_medias = []
alunos_aprovados = 0

# Número de alunos e notas a serem lidas
num_alunos = 10
num_notas = 4

print(f"--- Coleta de Notas de {num_alunos} Alunos ---")

# 2. Laço principal para percorrer cada aluno
for i in range(num_alunos):
    print(f"\n--- Aluno {i+1} ---")
    notas_do_aluno = []
    
    # 3. Laço interno para ler as 4 notas do aluno atual
    for j in range(num_notas):
        # Loop para garantir que a entrada seja um número válido
        while True:
            try:
                nota = float(input(f"Digite a {j+1}ª nota: "))
                notas_do_aluno.append(nota)
                break # Encerra o 'while' se a nota for válida
            except ValueError:
                print("Entrada inválida. Por favor, digite um número (ex: 8.5).")
    
    # 4. Calcula a média do aluno atual
    media = sum(notas_do_aluno) / len(notas_do_aluno)
    
    # Adiciona a média calculada à lista de médias
    lista_de_medias.append(media)
    
    print(f"A média do Aluno {i+1} foi: {media:.1f}")

# 5. Laço para contar quantos alunos tiveram média >= 7.0
for media_aluno in lista_de_medias:
    if media_aluno >= 7.0:
        alunos_aprovados += 1

# 6. Exibe o resultado final
print("\n=============================================")
print("Análise Concluída:")
print(f"Todas as médias calculadas: {lista_de_medias}")
print(f"Número de alunos com média maior ou igual a 7.0: {alunos_aprovados}")
print("=============================================")