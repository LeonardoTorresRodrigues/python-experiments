largura = int(input("Digite a largura: "))
altura = int(input("Digite a altura: "))
x = largura
while largura > 0:
    print("#", end=(""))
    largura -= 1
    if largura == 0 and altura > 1:
        print()
        altura -= 1
        largura = x
