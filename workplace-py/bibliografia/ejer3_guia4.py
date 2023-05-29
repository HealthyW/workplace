'''
3.	Generar en forma aleatoria N números enteros en el rango -200 a 200. Mostrar por pantalla:
-	Los números generados
-	La suma de los números pares positivos generados
-	El mayor y menor número generado
-	Cantidad de números generados con sólo dos dígitos

'''
import random
n=int(input("Ingrese cantidad que desea generar: "))
cont=0
suma=0
numMayor=-201
numMenor=201
cont2=0
while(cont<n):
    cont+=1
    x=random.randint(-200,200)
    print(x,end=", ")
    if(x%2==0 and x>0):
        suma=suma+x
    if(x>numMayor):

        numMayor=x
    if(x<numMenor):
        numMenor=x
    if((x>9 and x<100) or(x<-9 and x>-100)):
        cont2+=1
print("\n\n\t***** Estadísticas******")
print("Suma de los pares positivos: "+str(suma))
print("Mayor número: "+str(numMayor))
print("Menor número: "+str(numMenor))
print("Cantidad con sólo dos dígitos: "str(cont2))