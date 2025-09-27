# Exercício 4
# Faça um algoritmo que leia uma string no formato de data (dd/mm/aaaa)
# e escreva esta com o nome do mês por extenso.
# Exemplo:
# entrada: 25/04/2025
# saida : 25 de abril de 2025.

meses = [
    "", "janeiro", "fevereiro", "março", "abril", "maio", "junho",
    "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"
]

data = input("Digite a data no formato dd/mm/aaaa: ")

# Validação do formato básico
if len(data) == 10 and data[2] == "/" and data[5] == "/":
    dia, mes, ano = data.split("/")
    
    # Verificar se são números
    if dia.isdigit() and mes.isdigit() and ano.isdigit():
        dia = int(dia)
        mes = int(mes)
        ano = int(ano)
        
        # Validar mês e dia básicos
        if 1 <= mes <= 12 and 1 <= dia <= 31:
            print(f"{dia} de {meses[mes]} de {ano}")
        else:
            print("Data inválida! Verifique o dia ou o mês.")
    else:
        print("Erro! Digite apenas números na data.")
else:
    print("Formato inválido! Use dd/mm/aaaa.")

#Explicação:
#meses[mes] → acessa o nome do mês correspondente ao número.
#Lista meses → Índice do mês (1 = janeiro, 2 = fevereiro...).
#data.split("/") → divide a string em 3 partes.
#mes = int(mes) → converte para número para acessar a lista.