# Esta función recibe una lista y regresa una copia ordenada
def merge_sort(lista):
	n = len(lista)
	listaOrd = list(lista)
	i = 1
	while i < n:	#separamos la lista en sublistas
		j = 0
		while j < n:	#las unimos
			merge(listaOrd, j, min(j+i,n), min(j+i*2,n))
			j += 2*i
		i *= 2
	return listaOrd
	
# funcion merge que combina dos de los sub 'arreglos'
def merge(listaO, beg, mid, end):
	pass

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
