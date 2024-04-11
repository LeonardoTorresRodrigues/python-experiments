largura = int(input("Digite a largura: "))
altura = int(input("Digite a altura: "))
y = altura
while altura > 0:
    if altura == y or altura == 1:
        print("#"*largura, end="")
    if altura != y and altura > 1:
        print("#" + " " * (largura - 2) + "#", end="")
    if altura > 1:
        print()
    altura -= 1
