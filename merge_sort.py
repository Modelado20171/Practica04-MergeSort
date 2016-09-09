# Aquí es donde debe de ir su implementación del merge sort

# Esta función recibe una lista y regresa una copia ordenada
def merge_sort(lista):
    result = []
    if len(lista) < 2:
    	return lista
    mitad = int(len(lista)/2)
    l1 = merge_sort(lista[:mitad])
    l2 = merge_sort(lista[mitad:])

    i = 0
    j = 0

    while i < len(l1) and j < len(l2):
    	if l1[i] > l2[j]:
    		result.append(l2[j])
    		j+=1
    	else:
    		result.append(l1[i])
    		i+=1
    #Manda todos los elementos restantes de la lista no vacía a result, no necesita verificar cual es la lista vacía.
    result+=l1[i:]
    result+=l2[j:]
    return result


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
