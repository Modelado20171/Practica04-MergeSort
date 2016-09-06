# Aquí es donde debe de ir su implementación del merge sort

# Esta función recibe una lista y regresa una copia ordenada
def merge_sort(lista):
	return divide_lista(lista)

#Método que se encarga de dividir una lista en dos, hasta llegar a listas de tamaño uno (ya ordenadas) y dejándolas listas para aplicar la función merge.
def divide_lista(lista):
	if len(lista) == 1:
		return lista
	else:
		tam_listas_divididas= len(lista)//2 #Las vamos diviendo entre dos (usando función piso si son de tamaño impar) hasta llegar a listas de tamaño 1.                                                                                                                                                                                              HOLA 
		nueva_lista1= list()
		nueva_lista2= list()
		for i in range(len(lista)):
			if i < tam_listas_divididas:
				nueva_lista1.append(lista[i])   #Izquierda.
			else:
				nueva_lista2.append(lista[i])	#Derecha
				
		izquierda= divide_lista(nueva_lista1)
		derecha= divide_lista(nueva_lista2)

		return merge(izquierda, derecha)

#Método que junta las listas ordenadas de tamaño uno, comparándolas y agregándolas en una nueva lista de forma ordenada ascendiente.
def merge(listaIzq, listaDer):
	listaOrd= list()
	
	while listaIzq and listaDer:
		if listaIzq[0] <= listaDer[0]:
			listaOrd.append(listaIzq[0])
			del listaIzq[0]
		else:
			listaOrd.append(listaDer[0])
			del listaDer[0]
			
	while listaIzq:
		listaOrd.append(listaIzq[0])
		del listaIzq[0]
	while listaDer:
		listaOrd.append(listaDer[0])
		del listaDer[0]
		
	return listaOrd
	
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
