def multiplos_de_i_ou_j(n, i, j):
    numeros = []
    numero = 0
    while len(numeros) < n:
        if numero % i == 0 or numero % j == 0:
            numeros.append(numero)
        numero += 1
    return numeros


n = int(input("Digite o valor de n: "))
i = int(input("Digite o valor de i: "))
j = int(input("Digite o valor de j: "))

resultado = multiplos_de_i_ou_j(n, i, j)
print(" ".join(map(str, resultado)))
