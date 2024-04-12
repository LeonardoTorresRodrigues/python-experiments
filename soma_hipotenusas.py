import math


def é_hipotenusa(c):
    for a in range(1, c):
        for b in range(1, c):
            if a**2 + b**2 == c**2:
                return True
    return False


def soma_hipotenusas(n):
    soma = 0
    for c in range(1, n + 1):
        if é_hipotenusa(c):
            soma += c
    return soma


n = int(input("Digite um número inteiro: "))
resultado = soma_hipotenusas(n)
print(resultado)
