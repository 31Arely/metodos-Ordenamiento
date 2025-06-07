Radix Sort


Radix Sort ordena los números **dígito por dígito**, 
empezando por el dígito menos significativo (por ejemplo, las unidades). 

**Funciona bien con números enteros no negativos**.

## Pasos
1. Encuentra el número con más dígitos.
2. Ordena los números por cada posición decimal:
   - Unidades
   - Decenas
   - Centenas
   - ...
3. Utiliza Counting Sort en cada paso para mantener la estabilidad.


