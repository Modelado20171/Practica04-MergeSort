# Aquí es donde debe de ir su implementación del merge sort

# Esta función recibe una lista y regresa una copia ordenada
def merge_sort(lista):
  pass

def merge(l1, l2):
    l = []
    l1_index, l2_index = 0, 0

    while l1_index < len(l1) and l2_index < len(l2):
        if l1[l1_index] < l2[l2_index]:
            l.append(l1[l1_index])
            l1_index += 1
        else:
            l.append(l2[l2_index])
            l2_index += 1

    if l1_index == len(l1):
        l.extend(l2[l2_index:])
    elif l2_index == len(l2):
        l.extend(l1[l1_index:])
    
    return l

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
