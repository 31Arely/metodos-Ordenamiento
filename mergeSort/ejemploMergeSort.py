def merge_sort(lista):
    if len(lista) > 1:
        #aqui se divide la lista en dos por mitad
        mitad = len(lista) // 2
        izquierda = lista[:mitad]
        derecha = lista[mitad:]

        #se ordena recursivamente cada mitad
        merge_sort(izquierda)
        merge_sort(derecha)

        #se combinan las dos mitades ordenadas
        i = j = k = 0  #i: izquierda, j: derecha, k: lista final

        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                lista[k] = izquierda[i]
                i += 1
            else:
                lista[k] = derecha[j]
                j += 1
            k += 1

        #se copian los elementos restantes de izquierda
        while i < len(izquierda):
            lista[k] = izquierda[i]
            i += 1
            k += 1

        #se copian los elementos restantes de derecha
        while j < len(derecha):
            lista[k] = derecha[j]
            j += 1
            k += 1

#ejemplo
mi_lista = [38, 27, 43, 3, 9, 82, 10]
merge_sort(mi_lista)

print("Lista ordenada:", mi_lista)

