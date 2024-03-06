ano = int(input("Insira um ano: "))

is_bissexto = (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)

print(is_bissexto)
