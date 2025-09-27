#A ACME Inc., uma empresa de 500 funcionários, está tendo problemas de espaço em disco no
#seu servidor de arquivos. Para tentar resolver este problema, o Administrador de Rede precisa
#saber qual o espaço ocupado pelos usuários, e identificar os usuários com maior espaço ocupado.
#Através de um programa, baixado da Internet, ele conseguiu gerar o seguinte arquivo, chamado
#"usuarios.txt":
#alexandre 456123789
#anderson 1245698456
#antonio 123456456
#carlos 91257581
#cesar 987458
#rosemary 789456125
#Neste arquivo, o nome do usuário possui 15 caracteres. A partir deste arquivo, você deve criar um
#programa que gere um relatório, chamado "relatório.txt", no seguinte formato:
#ACME Inc. Uso do espaço em disco pelos usuários
#----------------------------------------------------------------
#--------
#Nr. Usuário Espaço utilizado % do uso
#1 alexandre 434,99 MB 16,85%
#2 anderson 1187,99 MB 46,02%
#3 antonio 117,73 MB 4,56%
#4 carlos 87,03 MB 3,37%
#5 cesar 0,94 MB 0,04%
#6 rosemary 752,88 MB 29,16%
#Espaço total ocupado: 2581,57 MB
#Espaço médio ocupado: 430,26 MB
#O arquivo de entrada deve ser lido uma única vez, e os dados armazenados em memória, caso
#sejam necessários, de forma a agilizar a execução do programa. A conversão da espaço ocupado
#em disco, de bytes para megabytes deverá ser feita através de uma função separada, que será
#chamada pelo programa principal. O cálculo do percentual de uso também deverá ser feito através
#de uma função, que será chamada pelo programa principal.

import sys

# --- Funções Auxiliares ---

def bytes_para_mb(n_bytes):
    """Converte um valor de bytes para megabytes."""
    return n_bytes / (1024 * 1024)

def calcular_percentual(espaco_usuario_bytes, espaco_total_bytes):
    """Calcula o percentual de uso de um usuário em relação ao total."""
    if espaco_total_bytes == 0:
        return 0.0
    return (espaco_usuario_bytes / espaco_total_bytes) * 100

# --- 1. Leitura do Arquivo e Armazenamento em Memória ---

usuarios = []
espacos_em_bytes = []

try:
    with open("usuarios.txt", "r", encoding="utf-8") as arquivo_entrada:
        for linha in arquivo_entrada:
            # Pula linhas em branco
            if not linha.strip():
                continue
            
            # Divide a linha em nome e espaço
            partes = linha.split()
            nome = partes[0]
            espaco = int(partes[1])
            
            # Armazena os dados nas listas
            usuarios.append(nome)
            espacos_em_bytes.append(espaco)

except FileNotFoundError:
    print("Erro: O arquivo 'usuarios.txt' não foi encontrado.")
    print("Por favor, crie o arquivo no mesmo diretório do programa.")
    sys.exit() # Encerra o programa se o arquivo não existe
except (ValueError, IndexError):
    print("Erro: O arquivo 'usuarios.txt' contém uma linha com formato inválido.")
    sys.exit()

# --- 2. Cálculos Necessários ---

# Calcula o espaço total e médio
total_ocupado_bytes = sum(espacos_em_bytes)
total_ocupado_mb = bytes_para_mb(total_ocupado_bytes)

# Evita divisão por zero se o arquivo estiver vazio
if len(usuarios) > 0:
    media_ocupada_mb = total_ocupado_mb / len(usuarios)
else:
    media_ocupada_mb = 0

# --- 3. Geração do Arquivo de Relatório ---

try:
    with open("relatório.txt", "w", encoding="utf-8") as arquivo_saida:
        # Escreve o cabeçalho
        arquivo_saida.write("ACME Inc.       Uso do espaço em disco pelos usuários\n")
        arquivo_saida.write("-" * 72 + "\n")
        arquivo_saida.write(f"{'Nr.':<5}{'Usuário':<15}{'Espaço utilizado':>20}{'% do uso':>15}\n")
        
        # Escreve os dados de cada usuário
        for i, usuario in enumerate(usuarios):
            espaco_usuario_bytes = espacos_em_bytes[i]
            espaco_usuario_mb = bytes_para_mb(espaco_usuario_bytes)
            percentual_uso = calcular_percentual(espaco_usuario_bytes, total_ocupado_bytes)
            
            # Formata a linha para alinhar as colunas
            linha_usuario = (f"{i+1:<5}"
                             f"{usuario:<15}"
                             f"{espaco_usuario_mb:>15.2f} MB"
                             f"{percentual_uso:>15.2f}%\n")
            arquivo_saida.write(linha_usuario)
            
        # Escreve o rodapé do relatório
        arquivo_saida.write("\n")
        arquivo_saida.write(f"Espaço total ocupado: {total_ocupado_mb:.2f} MB\n")
        arquivo_saida.write(f"Espaço médio ocupado: {media_ocupada_mb:.2f} MB\n")

    print("Relatório 'relatório.txt' gerado com sucesso!")

except IOError as e:
    print(f"Ocorreu um erro ao escrever o arquivo de relatório: {e}")