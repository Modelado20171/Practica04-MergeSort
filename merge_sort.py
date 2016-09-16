# Aquí es donde debe de ir su implementación del merge sort

# Esta función recibe una lista y regresa una copia ordenada
def merge_sort(lista):
    if (len(lista) <= 1):
        return lista
    pivote = len(lista) // 2
    izquierda = lista[:pivote]
    derecha = lista[pivote:]
    izquierda = merge_sort(izquierda)
    derecha = merge_sort(derecha)
    return merge_sort_aux(izquierda, derecha)

def merge_sort_aux(lista_izquierda, lista_derecha):
    lista_aux = list()
    inicio = 0
    fin = 0
    while(inicio < len(lista_izquierda) and fin < len(lista_derecha)):
        if(inicio >= len(lista_izquierda)):
            lista_aux.append(lista_derecha[fin])
            fin += 1 
        elif(fin >= len(lista_derecha)): 
            lista_aux.append(lista_izquierda[inicio]) 
            inicio += 1
        elif(lista_izquierda[inicio] <= lista_derecha[fin]): 
            lista_aux.append(lista_izquierda[inicio]) 
            inicio += 1 
        else: 
            lista_aux.append(lista_derecha[fin]) 
            fin += 1 
            
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
