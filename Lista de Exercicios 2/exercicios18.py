#Uma grande emissora de televisão quer fazer uma enquete entre os seus telespectadores para
#saber qual o melhor jogador após cada jogo. Para isto, faz-se necessário o desenvolvimento de
#um programa, que será utilizado pelas telefonistas, para a computação dos votos. Sua equipe foi
#contratada para desenvolver este programa, utilizando a linguagem de programação C++. Para
#computar cada voto, a telefonista digitará um número, entre 1 e 23, correspondente ao número da
#camisa do jogador. Um número de jogador igual zero, indica que a votação foi encerrada. Se um
#número inválido for digitado, o programa deve ignorá-lo, mostrando uma breve mensagem de
#aviso, e voltando a pedir outro número. Após o final da votação, o programa deverá exibir:
#a. O total de votos computados;
#b. Os númeos e respectivos votos de todos os jogadores que receberam votos;
#c. O percentual de votos de cada um destes jogadores;
#d. O número do jogador escolhido como o melhor jogador da partida, juntamente com o
#número de votos e o percentual de votos dados a ele.
#§ Observe que os votos inválidos e o zero final não devem ser computados como
#votos. O resultado aparece ordenado pelo número do jogador. O programa deve
#fazer uso de arrays. O programa deverá executar o cálculo do percentual de
#cada jogador através de uma função. Esta função receberá dois parâmetros: o
#número de votos de um jogador e o total de votos. A função calculará o
#percentual e retornará o valor calculado. Abaixo segue uma tela de exemplo. O
#disposição das informações deve ser o mais próxima possível ao exemplo. Os
#dados são fictícios e podem mudar a cada execução do programa. Ao final, o
#programa deve ainda gravar os dados referentes ao resultado da votação em
#um arquivo texto no disco, obedecendo a mesma disposição apresentada na
#tela.
#Enquete: Quem foi o melhor jogador?
#Número do jogador (0=fim): 9
#Número do jogador (0=fim): 10
#Número do jogador (0=fim): 9
#Número do jogador (0=fim): 10
#Número do jogador (0=fim): 11
#Número do jogador (0=fim): 10
#Número do jogador (0=fim): 50
#Informe um valor entre 1 e 23 ou 0 para sair!
#Número do jogador (0=fim): 9
#Número do jogador (0=fim): 9
#Número do jogador (0=fim): 0
#Resultado da votação:
#Foram computados 8 votos.
#Jogador Votos %
#9 4 50,0%
#Exercícios Utilizando Listas
#10 3 37,5%
#11 1 12,5%
#O melhor jogador foi o número 9, com 4 votos, correspondendo a 50%
#do total de votos.

# --- 1. Função para Cálculo de Percentual ---
def calcular_percentual(votos_jogador, total_votos):
    """
    Calcula o percentual de votos de um jogador em relação ao total.
    Recebe: número de votos do jogador e o total de votos.
    Retorna: o percentual calculado.
    """
    if total_votos == 0:
        return 0.0
    return (votos_jogador / total_votos) * 100

# --- 2. Coleta de Votos ---

# Utiliza uma lista como "array de contadores". A posição do índice corresponde
# ao número da camisa do jogador. O índice 0 não será usado.
# Tamanho 24 para ter índices de 1 a 23.
votos_por_jogador = [0] * 24 
total_de_votos = 0

print("Enquete: Quem foi o melhor jogador?")

while True:
    try:
        entrada = int(input("Número do jogador (0=fim): "))

        # Condição de parada
        if entrada == 0:
            break

        # Validação do número do jogador
        if entrada < 1 or entrada > 23:
            print("Informe um valor entre 1 e 23 ou 0 para sair!")
            continue # Pula para a próxima iteração do loop

        # Computa o voto válido
        votos_por_jogador[entrada] += 1
        total_de_votos += 1

    except ValueError:
        print("Entrada inválida. Por favor, digite um número.")

# --- 3. Análise dos Dados ---

# Encontra o jogador mais votado
melhor_jogador = 0
max_votos = 0
for jogador_numero, num_votos in enumerate(votos_por_jogador):
    if num_votos > max_votos:
        max_votos = num_votos
        melhor_jogador = jogador_numero

# --- 4. Geração do Relatório ---

# Cria uma lista de strings para armazenar cada linha do relatório
# Isso facilita imprimir na tela e gravar no arquivo com a mesma formatação
relatorio = []

relatorio.append("Resultado da votação:")
relatorio.append(f"\nForam computados {total_de_votos} votos.")
relatorio.append("\nJogador   Votos     %")
relatorio.append("-------------------")

# Itera de 1 a 23 para verificar os votos de cada jogador
for jogador_numero in range(1, len(votos_por_jogador)):
    votos_do_jogador = votos_por_jogador[jogador_numero]

    # Adiciona ao relatório apenas jogadores que receberam votos
    if votos_do_jogador > 0:
        percentual = calcular_percentual(votos_do_jogador, total_de_votos)
        linha = f"{jogador_numero:<10}{votos_do_jogador:<10}{percentual:.1f}%"
        relatorio.append(linha)

# Adiciona a linha final sobre o melhor jogador
percentual_melhor = calcular_percentual(max_votos, total_de_votos)
linha_final = (f"\nO melhor jogador foi o número {melhor_jogador}, com {max_votos} votos, "
               f"correspondendo a {percentual_melhor:.1f}% do total de votos.")
relatorio.append(linha_final)

# Junta todas as linhas do relatório com quebras de linha
texto_do_relatorio = "\n".join(relatorio)

# Exibe o relatório na tela
print("\n" + texto_do_relatorio)

# Grava o relatório em um arquivo de texto
try:
    with open("resultado_enquete.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write(texto_do_relatorio)
    print("\nRelatório salvo com sucesso no arquivo 'resultado_enquete.txt'")
except IOError as e:
    print(f"\nOcorreu um erro ao salvar o arquivo: {e}")