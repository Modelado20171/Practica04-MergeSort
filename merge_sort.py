# Aquí es donde debe de ir su implementación del merge sort

# Esta función recibe una lista y regresa una copia ordenada
def merge_sort(lista):
    if len(lista) < 2:
        return lista
    res = []
    mid = int(len(lista)/2)
    a1 = merge_sort(lista[:mid])
    a2 = merge_sort(lista[mid:])
    while (len(a1) > 0) and (len(a2) > 0):
        if a1[0] < a2[0]:
            res.append(a1.pop(0))
        else:
            res.append(a2.pop(0))
    res += a1
    res += a2
    return res



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
