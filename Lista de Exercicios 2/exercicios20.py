#As Organizações Tabajara resolveram dar um abono aos seus colaboradores em reconhecimento
#ao bom resultado alcançado durante o ano que passou. Para isto contratou você para desenvolver
#a aplicação que servirá como uma projeção de quanto será gasto com o pagamento deste abono.
#o Após reuniões envolvendo a diretoria executiva, a diretoria financeira e os representantes
#do sindicato laboral, chegou-se a seguinte forma de cálculo:
#o a.Cada funcionário receberá o equivalente a 20% do seu salário bruto de dezembro; a.O
#piso do abono será de 100 reais, isto é, aqueles funcionários cujo salário for muito baixo,
#recebem este valor mínimo; Neste momento, não se deve ter nenhuma preocupação com
#colaboradores com tempo menor de casa, descontos, impostos ou outras
#particularidades. Seu programa deverá permitir a digitação do salário de um número
#indefinido (desconhecido) de salários. Um valor de salário igual a 0 (zero) encerra a
#digitação. Após a entrada de todos os dados o programa deverá calcular o valor do abono
#concedido a cada colaborador, de acordo com a regra definida acima. Ao final, o
#programa deverá apresentar:
#o O salário de cada funcionário, juntamente com o valor do abono;
#o O número total de funcionário processados;
#o O valor total a ser gasto com o pagamento do abono;
#o O número de funcionário que receberá o valor mínimo de 100 reais;
#o O maior valor pago como abono; A tela abaixo é um exemplo de execução do programa,
#apenas para fins ilustrativos. Os valores podem mudar a cada execução do programa.
#Projeção de Gastos com Abono
#Exercícios Utilizando Listas
#============================
#Salário: 1000
#Salário: 300
#Salário: 500
#Salário: 100
#Salário: 4500
#Salário: 0
#Salário - Abono
#R$ 1000.00 - R$ 200.00
#R$ 300.00 - R$ 100.00
#R$ 500.00 - R$ 100.00
#R$ 100.00 - R$ 100.00
#R$ 4500.00 - R$ 900.00
#Foram processados 5 colaboradores
#Total gasto com abonos: R$ 1400.00
#Valor mínimo pago a 3 colaboradores
#Maior valor de abono pago: R$ 900.00

# --- 1. Coleta de Dados ---

# Inicializa uma lista vazia para armazenar os salários
salarios = []

print("Projeção de Gastos com Abono")
print("============================")

while True:
    try:
        entrada_str = input("Salário: ").replace(',', '.')
        salario = float(entrada_str)

        # Condição de parada
        if salario == 0:
            break
        
        # Adiciona apenas salários válidos (positivos)
        if salario > 0:
            salarios.append(salario)
        else:
            print("Por favor, insira um salário com valor positivo.")

    except ValueError:
        print("Entrada inválida. Por favor, digite um número.")

# --- 2. Cálculo dos Abonos ---

# Lista para armazenar os abonos calculados
abonos = []
# Contador para funcionários que recebem o valor mínimo
colaboradores_piso = 0

for salario in salarios:
    # a. Calcula 20% do salário
    abono_calculado = salario * 0.20
    
    # b. Aplica a regra do piso de R$ 100,00
    if abono_calculado < 100:
        abono_final = 100.00
        colaboradores_piso += 1
    else:
        abono_final = abono_calculado
        
    abonos.append(abono_final)

# --- 3. Geração do Relatório ---

# Verifica se algum dado foi processado
if not salarios:
    print("\nNenhum salário foi informado.")
else:
    print("\nSalário   - Abono")
    
    # Imprime a lista de salários e abonos
    for i in range(len(salarios)):
        # :>9.2f formata o número para ter 9 caracteres de largura, alinhado à direita, com 2 casas decimais
        print(f"R$ {salarios[i]:>9.2f} - R$ {abonos[i]:>9.2f}")

    # Imprime as estatísticas finais
    total_colaboradores = len(salarios)
    total_gasto_abonos = sum(abonos)
    maior_abono_pago = max(abonos)

    print(f"\nForam processados {total_colaboradores} colaboradores")
    print(f"Total gasto com abonos: R$ {total_gasto_abonos:.2f}")
    print(f"Valor mínimo pago a {colaboradores_piso} colaboradores")
    print(f"Maior valor de abono pago: R$ {maior_abono_pago:.2f}")