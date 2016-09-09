
def merge_sort(lista):
    lista_Izquierda = list()
    lista_Derecha = list()
    if ((len(lista) == 0) or (len(lista) == 1)):
        return lista
    else:
        mitad = len(lista)/2
        for i in range(0, mitad):
           	lista_Izquierda.append(lista[i])
        for j in range(mitad,len(lista)):
           	lista_Derecha.append(lista[j])

    return Ordenamiento(merge_sort(lista_Izquierda), merge_sort(lista_Derecha)) 
        

def Ordenamiento(lista_Izquierda, lista_Derecha):
    lista_Ordenada = list()
    
    while len(lista_Izquierda) > 0 and len(lista_Derecha) > 0:
        if lista_Izquierda[0] <= lista_Derecha[0]:
            lista_Ordenada.append(lista_Izquierda[0])
        else:
            ordenado.append(lista_Derecha[0])

            
    while len(lista_Izquierda) > 0 or len(lista_Derecha) > 0:   
        if len(lista_Izquierda) > 0:
            lista_Ordenada.append(lista_Izquierda[0])
        if len(lista_Derecha) > 0:
            lista_Ordenada.append(lista_Derecha[0])
        
    return lista_Ordenada


lista1 = [1,2,3,4,5,6]
lista2 = [6,5,4,3,2,1]
lista3 = [5,3,8,1,3,8,7,8,2,1,6,8,1,3,8]

listaOrdenada1 = merge_sort(lista1)
listaOrdenada2 = merge_sort(lista2)
listaOrdenada3 = merge_sort(lista3)

print(listaOrdenada1)
print(listaOrdenada2)
print(listaOrdenada3)




		