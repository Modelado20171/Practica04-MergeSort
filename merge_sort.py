# Aquí es donde debe de ir su implementación del merge sort

# Esta función recibe una lista y regresa una copia ordenada
def merge_sort(lista):
    pass

def merge(listaIzquierda, listaDerecha):
	i=0
	j=0
	lonIzq=len(listaIzquierda)
	lonDer= len(listaDerecha)
	resultado=[]

	while i<lonIzq and j< lonDer:
		if listaIzquierda[i]<listaDerecha[j]:
			resultado.append(listaIzquierda[i])
			i=i+1
		else:
			resultado.append(listaDerecha[j])
			j=j+1
	while i<lonIzq:
		resultado.append(listaIzquierda[i])
		i=i+1
	while j<lonDer:
		resultado.append(listaDerecha[j])
		j=j+1
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
