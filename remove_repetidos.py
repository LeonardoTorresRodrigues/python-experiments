def remove_repetidos(lista):
    lista_ordenada = sorted(set(lista))
    return lista_ordenada


lista = [1, 2, 3, 3, 3, 4, 5, 0, 7, 6, 6, 6, 9, 8]
lista_sem_repetidos = remove_repetidos(lista)
print(lista_sem_repetidos)
