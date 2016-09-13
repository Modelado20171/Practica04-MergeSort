# Aquí es donde debe de ir su implementación del merge sort
def mezcla(lista1, lista2):
	aux = []
	indice1 = 0
	indice2 = 0
	while(indice1 < len(lista1) and indice2 < len(lista2)):
		if(lista1[indice1] < lista2[indice2]):
			aux.append(lista1[indice1])
			indice1 += 1
		else: 
			aux.append(lista2[indice2])
			indice2 += 1

		if indice1 == len(lista1):
			aux.extend(lista2[indice2:])
    	elif indice2 == len(lista2):
    		aux.extend(lista1[indice1:])
        return aux

# Esta función recibe una lista y regresa una copia ordenada
def merge_sort(lista):
  if len(lista) < 2:
    return lista
half = len(lista) // 2
  return mezcla(merge_sort(lista[:half]), merge_sort(lista[half:]))


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
