# Aquí es donde debe de ir su implementación del merge sort

# Esta función recibe una lista y regresa una copia ordenada
def merge_sort(lista):
    if len(lista)==0:
        return []
    elif len(lista)==1:
        return [lista[0]]
    else:
        return merge(merge_sort(lista[:len(lista)//2]), merge_sort(lista[len(lista)//2:]))

def merge(comp_list1,comp_list2):
    ordered_list=[]
    while len(comp_list1)>0 and len(comp_list2)>0:
        if comp_list1[0]>comp_list2[0]:
            ordered_list.append(comp_list2[0])
            comp_list2=comp_list2[1:]
        else:
            ordered_list.append(comp_list1[0])
            comp_list1=comp_list1[1:]
    if len(comp_list1)!=0:
        ordered_list.extend(comp_list1)
    if len(comp_list2)!=0:
        ordered_list.extend(comp_list2)
    return ordered_list


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
