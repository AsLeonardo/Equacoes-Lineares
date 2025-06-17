# Sistema de Equações Lineares - Resolução via Eliminação de Gauss com Pivotamento
# Desenvolvido sem bibliotecas externas, 100% Python puro.

def print_header():
    print("\n" + "=" * 50)
    print("  RESOLUÇÃO DE SISTEMAS LINEARES - PYTHON PURO")
    print("=" * 50 + "\n")

def input_float(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Entrada inválida. Por favor, insira um número real.")

def input_positive_integer(message):
    while True:
        try:
            value = int(input(message))
            if value > 0:
                return value
            else:
                print("Por favor, insira um número inteiro positivo.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número inteiro positivo.")

def display_system(A, B, n):
    print("\nSistema inserido:")
    for i in range(n):
        row = " + ".join([f"({A[i][j]:.2f})x{j+1}" for j in range(n)])
        print(f"{row} = {B[i]:.2f}")
    print()

def gauss_elimination(A, B, n):
    for i in range(n):
        # Pivotamento parcial
        max_row = i
        for k in range(i+1, n):
            if abs(A[k][i]) > abs(A[max_row][i]):
                max_row = k
        if max_row != i:
            A[i], A[max_row] = A[max_row], A[i]
            B[i], B[max_row] = B[max_row], B[i]

        if A[i][i] == 0:
            print("Sistema impossível ou indeterminado. Não é possível resolver.")
            return None

        # Eliminação
        for j in range(i+1, n):
            factor = A[j][i] / A[i][i]
            for k in range(i, n):
                A[j][k] -= factor * A[i][k]
            B[j] -= factor * B[i]

    # Substituição regressiva
    X = [0] * n
    for i in range(n - 1, -1, -1):
        sum_ax = sum(A[i][j] * X[j] for j in range(i+1, n))
        X[i] = (B[i] - sum_ax) / A[i][i]

    return X

def main():
    print_header()

    while True:
        print("Menu:")
        print("1. Resolver um sistema de equações lineares")
        print("2. Sair")

        choice = input("\nEscolha uma opção: ")

        if choice == '1':
            n = input_positive_integer("\nInforme o número de variáveis (n): ")

            # Criação das matrizes
            A = []
            B = []

            print("\nInforme os coeficientes do sistema:")
            for i in range(n):
                row = []
                print(f"\nEquação {i + 1}:")
                for j in range(n):
                    coef = input_float(f"Coeficiente a{i+1}{j+1}: ")
                    row.append(coef)
                const = input_float(f"Termo independente b{i+1}: ")
                A.append(row)
                B.append(const)

            display_system(A, B, n)

            solution = gauss_elimination(A, B, n)

            if solution:
                print("\nSolução encontrada:")
                for i, x in enumerate(solution):
                    print(f"x{i + 1} = {x:.6f}")
                print("\nSistema resolvido com sucesso!\n")
            else:
                print("\nFalha na resolução do sistema.\n")

            print("\n" + "-" * 50 + "\n")

        elif choice == '2':
            print("\nEncerrando o programa. Até logo!")
            break

        else:
            print("\nOpção inválida. Por favor, selecione 1 ou 2.\n")

if __name__ == "__main__":
    main()
