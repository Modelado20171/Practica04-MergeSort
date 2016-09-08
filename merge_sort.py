# Aquí es donde debe de ir su implementación del merge sort
def merge(l1, l2):
    if l1 == []:
        return l2
    if l2 == []:
        return l1
    if l1[0] < l2[0]:
        return [l1[0]]+merge(l1[1:], l2)
    return [l2[0]]+merge(l1, l2[1:])

# Esta función recibe una lista y regresa una copia ordenada
def merge_sort(lista):
    if lista == [] or len(lista) == 1:
        return lista
    izq = lista[:int(len(lista)/2)]
    der = lista[int(len(lista)/2):]
    return merge(merge_sort(izq), merge_sort(der))


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
