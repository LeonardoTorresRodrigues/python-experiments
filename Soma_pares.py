# Versão 1
tamanho = int(input("Digite o tamanho da sequência de números: "))
i = 0
numeros = 0
somador = 0

while i < tamanho:
    numeros = int(input("Digite os números a serem somados: "))
    if numeros % 2 == 0:
        somador = numeros + somador
    i += 1
print("A soma dos números pares é: ", somador)
