# Aquí es donde debe de ir su implementación del merge sort

# Esta función recibe una lista y regresa una copia ordenada
def merge_sort(lista):
    if (len(lista) <= 1):
    	return lista

    mitad = len(lista)//2
    mitad_izq = lista[:mitad]
    mitad_der = lista[mitad:]

    mitad_izq = merge_sort(mitad_izq)
    mitad_der = merge_sort(mitad_der)

    return (merge(mitad_izq, mitad_der))

#Función para unir y ordenar dos listas ordenadas
#Recibe dos listas ordenadas
#Regresa una lista ordenada con la union de las listas que recibió
def merge(mitad_izq, mitad_der):
    resultado = []

    while (len(mitad_der) != 0 and len(mitad_izq) != 0):
        if mitad_der[0] < mitad_izq[0]:
            resultado.append(mitad_der.pop(0))
        else:
            resultado.append(mitad_izq.pop(0))

    if (len(mitad_izq) == 0):
        resultado = resultado + mitad_der
    else:
        resultado = resultado + mitad_izq

    return resultado

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
