def bucket_sort_enteros(lista):
    max_val = max(lista)
    buckets = [[] for _ in range(10)]
    
    for num in lista:
        indice = min(num // (max_val // 10), 9)  #aqui se asegura que el índice ≤ 9
        buckets[indice].append(num)
    
    for bucket in buckets:
        bucket.sort()
    
    return [num for bucket in buckets for num in bucket]

#ejemplo
mi_lista = [32, 12, 45, 78, 5, 91]
print("enteros ordenados:", bucket_sort_enteros(mi_lista))