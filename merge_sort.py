def merge_sort(lista) :
	if len(lista) == 1 :
		return lista[:]
	n = len(lista) // 2
	lista1 = lista[:n]
	lista2 = lista[n:]
	return merge(merge_sort(lista1), merge_sort(lista2))	

lista1 = [1,2,3,4,5,6]
lista2 = [6,5,4,3,2,1]
lista3 = [5,3,8,1,3,8,7,8,2,1,6,8,1,3,8]

listaOrdenada1 = merge_sort(lista1)
listaOrdenada2 = merge_sort(lista2)
listaOrdenada3 = merge_sort(lista3)

print(listaOrdenada1)
print(listaOrdenada2)
print(listaOrdenada3)