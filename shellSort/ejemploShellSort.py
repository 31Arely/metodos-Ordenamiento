def shell_sort(lista):
    n = len(lista)
    #define la secuencia de gaps
    gap = n // 2
    
    while gap > 0:
        #aplica insertion sort para cada gap
        for i in range(gap, n):
            temp = lista[i]
            j = i
            #mueve elementos anteriores en el gap hasta encontrar la posición correcta
            while j >= gap and lista[j - gap] > temp:
                lista[j] = lista[j - gap]
                j -= gap
            lista[j] = temp
        gap //= 2  #reduce el gap

#ejemplo
mi_lista = [35, 12, 29, 17, 8, 23, 5]
shell_sort(mi_lista)

print("Lista ordenada:", mi_lista)


