# Versão 1
tamanho = int(input("Digite o tamanho da sequência de números: "))
i = 0
numeros = 0
pares = 0
impares = 0

while i < tamanho:
    numeros = int(input("Digite os números para serem contados: "))
    if numeros % 2 == 0:
        pares += 1
    else:
        impares += 1
    i += 1
print(pares, "pares", impares, "impares")


# Versão 2
n = int(input("Digite o tam da seq: "))  # atribuição multipla

cont = conta_par = conta_impar = 0
while cont < n:
    num = int(input("Digite um num da seq: "))
    cont = cont + 1
    if num % 2 == 0:  # se num é múltiplo de 2, ou seja, é par
        conta_par = conta_par + 1
    else:
        conta_impar = conta_impar + 1

print(conta_par,   "numeros pares")
print(conta_impar, "numeros impares")


# Versão 3
n = int(input("Digite o tam da seq: "))  # atribuição multipla

conta_par = 0
cont = 0
while cont < n:
    num = int(input("Digite um num da seq: "))
    cont = cont + 1
    if num % 2 == 0:  # se num é múltiplo de 2, ou seja, é par
        conta_par = conta_par + 1

print(conta_par,   "numeros pares")
print(n - conta_par, "numeros impares")
