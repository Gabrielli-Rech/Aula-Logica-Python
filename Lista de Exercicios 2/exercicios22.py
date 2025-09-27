#Sua organização acaba de contratar um estagiário para trabalhar no Suporte de Informática, com
#a intenção de fazer um levantamento nas sucatas encontradas nesta área. A primeira tarefa dele
#é testar todos os cerca de 200 mouses que se encontram lá, testando e anotando o estado de
#cada um deles, para verificar o que se pode aproveitar deles.
#Exercícios Utilizando Listas
#o Foi requisitado que você desenvolva um programa para registrar este levantamento. 
#programa deverá receber um número indeterminado de entradas, cada uma
#contendo: um número de identificação do mouse o tipo de defeito:
#o necessita da esfera;
#o necessita de limpeza; a.necessita troca do cabo ou conector; a.quebrado ou
#inutilizado Uma identificação igual a zero encerra o programa. Ao final o programa deverá
#emitir o seguinte relatório:
#Quantidade de mouses: 100
#Situação Quantidade Percentual
#1- necessita da esfera 40 40%
#2- necessita de limpeza 30 30%
#3- necessita troca do cabo ou conector 15 15%
#4- quebrado ou inutilizado 15 15%

# --- 1. Inicialização ---

# Lista com as descrições dos defeitos para o relatório final.
defeitos = [
    "necessita da esfera",
    "necessita de limpeza",
    "necessita troca do cabo ou conector",
    "quebrado ou inutilizado"
]

# Lista para armazenar a contagem de cada defeito.
# O tamanho é 5 para usarmos os índices de 1 a 4 diretamente.
contadores = [0] * 5

# Variável para contar o total de mouses registrados
total_mouses = 0

print("--- Levantamento de Sucatas de Mouses ---")
print("Registre o defeito de cada mouse.")

# --- 2. Coleta de Dados ---

while True:
    try:
        identificacao = int(input("\nNúmero de identificação (0 para encerrar): "))

        # Condição de parada do programa
        if identificacao == 0:
            break

        # Se a identificação for válida, pede o tipo de defeito
        while True: # Loop interno para garantir um defeito válido
            print("\nTipos de defeito:")
            print("1- necessita da esfera")
            print("2- necessita de limpeza")
            print("3- necessita troca do cabo ou conector")
            print("4- quebrado ou inutilizado")
            
            tipo_defeito = int(input("Digite o número do defeito (1-4): "))

            # Validação do tipo de defeito
            if 1 <= tipo_defeito <= 4:
                contadores[tipo_defeito] += 1
                total_mouses += 1
                print("--> Defeito registrado com sucesso.")
                break # Sai do loop de defeitos e volta a pedir uma nova identificação
            else:
                print("Opção inválida. O número do defeito deve ser entre 1 e 4.")
        
    except ValueError:
        print("Entrada inválida. Por favor, digite um número para a identificação.")

# --- 3. Geração do Relatório ---

if total_mouses == 0:
    print("\nNenhum mouse foi cadastrado.")
else:
    print(f"\nQuantidade de mouses: {total_mouses}")
    print("\nSituação                        Quantidade    Percentual")
    
    # Itera de 1 a 4 para exibir os resultados de cada defeito
    for i in range(1, 5):
        descricao = defeitos[i-1] # O nome do defeito está no índice (número - 1)
        quantidade = contadores[i]
        
        percentual = (quantidade / total_mouses) * 100
        
        # Imprime a linha formatada. O alinhamento (<) garante que as colunas fiquem retas.
        print(f"{i}- {descricao:<30} {quantidade:<14} {percentual:.0f}%")