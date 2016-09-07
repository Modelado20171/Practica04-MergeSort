# Aquí es donde debe de ir su implementación del merge sort

# Esta función recibe una lista y regresa una copia ordenada
def merge_sort(lista):
	pass

# Definimos la funcion para concatenar las listas ya ordenadas.
def merge(ListIzq, ListDer):
	resultado = []
	while(len(ListIzq) > 0 and len(ListDer) > 0):
		if(ListIzq[0] <= ListDer[0]):
			resultado.append(ListIzq[0])
			ListIzq = ListIzq[1:]
		else:
			resultado.append(ListDer[0])
			ListDer = ListDer[1:]
	if(len(ListIzq) > 0):
		resultado.extend(ListIzq[0:])
	if(len(ListDer) > 0):
		resultado.extend(ListDer[0:])
	return resultado

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
