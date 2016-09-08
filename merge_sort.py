# Aquí es donde debe de ir su implementación del merge sort

# Esta función recibe una lista y regresa una copia ordenada
def merge_sort(lista):
    n = len(lista)
    if(n <= 1):
        return lista
    izq = merge_sort(lista[:(n//2)])
    der = merge_sort(lista[(n//2):])
    return merge(izq, der)

#Esta función recibe dos listas, las junta y regresa una nueva lista ordenada
def merge(izq, der):
    ordenada = []
    while len(izq) != 0 and len(der) != 0:
        if izq[0] < der[0]:
            ordenada.append(izq.pop(0))
        else:
            ordenada.append(der.pop(0))
    if len(izq) == 0:
        ordenada += der
    else:
        ordenada += izq
    return ordenada

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
