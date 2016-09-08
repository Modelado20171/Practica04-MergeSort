#!/usr/bin/env python

'''Algoritmo de ordenamiento MergeSort.
Divide en subarreglos (sublistas) de cerca de la mitad del tamaño del que 
es pasado como parámetro de forma recursiva. Posteriormente,
en cada llamada recursiva se juntan las dos partes del arreglo anterior, fijándose
cuál es el menor elemento en cada caso; si una lista se recorrió primero, la otra es agregada al
final.
'''

__author__ = "Miguel Concha Vázquez"
__version__ = "1.0.1"
__email__ = "mconcha@ciencias.unam.mx"
__status__ = "Done"

# Aquí es donde debe de ir su implementación del merge sort

def merge(lista_izq, lista_der):
	gran_lista = list() #Lista que contendrá las dos mitades ya ordenadas.
	iterador_izquierda, iterador_derecha = 0, 0 #Variables para recorrer las entradas de cada lista.
	#Se van iterando ambas listas y se comparan las entradas; la menor de ellas se añade a la lista.
	while iterador_izquierda < len(lista_izq) and iterador_derecha < len(lista_der):
		if lista_izq[iterador_izquierda] <= lista_der[iterador_derecha]:
			gran_lista.append(lista_izq[iterador_izquierda])
			iterador_izquierda += 1
		else: 
			gran_lista.append(lista_der[iterador_derecha])
			iterador_derecha += 1
	#Se agrega toda la lista restante si una terminó de recorrerse primero. Por hipótesis, esa parte de la lista ya está ordenada.
	if iterador_izquierda < len(lista_izq):
		return gran_lista + lista_izq[iterador_izquierda:]
	if iterador_derecha < len(lista_der):
		return gran_lista + lista_izq[iterador_derecha:]
	return gran_lista #Regresando la lista ya ordenada que contempla ambas sublistas originales.

# Esta función recibe una lista y regresa una copia ordenada
def merge_sort(lista):
	if len(lista) <= 1: #Caso Base: Cuando la longitud de la lista es 0 o 1, ya está ordenada.
		return lista
	izq, der = lista[:len(lista) // 2], lista[len(lista) // 2:] #Se divide a la lista en dos partes, aproximádamente por la mitas de ésta.
	izq, der = merge_sort(izq), merge_sort(der) #Llamada Recursiva: se hace lo mismo con cada submitad.
	return merge(izq, der) #Finalmente, se van ordenando y mezclando las dos sublistas y el resultado va siendo regresado en cada llamada.

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
