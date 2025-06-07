def counting_sort(lista):
    #encouentra el valor máximo en la lista
    max_valor = max(lista)
    
    #crea un arreglo de conteo inicializado en ceros
    conteo = [0] * (max_valor + 1)
    
    #contar la frecuencia de cada elemento
    for num in lista:
        conteo[num] += 1
    
    #reconstruir la lista ordenada
    lista_ordenada = []
    for num in range(len(conteo)):
        lista_ordenada.extend([num] * conteo[num])
    
    return lista_ordenada

#ejemplo
mi_lista = [4, 2, 2, 8, 3, 3, 1]
lista_ordenada = counting_sort(mi_lista)

print("Lista ordenada:", lista_ordenada)