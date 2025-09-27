"""
    Lista A
    ---------------------------------
         1    2    3    4    5    6
    +-------------------------------+
    1 |  0 |  0 |  0 |  0 |  0 |  0 |
    2 |  0 |  0 |  0 |  0 |  0 |  0 |
    3 |  0 |  0 |  0 |  0 |  0 |  0 |
    +-------------------------------+
soma     0 |  0 |  0 |  0 |  0 |  0 |

Linha: 2
Coluna: 5
Número: 67




    Lista A
    ---------------------------------
         1    2    3    4    5    6
    +-------------------------------+
    1 |  0 |  0 |  0 |  0 |  0 |  0 |
    2 |  0 |  0 |  0 |  0 | 67 |  0 |
    3 |  0 |  0 |  0 |  0 |  0 |  0 |
    +-------------------------------+
soma     0 |  0 |  0 |  0 | 67 |  0 |

Linha:
"""

import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def exibir_matriz(matriz, somas):
    print("    Lista A")
    print("    ---------------------------------")
    print("         1    2    3    4    5    6")
    print("    +-------------------------------+", end="")
    for i, linha in enumerate(matriz):
        print(f"\n {i+1}  |", end="")
        for numero in linha:
            print(f"{numero:^5}|", end="")
    print("\n    +-------------------------------+", end="")
    print("\nsoma   ", end="")
    for soma in somas:
        print(f"{soma:^5}|", end="")
    print("\n")

# --- Programa Principal ---


matriz_A = [
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0]
]

# Loop principal para interação com o usuário
while True:
    # 2. Calcula a soma das colunas
    soma_colunas = [0] * 6 
    for j in range(6): 
        for i in range(3): 
            soma_colunas[j] += matriz_A[i][j]

    # 3. Exibe o estado atual da matriz
    limpar_tela()
    exibir_matriz(matriz_A, soma_colunas)

    # 4. Pede as coordenadas e o número ao usuário
    try:
        linha_str = input("Linha (1-3) (ou 0 para sair): ")
        linha = int(linha_str)

        if linha == 0:
            print("Programa encerrado.")
            break
        
        coluna = int(input("Coluna (1-6): "))
        numero = int(input("Número a ser inserido: "))

        # 5. Valida as entradas e atualiza a matriz
        if 1 <= linha <= 3 and 1 <= coluna <= 6:
            matriz_A[linha - 1][coluna - 1] = numero
        else:
            input("\nCoordenadas inválidas! Pressione Enter para tentar novamente.")

    except (ValueError, IndexError):
        input("\nEntrada inválida! Pressione Enter para tentar novamente.")