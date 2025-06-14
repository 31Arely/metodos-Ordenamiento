def selection_sort(lista):
    n = len(lista)
    
    for i in range(n):
        #encuentra el mínimo en la parte desordenada
        min_idx = i
        for j in range(i + 1, n):
            if lista[j] < lista[min_idx]:
                min_idx = j
        
        #intercambia el mínimo con el primer elemento desordenado
        lista[i], lista[min_idx] = lista[min_idx], lista[i]

#ejemplo
mi_lista = [64, 25, 12, 22, 11]
selection_sort(mi_lista)

print("Lista ordenada:", mi_lista)


