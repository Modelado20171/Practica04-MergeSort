# Aquí es donde debe de ir su implementación del merge sort
# Esta función recibe una lista y regresa una copia ordenada
def merge_sort(lista):
	if len(lista) == 0 or len(lista) == 1:
		return lista
	else:
		mitad = int(len(lista)/2)
		mitadA = merge_sort(lista[:mitad])
		mitadB = merge_sort(lista[mitad:])
		return merge(mitadA,mitadB)
#Esta función fuciona una lista ordenada
def merge(mitadA,mitadB):
    merged = []
    while len(mitadA) != 0 and len(mitadB) != 0:
        if mitadA[0] < mitadB[0]:
            merged.append(mitadA[0])
            mitadA.remove(mitadA[0])
        else:
            merged.append(mitadB[0])
            mitadB.remove(mitadB[0])
    if len(mitadA) == 0:
        merged += mitadB
    else:
        merged += mitadA
    return merged


   
    

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