'''
3.	Generar en forma aleatoria N números enteros en el rango -200 a 200. Mostrar por pantalla:
-	Los números generados
-	La suma de los números pares positivos generados
-	El mayor y menor número generado
-	Cantidad de números generados con sólo dos dígitos
'''

import random

a=int(input("Ingrese N numeros enteros: "))

cont=0
n_aleatorio=0


while cont<a:
    n_aleatorio=random.randint(-200,200)
    print(n_aleatorio, end=(", "))
    cont+=1
