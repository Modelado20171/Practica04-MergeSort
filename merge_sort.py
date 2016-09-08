#!/usr/bin/python

#-*- coding: utf-8 -*-

# Aqui es donde debe de ir su implementacion del merge sort

# Esta funcion recibe una lista y regresa una copia ordenada
def merge_sort(lista):
	if len(lista) == 1:
		return lista;
	m = len(lista)//2
	left = lista[:m]
	right = lista[m:]
	left = merge_sort(left)
	right = merge_sort(right)
	return list(merge(left, right))

def merge(left, right):
    result = []
    i ,j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result
# Tienes estrictamente prohibido borrar lineas despues de este punto
lista1 = [1,2,3,4,5,6]
lista2 = [6,5,4,3,2,1]
lista3 = [5,3,8,1,3,8,7,8,2,1,6,8,1,3,8]

listaOrdenada1 = merge_sort(lista1)
listaOrdenada2 = merge_sort(lista2)
listaOrdenada3 = merge_sort(lista3)

print(listaOrdenada1)
print(listaOrdenada2)
print(listaOrdenada3)
