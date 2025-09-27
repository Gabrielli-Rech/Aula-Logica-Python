#Em uma competição de salto em distância cada atleta tem direito a cinco saltos. O resultado do
#atleta será determinado pela média dos cinco valores restantes. Você deve fazer um programa
#que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois informe
#o nome, os saltos e a média dos saltos. O programa deve ser encerrado quando não for informado
#o nome do atleta. A saída do programa deve ser conforme o exemplo abaixo:
#Atleta: Rodrigo Curvêllo
#Primeiro Salto: 6.5 m
#Segundo Salto: 6.1 m
#Terceiro Salto: 6.2 m
#Quarto Salto: 5.4 m
#Quinto Salto: 5.3 m
#Resultado final:
#Atleta: Rodrigo Curvêllo
#Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3
#Média dos saltos: 5.9 m

# Inicia o loop principal do programa
while True:
    # Pede o nome do atleta. .strip() remove espaços em branco antes e depois.
    nome_atleta = input("Digite o nome do atleta (ou pressione Enter para sair): ").strip()

    # Condição de parada: se o nome for uma string vazia, encerra o loop.
    if not nome_atleta:
        break

    # --- Coleta de Dados do Atleta ---
    
    # Inicializa uma lista vazia para guardar os saltos do atleta atual
    saltos = []
    
    # Lista para ajudar a formatar a saída com os nomes ordinais dos saltos
    nomes_saltos = ["Primeiro", "Segundo", "Terceiro", "Quarto", "Quinto"]

    print(f"\nColetando os 5 saltos para o atleta: {nome_atleta}")
    for i in range(5):
        # Loop para garantir que a entrada seja um número válido
        while True:
            try:
                # Substitui vírgula por ponto para aceitar ambos os formatos (ex: 6,5 e 6.5)
                distancia_str = input(f"Distância do {nomes_saltos[i]} Salto: ").replace(',', '.')
                distancia = float(distancia_str)
                saltos.append(distancia)
                break # Encerra o 'while' se a entrada for válida
            except ValueError:
                print("Entrada inválida. Por favor, digite um número.")

    # --- Cálculo e Exibição do Resultado ---

    # Calcula a média dos saltos
    media_saltos = sum(saltos) / len(saltos)
    
    # Imprime a saída formatada exatamente como no exemplo
    print("\n----------------------------------------")
    print("Resultado final:")
    print(f"Atleta: {nome_atleta}")

    # Imprime os saltos individuais no relatório inicial
    # for i in range(5):
    #     print(f"{nomes_saltos[i]} Salto: {saltos[i]:.1f} m")

    # Formata a lista de saltos para exibição em uma única linha
    saltos_formatado = " - ".join([str(s) for s in saltos])
    
    print(f"Saltos: {saltos_formatado}")
    print(f"Média dos saltos: {media_saltos:.1f} m")
    print("----------------------------------------\n")

# Mensagem de encerramento do programa
print("\nPrograma encerrado.")