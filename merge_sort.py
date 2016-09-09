# Aquí es donde debe de ir su implementación del merge sort

# Esta función recibe una lista y regresa una copia ordenada
def merge_sort(lista):
    longitud = len(lista)

    if longitud < 2:
        return lista

    medio = math.floor(longitud/2)

    lista_izq = merge_Sort(lista[:medio])
    lista_der = merge_Sort(lista[medio:])

    return mezcla(lista_izq, lista_der)

#funcion auxiliar que fuciona dos listas
def mezcla(lista_izq, lista_der):
    i, j = 0, 0
    lista = []

    while (i < len(lista_izq) and j < len(lista_der)):
        if lista_izq[i] < lista_der[j]:
            lista.append(lista_izq[i])
            i += 1
        else:
            lista.append(lista_der[j])
            j += 1

    lista += lista_izq[i:]
    lista += lista_der[j:]

    return lista


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
