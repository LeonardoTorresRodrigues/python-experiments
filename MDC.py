def mdc_euclides(a, b):
    while b != 0:
        a, b = b, a % b
    return a


num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
print(f'O MDC de {num1} e {num2} é: {mdc_euclides(num1, num2)}')
