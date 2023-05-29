'''
1.	Ingresar N números enteros y luego mostrar:
•	Cantidad de números pares ingresados
•	Suma de los números positivos
•	Promedio de los números impares ingresados
'''

n=int(input("¿Cuantos numeros desea ingresar?: "))

cont=0
contpar=0
suma=0
sumaimpar=0
contimpar=0

while(cont<n):
    cont+=1
    num=int(input("Ingrese un numero entero: "))

    if(num%2==0):

        contpar+=1

    if(num>0):

        suma+=num

    if(num%2!=0):

        sumaimpar=sumaimpar+num
        contimpar+=1

print("La cantidad de numeros pares es "+str(contpar))
print("La suma de los numeros positivos es "+str(suma))

if (contimpar!=0):
    
    prom=sumaimpar/contimpar
    print("El promedio de los impares es "+str(prom))

else:

    print("No se ingresaron numeros impares")


