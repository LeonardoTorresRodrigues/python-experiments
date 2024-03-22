def eh_triangular(n):
    # Inicializa o produto e o contador
    produto = 1
    contador = 1

    # Itera enquanto o produto for menor que ou igual a 'n'
    while produto < n:
        # Atualiza o produto multiplicando pelo próximo número
        contador += 1
        produto *= contador

    # Verifica se o produto é igaul a 'n'
    return produto == n


numero = int(input("Digite um número inteiro positivo: "))
if eh_triangular(numero):
    print(numero, "é um número trinagular :D")
else:
    print(numero, "não é um número triangular D:")
