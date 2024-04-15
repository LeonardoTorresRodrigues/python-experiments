def ler_sequecia():
    numeros = []
    while True:
        try:
            num = int(input("Digite um número inteiro (ou 0 para terminar): "))
            if num == 0:
                break
            numeros.append(num)
        except ValueError:
            print("Entrada inválida. Digite apenas números inteiros.")

    return numeros


def imprimir_inverso(sequencia):
    print("Sequência na ordem inversa:")
    for num in reversed(sequencia):
        print(num, end=" ")


def main():
    print("Digite uma sequência de números inteiros para terminar, digite 0")
    sequencia = ler_sequecia()
    imprimir_inverso(sequencia)


if __name__ == "__main__":
    main()
