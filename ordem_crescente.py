# Lê 3 números inteiros
def ler_numeros():
    numeros = []
    for i in range(3):
        numero = int(input(f"Digite o {i+1}° número inteiro: "))
        numeros.append(numero)
    return numeros


# Imprime os números em ordem crescente
def imprimir_ordem_crescente(numeros):
    numeros_ordenados = sorted(numeros)
    print("Números em ordem crescente: ")
    for numero in numeros_ordenados:
        print(numero)


def main():
    print("Este programa ordena três números inteiros em ordem crescente.")
    numeros = ler_numeros()
    imprimir_ordem_crescente(numeros)


if __name__ == "__main__":
    main()
