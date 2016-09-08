# Aqui es donde debe de ir su implementacion del merge sort

# Esta funcion recibe una lista y regresa una copia ordenada
def merge_sort(lista):
	if len(lista)==1:
		return lista
	else:
		#Partiendo lista en 2 (o al menos con la parte entera :l)
		l_iz= lista[0 : (len(lista))//2]
		l_dr= lista[(len(lista))//2 : len(lista)]
		#llamamos el metodo junta al tener las sublistas, subdividendo estas mismas
		return junta(merge_sort(l_iz),merge_sort(l_dr))
		
def junta(lista_i, lista_d):
	tmp=[]
	#en cada caso dentro de while usamos pop(), esto saca el ultimo elemento de la lista
	while len(lista_i)>0 or len(lista_d)>0:		
		#Si la lista izquierda es vacia, agrega de la derecha
		if len(lista_i)==0: 
			tmp.append(lista_d.pop())
			
		#Si no, entonces si la lista derecha esta vacia 
		#o el ultimo elemento de la lista izquierda es mayor que el ultimo de la derecha agrega el de la izquierda,
		#asi podemos hacer el reverse para tenerla ordenada
		elif len(lista_d)==0 or lista_i[-1] > lista_d[-1]: 
			tmp.append(lista_i.pop())			
		
		else:
		#Si no, agrega de la derecha
			tmp.append(lista_d.pop())	
	
	#ordenando de izquierda a derecha
	tmp.reverse()	
	return tmp


# Tienes estictamente prohibido borrar lineas despues de este punto
lista1 = [1,2,3,4,5,6]
lista2 = [6,5,4,3,2,1]
lista3 = [5,3,8,1,3,8,7,8,2,1,6,8,1,3,8]

listaOrdenada1 = merge_sort(lista1)
listaOrdenada2 = merge_sort(lista2)
listaOrdenada3 = merge_sort(lista3)

print(listaOrdenada1)
print(listaOrdenada2)
print(listaOrdenada3)
