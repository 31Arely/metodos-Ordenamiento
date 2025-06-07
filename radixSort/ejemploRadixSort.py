def radix_sort(lista):
    #encuentra el número máximo para saber el número de dígitos
    max_num = max(lista)
    
    #realiza counting sort para cada dígito (unidades, decenas...)
    exp = 1
    while max_num // exp > 0:
        counting_sort_por_digito(lista, exp)
        exp *= 10  #pasa al siguiente dígito (unidades → decenas...)

def counting_sort_por_digito(lista, exp):
    n = len(lista)
    salida = [0] * n
    conteo = [0] * 10  #para dígitos del 0 al 9

    #aqui se cuentar la frecuencia de cada dígito en la posición actual
    for i in range(n):
        indice = (lista[i] // exp) % 10
        conteo[indice] += 1

    #aqui se calculan las posiciones acumuladas
    for i in range(1, 10):
        conteo[i] += conteo[i - 1]

    #aqui se construye la lista de salida
    i = n - 1
    while i >= 0:
        indice = (lista[i] // exp) % 10
        salida[conteo[indice] - 1] = lista[i]
        conteo[indice] -= 1
        i -= 1

    #copiar la lista ordenada al arreglo original
    for i in range(n):
        lista[i] = salida[i]

#ejemplo
mi_lista = [170, 45, 75, 90, 802, 24, 2, 66]
radix_sort(mi_lista)

print("Lista ordenada:", mi_lista)


