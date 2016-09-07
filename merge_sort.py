# Aquí es donde debe de ir su implementación del merge sort
def merge(left, right):
    """
    Merge 2 list and returns a new ordered one.

    left    First list to merge.
    right   Second list to merge.
    """
    ordered_list = list()
    left_list_size = len(left)
    right_list_size = len(right)
    while(len(left) > 0 and len(right) > 0):
        if left[0] <= right[0]:
            ordered_list.append(left.pop(0) )
        else:
            ordered_list.append(right.pop(0) )
    for element in left:
        ordered_list.append(element)
    for element in right:
        ordered_list.append(element)
    return ordered_list

# Esta función recibe una lista y regresa una copia ordenada
def merge_sort(unordered_list):
    """
    Merge sort recursive algorith.
    This algorith divides the list in half creating
    left_list and right_list, then merges both
    in a new ordered one.

    unordered_list  An unordered list to be ordered.
    """
    length = len(unordered_list)
    if length <= 1:
        return unordered_list
    left_list = list()
    right_list = list()
    for i in range(length):
        if i < length // 2:
            left_list.append(unordered_list[i] )
        else:
            right_list.append(unordered_list[i] )
    left = merge_sort(left_list)
    right = merge_sort(right_list)
    return merge(left, right)

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
