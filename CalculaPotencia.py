def calcular_potencia(n, k):
    return n ** k


n = int(input("Digite o valor de n: "))
k = int(input("Digite o valor de k: "))

resultado = calcular_potencia(n, k)
print("O resultado de", n, "elevado a", k, "é:", resultado)
