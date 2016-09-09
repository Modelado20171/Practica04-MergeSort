# Esta función recibe una lista y regresa una copia ordenada
def merge_sort(lista):
    return split(lista)

#Va a partir la lista hasta que solo tengan un elemento.
def split(lista):
    if len(lista) == 1:
        return lista
    else:
        mitad = len(lista)//2
        mitadIzquierda = lista[:mitad]
        mitadDerecha = lista[mitad:]
    return merge(split(mitadIzquierda), split(mitadDerecha))
        
#Va a comparar cada elemento de la lista y ordenarla        
def merge(mitadIzquierda, mitadDerecha):
    
    listaOrdenada = list()
    i=j=0    
    while i < len(mitadIzquierda) and j < len(mitadDerecha):
        if mitadIzquierda[i] < mitadDerecha[j]:
            listaOrdenada.append(mitadIzquierda[i])
            i = i + 1
        else:
            listaOrdenada.append(mitadDerecha[j])
            j = j + 1
    while i < len(mitadIzquierda):
        listaOrdenada.append(mitadIzquierda[i])
        i=i+1
    while j < len(mitadDerecha):
        listaOrdenada.append(mitadDerecha[j])
        j=j+1
        
    return listaOrdenada
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
