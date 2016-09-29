
def ordena(lista1, lista2):
	""" Nos ordena la lista en dos sublistas 
    	  Recibe lista1 y lista2 las cuales seran mezcladas.
      	 Devuelve: Una lista con la union de la lista1 y lista 2"""	
	posicion1 = 0 # Posicion o indice de la lista. 
	posicion2 = 0 # Posicion o indice de la lista. 
	guarda = [] #Auxiliar que guarda  el resultado de las dos sublistas. 
	while(posicion1 < len(lista1) and posicion2 < len(lista2)):
		if(lista1[posicion1] < lista2[posicion2]):
			guarda.append(lista1[posicion1]) #Se guarda mayores y menores en las listas (de una sublista). 
			posicion1 += 1
		else:
			guarda.append(lista2[posicion2]) #Se guarda mayores y menores en las listas (de una sublista).
			posicion2 +=1
		if(posicion1 == len(lista1)):# Las sublistas ahora se convierten en una lista de guarda. 
			guarda.extend(lista2[posicion2:])
		else:
			if(posicion2 == len(lista2)):# Las sublistas ahora se convierten en una lista de guarda.
				guarda.extend(lista1[posicion1:])
	return guarda
def merge_sort(lista):
	"""  Metodo auxiliar que nos devuelve una lista y verifica su tamanio 
    	  Recibe lista para ordenar.
      	 Devuelve: lista ordenada"""	
	if len(lista) < 2 :# Si la lista es menor a 1, no hay nada que ordenar.  
		return lista 
	else:
		mitad = len(lista) // 2 
		temp = [] # Lista auxiliar. 
		temp = ordena(merge_sort(lista[:mitad]), merge_sort(lista[mitad:])) # Separa la lista original en mitades.   
		return temp
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
