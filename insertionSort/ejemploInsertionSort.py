def insertion_sort(lista):
    for i in range(1, len(lista)):
        valor_actual = lista[i]  # el elemento que se va a insertar en su posición correcta
        posicion = i - 1  #se compara con el elemento anterior

        while posicion >= 0 and valor_actual < lista[posicion]:
            lista[posicion + 1] = lista[posicion]
            posicion -= 1

        lista[posicion + 1] = valor_actual  #se coloca el valor en su lugar correcto

#ejemplo 
mi_lista = [19, 13, 8, 7, 4]
insertion_sort(mi_lista)

print("Lista ordenada:", mi_lista)