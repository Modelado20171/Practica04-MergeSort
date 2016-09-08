# Aquí es donde debe de ir su implementación del merge sort

# Esta función recibe una lista y regresa una copia ordenada
def merge_sort(lista):
    mitadI = list()
    mitadD = list()
    if len(lista) == 1 or len(lista) == 0:
        return lista
    else:
        mitad = len(lista)//2
        for x in range(0,mitad):
            mitadI.append(lista[x])
        for y in range(mitad,len(lista)):
            mitadD.append(lista[y])

        return merge(merge_sort(mitadI), merge_sort(mitadD))


# Tienes estríctamente prohibido borrar líneas después de este punto
lista1 = [1,2,3,4,5,6]
lista2 = [6,5,4,3,2,1]
lista3 = [5,3,8,1,3,8,7,8,2,1,6,8,1,3,8]

listaOrdenada1 = merge_sort(lista1)
listaOrdenada2 = merge_sort(lista2)
listaOrdenada3 = merge_sort(lista3)

print(listaOrdenada1)
print(listaOrdenada2)
print(listaOrdenada3)
