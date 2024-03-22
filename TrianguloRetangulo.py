def verifica_triangulo_retangulo(a, b, c):
    # Ordena os lados em ordem crescente
    lados = sorted([a, b, c])

    # Verifa se é um triângulo retângulo usando o Teorema de Pitágoras
    if lados[0]**2 + lados[1]**2 == lados[2]**2:
        return True
    else:
        return False


# Função para ler números naturais
def ler_numero_natural(mensagem):
    while True:
        try:
            numero = int(input(mensagem))
            if numero <= 0:
                raise ValueError
            return numero
        except ValueError:
            print("Por favor, insira um número natural válido.")


def main():
    print("Digite os comprimentos dos lados do triângulo: ")
    a = ler_numero_natural("Lado 1: ")
    b = ler_numero_natural("Lado 2: ")
    c = ler_numero_natural("Lado 3: ")

    if verifica_triangulo_retangulo(a, b, c):
        print("Os lados formam um triângulo retângulo.")
    else:
        print("Os lados não formam um triângulo retângulo.")


if __name__ == "__main__":
    main()
