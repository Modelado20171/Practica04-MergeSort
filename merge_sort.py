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
	a = beg
	b = mid
	listaTmp = listaO[:]	#hacemos una lista temporal para hacerlo mas facil
	for c in range(beg, end):
		if a >= mid:	
			listaO[c] = listaTmp[b]
			b += 1;
		elif b >= end:
			listaO[c] = listaTmp[a]
			a += 1;
		elif listaTmp[b] < listaTmp[a]:
			listaO[c] = listaTmp[b]
			b += 1;
		else:
			listaO[c] = listaTmp[a]
			a += 1;

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
