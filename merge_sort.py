import sys

# Aquí es donde debe de ir su implementación del merge sort

# Esta función recibe una lista y regresa una copia ordenada
def merge_sort(listilla):
    if len(listilla)>1:
        mid = len(listilla)//2
        izquierda = listilla[:mid]
        derecha = listilla[mid:]

        merge_sort(izquierda)
        merge_sort(derecha)

        i=0
        m=0
        n=0
        while i < len(izquierda) and m < len(derecha):
            if izquierda[i] < derecha[m]:
                listilla[n]=izquierda[i]
                i=i+1
            else:
                listilla[n]=derecha[m]
                m=m+1
            n=n+1

        while i < len(izquierda):
            listilla[n]=izquierda[i]
            i=i+1
            n=n+1

        while m < len(derecha):
            listilla[n]=derecha[m]
            m=m+1
            n=n+1
    return listilla


# Tienes estríctamente prohibido borrar líneas después de este punto

print('\n--[Ejemplos de listas a ordenar]--\n')
lista1 = [1,2,3,4,5,6]
lista2 = [6,5,4,3,2,1]
lista3 = [5,3,8,1,3,8,7,8,2,1,6,8,1,3,8]
print(lista1)
print(lista2)
print(lista3)

listaOrdenada1 = merge_sort(lista1)
listaOrdenada2 = merge_sort(lista2)
listaOrdenada3 = merge_sort(lista3)

print('\n--[Resultados de merge_sort]--\n')
print(listaOrdenada1)
print(listaOrdenada2)
print(listaOrdenada3)

print('\n--[Ingrese valores a ordenar]--\n($quit para salir del programa)\n')

while True:
    aordenar = input()
    if aordenar == 'quit':
        sys.exit(0)
    else:
        x = aordenar.split()
        merge_sort(x)
        print(x, '\n')
