import copy

lista_originala = [1, [5, 2, 3, 5]]
print("Original list: ", lista_originala)

copie_lista = copy.deepcopy(lista_originala)
print("Deepcopy of list: ", copie_lista)

lista_originala[1][0] = 10
print("\nChange the value of an element of the original list: ", lista_originala)