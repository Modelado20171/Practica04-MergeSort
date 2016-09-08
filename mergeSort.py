
def unir(uno, dos):
    ordenada = list()
    i = 0
    j = 0
    while i < len(uno) and j < len(dos):
        if (uno[i] - dos[j]) < 0:
            ordenada.append(uno[i])
            i += 1
        else:
            ordenada.append(dos[j])
            j += 1

    while j < len(dos):
        ordenada.append(dos[j])
        j += 1

    while i < len(uno):
        ordenada.append(uno[i])
        i += 1
    return ordenada

def mergeSort(lista):
    if len(lista) <= 1:
        return lista.copy()
    primeros = []
    ultimos = []
    i = 0
    while(i < len(lista)/2):
        primeros.append(lista[i])
        i += 1
    h = int(len(lista)/2)
    while h < len(lista):
        ultimos.append(lista[h])
        h += 1
    primeros = mergeSort(primeros)
    ultimos = mergeSort(ultimos)
    return unir(primeros,ultimos)
