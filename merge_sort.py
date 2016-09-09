# Aquí es donde debe de ir su implementación del merge sort

# Esta función recibe una lista y regresa una copia ordenada
def merge_Sort(l):
	if len(l) == 0 or len(l) == 1 :
		return l[:]
	i = 0
	j = len(l)
	mitad = int(j/2)
	first_part = []
	scond_part = []
	x = 0
	while i < mitad :
		first_part.append(l[i])
		i += 1

	while mitad < j :
		scond_part.append(l[mitad])
		mitad += 1

	return mezclaMerge( merge_Sort(first_part),merge_Sort(scond_part))




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
