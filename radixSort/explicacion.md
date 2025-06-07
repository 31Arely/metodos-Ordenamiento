Bucket Sort


Bucket Sort divide los elementos en varios "cubos" (buckets), 
distribuyéndolos según su valor. Luego ordena individualmente cada cubo 
(usualmente con otro algoritmo como Insertion Sort) y finalmente los concatena.

Funciona mejor con **números reales entre 0 y 1**, o con datos distribuidos uniformemente.

## Pasos
1. Crea N buckets vacíos.
2. Distribuye los elementos en los buckets según su valor.
3. Ordena cada bucket.
4. Combina todos los buckets en un solo arreglo ordenado.


