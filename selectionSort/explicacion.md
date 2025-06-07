Shell Sort


Shell Sort compara elementos que están separados por un intervalo (*gap*) 
que se va reduciendo en cada iteración, hasta llegar a 1 
(cuando se convierte en un Insertion Sort normal).

## Pasos
1. Elige un intervalo (*gap*), típicamente la mitad del tamaño del arreglo.
2. Compara y ordenar elementos separados por ese intervalo.
3. Reduce el intervalo y repite.
4. Cuando el intervalo es 1, hacer un Insertion Sort final.


