import cmath


def calcular_raizes(a, b, c):
    # Calcula o delta
    delta = b**2 - 4*a*c

    # Verifica o valor do delta
    if delta < 0:
        print("Esta equação não possui raízes reais.")
    elif delta == 0:
        raiz = -b / (2*a)
        print(f"A raiz desta equação é: {raiz}")
    else:
        raiz1 = (-b + cmath.sqrt(delta)) / (2*a)
        raiz2 = (-b - cmath.sqrt(delta)) / (2*a)
        print(f"As raízes da equação são: {raiz1} e {raiz2}")


a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

calcular_raizes(a, b, c)
