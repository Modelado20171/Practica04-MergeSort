# Aquí es donde debe de ir su implementación del merge sort

# Esta función recibe una lista y regresa una copia ordenada
def merge_sort(lista):
	longitud = len(lista)
	if longitud <= 1:
		return lista
	mitad = len(lista) // 2
	izquierda = merge_sort(lista[:mitad])
	derecha = merge_sort(lista[mitad:])
	return merge(izquierda, derecha)
    
def merge(izquierda, derecha):
    lista_ordenada = [] 
    i = 0
    j = 0
    longitud_izquierda = len(izquierda) 
    longitud_derecha = len(derecha) 
  
    while(i < longitud_izquierda or j < longitud_derecha): 
        if(i >= longitud_izquierda): 
            lista_ordenada.append(derecha[j]) 
            j = j + 1
        elif(j >= longitud_derecha): 
            lista_ordenada.append(izquierda[i]) 
            i = i + 1
        elif(izquierda[i] < derecha[j]): 
            lista_ordenada.append(izquierda[i]) 
            i = i + 1
        else: 
            lista_ordenada.append(derecha[j]) 
            j = j + 1
    return lista_ordenada 

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
