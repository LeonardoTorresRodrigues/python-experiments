# Fatiando listas
print("Fatiando listas")
primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
          31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

print(primos[1:2])
print(primos[2:7])
print(primos[0:12])
print(primos[12:25])
print(primos[:12])
print(primos[12:])

final = primos[12:]

print(primos)
print(final)

# Clonando listas
print("Clonando listas")
lista1 = ["vermelho", "verde", "azul"]
lista2 = lista1[:]

lista2[0] = "rosa"
print(lista1)
print(lista2)

# Pertinência a uma lista
print("Pertinência a uma lista")
print("rosa" in lista1)
print("rosa" in lista2)

if "rosa" in lista1:
    print("Está na lista 1")

if "rosa" in lista2:
    print("Está na lista 2")

# Concatenação de listas
print("Concatenação de listas")
print([1, 2] + [3, 4])
print([4, 3, 4, 5, 2] + [2, 4, 2, 4, 5, 6])

a = [1, 2, 3]
b = [4, 5, 6]

print(a + b)
print(b + a)
print(b + a + b)

# Repetição de listas
print("Repetições de listas")
a_triplicado = a * 3
b_quintuplicado = b * 5
print(a_triplicado)
print(b_quintuplicado)

# Remoção em listas
print("Remoção em listas")
del a[1]
print(a)

lista = ["a", "b", "c", "d", "e", "f"]
del lista[1:5]
print(lista)
