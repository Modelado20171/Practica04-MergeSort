##*-* encoding: utf-8 *-*

#Rubio Lezama Eduardo	
# Aquí es donde debe de ir su implementación del merge sort
def mezcla(lista1,lista2):
	nueva = [] # Donde se guardara la lista que mezcla dos listas
	while ((len(lista1) > 0) and (len(lista2)>0)):
		
		if (lista1[0] > lista2[0]):
			nueva.append (lista2.pop(0))
		
		else:
			nueva.append (lista1.pop(0))

	if (len(lista1) == 0 and len(lista2) > 0):
			while(len(lista2) > 0):
				nueva.append(lista2.pop(0))

	elif (len(lista2) == 0 and len(lista1) > 0):
			while(len(lista1) > 0):
				nueva.append(lista1.pop(0))		
	return nueva	
# Esta función recibe una lista y regresa una copia ordenada
def merge_sort(lista):

  	if (len(lista) <= 1):
  		return lista
   	
	else:

   		mitad = int (len(lista)/2)
   	  			
   		lista1 = merge_sort(lista[:mitad])
   		lista2 = merge_sort(lista[mitad:])
   		return mezcla(lista1,lista2)
	
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
