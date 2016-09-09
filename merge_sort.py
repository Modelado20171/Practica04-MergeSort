# Aqui es donde debe de ir su implementacion del merge sort

# Esta funcion recibe una lista y regresa una copia ordenada
def merge_sort (lista):
	longitudLista = len(lista)
	lista1 = list()
	lista2 = list()
	mitadLista = int(longitudLista/2)
	if (longitudLista < 2):
		return lista
	for i in range(0,mitadLista):
  		lista1.append(lista[i])
  	for j in range (mitadLista,len(lista)):
  		lista2.append(lista[j])
  	lista1 = merge_sort(lista1)
  	lista2 = merge_sort(lista2)
  	return merge_sort2(lista1,lista2)

def merge_sort2 (lista1,lista2):
	lista = list()
	i = 0
	j = 0
	while i < len(lista1) and j < len(lista2):
		if lista1[i] < lista2[j]:
			lista.append(lista1[i])
			i += 1
		else:
			lista.append(lista2[j])
			j += 1
	lista += lista1[i:]
	lista += lista2[j:]
	return lista
  	

	

#if __name__ == '__main__':
#	aux = merge_sort([10,9,8,7,6,5,4,3,2,1,15,45,32])
#	print aux
  		

#Tienes estrictamente prohibido borrar lineas despues de este punto

lista1 = [1,2,3,4,5,6]
lista2 = [6,5,4,3,2,1]
lista3 = [5,3,8,1,3,8,7,8,2,1,6,8,1,3,8]

listaOrdenada1 = merge_sort(lista1)
listaOrdenada2 = merge_sort(lista2)
listaOrdenada3 = merge_sort(lista3)

print(listaOrdenada1)
print(listaOrdenada2)
print(listaOrdenada3)


 #Esta funcion recibe una lista y regresa una copia ordenada
 

