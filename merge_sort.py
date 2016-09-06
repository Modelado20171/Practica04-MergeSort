def add_missing(merged_list, missed_list, i) :
	for j in range(i, len(missed_list)) :
		merged_list.append(missed_list[j])
	return merged_list

def merge(lista1, lista2) :
	merged_list = []
	i, j = 0, 0
	while i < len(lista1) and j < len(lista2) :
		if lista1[i] < lista2[j] :
			merged_list.append(lista1[i])
			i += 1
		else :
			merged_list.append(lista2[j])
			j += 1
	if i == len(lista1) :
		return add_missing(merged_list, lista2, j)
	else :
		return add_missing(merged_list, lista1, i)

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
