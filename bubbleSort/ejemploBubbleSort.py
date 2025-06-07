def bubble_sort(lista):
    n = len(lista)
    
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                #se intercambian elementos si están en el orden incorrecto
                lista[j], lista[j+1] = lista[j+1], lista[j]

#ejemplo para uso
mi_lista = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(mi_lista)

print("lista ordenada:", mi_lista)