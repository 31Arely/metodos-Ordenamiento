def heap(lista, n, i):
    #i: será el índice del nodo raíz
    mas_grande = i
    izquierda = 2 * i + 1
    derecha = 2 * i + 2

    #compara con el hijo izquierdo
    if izquierda < n and lista[mas_grande] < lista[izquierda]:
        mas_grande = izquierda

    #compara con el hijo derecho
    if derecha < n and lista[mas_grande] < lista[derecha]:
        mas_grande = derecha

    #si el más grande no es la raíz, intercambia y seguir haciendo la estructura de datos
    if mas_grande != i:
        lista[i], lista[mas_grande] = lista[mas_grande], lista[i]
        heap(lista, n, mas_grande)

def heap_sort(lista):
    n = len(lista)

    #convertir la lista en un heap
    for i in range(n // 2 - 1, -1, -1):
        heap(lista, n, i)

    #extrae elementos uno por uno del arreglo de datos
    for i in range(n - 1, 0, -1):
        lista[i], lista[0] = lista[0], lista[i] 
        heap(lista, i, 0)

#ejemplo
mi_lista = [12, 11, 13, 5, 6, 7]
heap_sort(mi_lista)

print("Lista ordenada:", mi_lista)