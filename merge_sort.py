# Aquí es donde debe de ir su implementación del merge sort
 
# Esta función recibe una lista y regresa una copia ordenada
def merge_sort(lista):
     
    size = len(lista)
 
    # Cláusula de escape: Si la lista es de longitud 1 o 0 
    if size <= 1:
        return lista
 
    # Almacena el elemento medio de la lista
    half = len(lista) // 2
 
    # Separamos a la lista en 2 partes: 
    # Su sección izquierda y derecha a partir de la mitad.
 
    # La sección izquierda, desde el primer elemento hasta antes
    # del elemento "h"
    left = merge_sort(lista[:half])
 
    # La sección derecha, desde el elemento "h" hasta el último
    right = merge_sort(lista[half:])
 
    # Fusiona ambas listas en una
    return merge(left, right)
     
# Esta función recibe 2 listas y las ordena
def merge(left, right):
 
    # Inicializa una lista donde se almacenarán los elementos
    # ordenados de la original.
    l_ord = [] 
 
 	# Índices de posición para las listas izquierda y derecha
    i, j = (0,)*2
 
    # Tamaño de la lista izquierda
    l_size = len(left) 
 
    # Tamaño de la lista derecha
    r_size = len(right) 
   
    # Se itera hasta que algun índice rebase el tamaño
    # de su lista correspondiente
    while(i < l_size or j < r_size): 

    	# Si el índice izquierdo rebasa la longitud de su lista
        if(i >= l_size): 

        	# Se añade a la lista ordenada el elemento j-ésimo
        	# de la lista derecha
            l_ord.append(right[j]); j += 1

        # Si el índice derecho rebasa la longitud de su lista
        elif(j >= r_size): 

        	# Se añade a la lista ordenada el elemento i-ésimo
        	# de la lista izquierda
            l_ord.append(left[i]); i += 1

        # Si el elemento i-ésimo en la lista izquierda es mayor
        # al elemento j-ésimo en la lista derecha
        elif(left[i] < right[j]): 

        	# Se añade a la lista ordenada el elemento i-ésimo
        	# de la lista izquierda
            l_ord.append(left[i]); i += 1

        # De lo contrario se agrega el elemento j-ésimo a la lista
        else: 
            l_ord.append(right[j]); j += 1

    return l_ord

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