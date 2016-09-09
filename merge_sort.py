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

def mezclaMerge(l1,l2):
	nueva = []
	i = 0
	j = 0

	while i < len(l1) and j < len(l2):
		if l1[i] < l2[j] :
			nueva.append(l1[i])
			i += 1
		else:
			nueva.append(l2[j])
			j += 1

	while j < len(l2) :
		nueva.append(l2[j])
		j += 1

	while i < len(l1) :
		nueva.append(l1[i])
		i += 1

	return nueva


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
