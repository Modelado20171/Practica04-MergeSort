def merge_sort(lista):
        if len(lista) == 1:
                return lista
        else:
                mid = len(lista)/2
                left = merge_sort(lista[:mid])
                right = merge_sort(lista[mid:])

        i, j, k = 0, 0, 0 

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                seq[k] = left[i]
                i += 1; k += 1
            else:
                seq[k] = right[j]
                j += 1; k += 1

        remaining = left if i < j else right
        r = i if remaining == left else j

        while r < len(remaining):
            lista[k] = remaining[r]
            r += 1; k += 1

        return lista


        lista1 = [1,2,3,4,5,6]
        lista2 = [6,5,4,3,2,1]
        lista3 = [5,3,8,1,3,8,7,8,2,1,6,8,1,3,8]

        listaOrdenada1 = merge_sort(lista1)
        listaOrdenada2 = merge_sort(lista2)
        listaOrdenada3 = merge_sort(lista3)

        print(listaOrdenada1)
        print(listaOrdenada2)
        print(listaOrdenada3)
