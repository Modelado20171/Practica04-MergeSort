# Aquí es donde debe de ir su implementación del merge sort

# Esta función recibe una lista y regresa una copia ordenada
def merge_sort(lista):
    if(len(lista) == 1):
        return lista.copy()
    l1, l2, counter= list(), list(), 0
    while counter < len(lista):
        if counter % 2 == 0:
            l1.append(lista[counter])
        else:
            l2.append(lista[counter])
        counter+= 1
    return merge(merge_sort(l1), merge_sort(l2))

def merge(lista1, lista2):
    lista= list()
    counter1, counter2= 0, 0
    while counter1 < len(lista1) and counter2 < len(lista2):
        if lista1[counter1] < lista2[counter2]:
            lista.append(lista1[counter1])
            counter1+= 1
        else:
            lista.append(lista2[counter2])
            counter2+= 1
    while counter2 < len(lista2):
        lista.append(lista2[counter2])
        counter2+= 1
    while counter1 < len(lista1):
        lista.append(lista1[counter1])
        counter1+= 1
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
