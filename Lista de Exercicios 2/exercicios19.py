#Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete feita a um grande
#quantidade de organizações:
#"Qual o melhor Sistema Operacional para uso em servidores?"
#As possíveis respostas são:
#1- Windows Server
#2- Unix
#3- Linux
#4- Netware
#5- Mac OS
#6- Outro
#Você foi contratado para desenvolver um programa que leia o resultado da enquete e informe ao
#final o resultado da mesma. O programa deverá ler os valores até ser informado o valor 0, que
#encerra a entrada dos dados. Não deverão ser aceitos valores além dos válidos para o programa
#(0 a 6). Os valores referentes a cada uma das opções devem ser armazenados numa lista. Após
#os dados terem sido completamente informados, o programa deverá calcular a percentual de cada
#um dos concorrentes e informar o vencedor da enquete. O formato da saída foi dado pela empresa,
#e é o seguinte:
#Sistema Operacional Votos %
#------------------- ----- ---
#Windows Server 1500 17%
#Unix 3500 40%
#Linux 3000 34%
#Netware 500 5%
#Mac OS 150 2%
#Outro 150 2%
#------------------- -----
#Total 8800
#O Sistema Operacional mais votado foi o Unix, com 3500 votos,
#correspondendo a 40% dos votos.

# --- 1. Inicialização ---

# Lista com os nomes dos Sistemas Operacionais. A ordem é importante.
opcoes_so = [
    "Windows Server", 
    "Unix", 
    "Linux", 
    "Netware", 
    "Mac OS", 
    "Outro"
]

# Lista para armazenar os votos. O tamanho é 7 para usar os índices 1 a 6
# diretamente, correspondendo às opções. O índice 0 não será usado.
votos = [0] * 7

# --- 2. Coleta de Votos ---

print("Qual o melhor Sistema Operacional para uso em servidores?")
print("\nAs possíveis respostas são:")
print("1- Windows Server")
print("2- Unix")
print("3- Linux")
print("4- Netware")
print("5- Mac OS")
print("6- Outro")

while True:
    try:
        voto = int(input("\nDigite seu voto (0 para encerrar): "))

        # Condição de parada
        if voto == 0:
            break

        # Validação da entrada
        if voto < 1 or voto > 6:
            print("Valor inválido. Por favor, digite um número entre 1 e 6, ou 0 para sair.")
            continue
        
        # Computa o voto válido
        votos[voto] += 1

    except ValueError:
        print("Entrada inválida. Por favor, digite um número.")

# --- 3. Processamento e Geração do Relatório ---

# Calcula o total de votos computados
total_votos = sum(votos)

# Verifica se houve votos para evitar divisão por zero
if total_votos == 0:
    print("\nNenhum voto foi computado. Encerrando programa.")
else:
    # Imprime o cabeçalho do relatório
    print("\nSistema Operacional     Votos   %")
    print("-------------------     -----   ---")

    # Variáveis para encontrar o vencedor
    votos_vencedor = 0
    nome_vencedor = ""

    # Itera de 1 a 6 para exibir os resultados de cada S.O.
    for i in range(1, 7):
        nome_so = opcoes_so[i-1]  # O nome está no índice (voto - 1)
        num_votos = votos[i]
        
        percentual = (num_votos / total_votos) * 100
        
        # Imprime a linha formatada para cada S.O.
        # A formatação com <24 e <8 alinha as colunas
        print(f"{nome_so:<24}{num_votos:<8}{percentual:.0f}%")
        
        # Verifica se este S.O. é o novo vencedor
        if num_votos > votos_vencedor:
            votos_vencedor = num_votos
            nome_vencedor = nome_so
            
    # Imprime o rodapé e o total
    print("-------------------     -----")
    print(f"Total                   {total_votos}")
    
    # Calcula o percentual do vencedor para a frase final
    percentual_vencedor = (votos_vencedor / total_votos) * 100
    
    # Imprime a conclusão
    print(f"\nO Sistema Operacional mais votado foi o {nome_vencedor}, com {votos_vencedor} votos,")
    print(f"correspondendo a {percentual_vencedor:.0f}% dos votos.")