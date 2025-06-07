def quick_sort(lista):
    #caso base: si la lista tiene 0 o 1 elemento, ya está ordenada
    if len(lista) <= 1:
        return lista
    
    #se elige un "pivote" (en este caso, el primer elemento)
    pivote = lista[0]
    
    #se divide la lista en tres partes:
    menores = [x for x in lista[1:] if x <= pivote]  #elementos <= pivote
    mayores = [x for x in lista[1:] if x > pivote]   #elementos > pivote
    
    #ordenar recursivamente y combinar
    return quick_sort(menores) + [pivote] + quick_sort(mayores)

#ejemplo
mi_lista = [15, 68, 35, 3, 8, 12]
lista_ordenada = quick_sort(mi_lista)

print("Lista ordenada:", lista_ordenada)