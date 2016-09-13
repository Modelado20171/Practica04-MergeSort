# Aquí es donde debe de ir su implementación del merge sort

# Esta función recibe una lista y regresa una copia ordenada
def merge_sort(lista):
	if len(lista) < 2 :
		return lista #Si la lista tiene menos de dos elementos, regresa la lista
	else:
		#Dividimos la lista
		mitad = len(lista) // 2
		#variable auxiliar para guardar 
		aux = []
		aux = divide_lista(merge_sort(lista[:mitad]), merge_sort(lista[mitad:])) 
		return aux
#Creamos una funcion para dividir la lista
def divide_lista(lista1, lista2):
	lisAyuda = []
	#creamos variables para movernos en las listas
	ind1 = 0
	ind2 = 0
	#iteramos en las listas
	while(ind1 < len(lista1) and ind2 < len(lista2)):
		#Hacemos la comparacion entre los indices
		if(lista1[ind1] < lista2[ind2]):
			#agregamos el indice1 de la lista1 a la lista auxiliar
			lisAyuda.append(lista1[ind1])
			ind1 += 1
		else:
			#agregamos el indice2 a la lista auxiliar
			lisAyuda.append(lista2[ind2])
			ind2 +=1
		#verificamos 
		if(ind1 == len(lista1)):
			#con extend añade el contenido de la lista2 a la lista auxiliar
			lisAyuda.extend(lista2[ind2:])
		else:
			if(ind2 == len(lista2)):
				#añade el contenido de la lista1 a la lista auxiliar
				lisAyuda.extend(lista1[ind1:])
	return lisAyuda

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