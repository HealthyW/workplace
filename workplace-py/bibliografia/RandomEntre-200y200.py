'''
3.	Generar en forma aleatoria N números enteros en el rango -200 a 200. Mostrar por pantalla:
-	Los números generados
-	La suma de los números pares positivos generados
-	El mayor y menor número generado
-	Cantidad de números generados con sólo dos dígitos
'''
import random

print("----------------------------------------------------")
n=int(input("Cuantos numeros desea crear? :"))

cont=0
suma=0
mayor=-201
menor=201
dig2=0
while cont<n:
    cont+=1
    x=random.randint(-200,200)
    print(x,end=", ")
    if(x%2==0 and x>0):
        suma=suma+x
    if(x>mayor):
        mayor=x
    if(x<menor):
        menor=x
    if(x>9 and x<100 ) or (x<-9 and x>-100):
        dig2+=1
   
    

print("\n\n----------------------------------------------------")
print("Suma de los pares positivos: "+str(suma))
print("El numero mayor es "+str(mayor))
print("El numero menor es "+str(menor))
print("La cantidad de numeros de solo dos digitos es "+str(dig2))
print("----------------------------------------------------")