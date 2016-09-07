# Aquí es donde debe de ir su implementación del merge sort

# Esta función recibe una lista y regresa una copia ordenada
def merge_sort(lista):
	if len(lista) == 1:
		return lista
	lista_izquierda = lista[:len(lista)//2]
	lista_derecha = lista[len(lista)//2:]
	return merge(merge_sort(lista_izquierda),merge_sort(lista_derecha))

def merge(lista1,lista2):
	lista_ordenada = list()
	indice_izq,indice_der = 0, 0
	while indice_izq < len(lista1) and indice_der < len(lista2):
		if lista1[indice_izq] < lista2[indice_der]:
			lista_ordenada.append(lista1[indice_izq])
			indice_izq += 1
		else:
			lista_ordenada.append(lista2[indice_der])
			indice_der += 1
	lista_ordenada += lista1[indice_izq:]
	lista_ordenada += lista2[indice_der:]
	return lista_ordenada


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
