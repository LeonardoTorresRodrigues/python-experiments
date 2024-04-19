a = "banana"
b = "banana"
c = "maçã"
# Strings são imutáveis em Python

print(a is b)  # aponta para o mesmo espaço em memória
print(a is c)  # aponta para espaços diferentes em memória

d = [81, 82, 83]
e = [81, 82, 83]

# aponta para duas listas diferentes, por tanto, estão em espaços diferentes em memória
print(d is e)
print(d == e)  # o conteúdo das listas são iguais


origilists = [45, 76, 34, 55]
newlist = [origilists] * 3  # aponta para [origilist]
origilists[1] = 99  # altera também no [newlist]
