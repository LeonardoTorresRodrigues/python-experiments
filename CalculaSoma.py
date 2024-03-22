def calcular_soma():
    soma = 0
    while True:
        num = int(input("Digite um número (0 para sair): "))
        if num == 0:
            break
        soma += num
    return soma


resultado = calcular_soma()
print("A soma dos números é: ", resultado)
