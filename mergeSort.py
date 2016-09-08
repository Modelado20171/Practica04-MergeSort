# Aquí es donde debe de ir su implementación del merge sort

# Esta función recibe una lista y regresa una copia ordenada
def unir(uno, dos):
    ordenada = list()
    i = 0
    j = 0
    while i < len(uno) and j < len(dos):
        if (uno[i] - dos[j]) < 0:
            ordenada.append(uno[i])
            i += 1
        else:
            ordenada.append(dos[j])
            j += 1

    while j < len(dos):
        ordenada.append(dos[j])
        j += 1

    while i < len(uno):
        ordenada.append(uno[i])
        i += 1
    return ordenada

def merge_sort(lista):
    if len(lista) <= 1:
        return lista.copy()
    primeros = []
    ultimos = []
    i = 0
    while(i < len(lista)/2):
        primeros.append(lista[i])
        i += 1
    h = int(len(lista)/2)
    while h < len(lista):
        ultimos.append(lista[h])
        h += 1
    primeros = merge_sort(primeros)
    ultimos = merge_sort(ultimos)
    return unir(primeros,ultimos)

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
