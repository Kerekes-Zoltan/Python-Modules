import copy

lista_originala = [1, 2, 3, 4, 5]
print("Original list: ", lista_originala)

copie_lista = copy.copy(lista_originala)
print("Copied list: ", copie_lista)

lista_originala[1][0] = 24
print("Change the value of element in list: ", lista_originala)