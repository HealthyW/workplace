'''
2.	Ingresar la edad y género ([M]: Masculino, [F]: Femenino) de N personas y luego mostrar:
-	Promedio de las edades de los hombres
-	Cantidad de mujeres con edad mayor a 30 años
-	Mayor edad ingresada
'''

n=int(input("Ingrese el numero de personas: "))

cont=0
sumaHombre=0
contHombre=0
contMujer=0
mayor=0

while(cont<n):
    cont+=1
    print("***** Datos persona N° "+str(cont)+" *****")
    edad=int(input("Edad: "))
    genero=input("genero: M:MASCULINO o F:FEMENINO: ").upper()
    if(genero=="M"):
        sumaHombre=sumaHombre+edad
        contHombre+=1
    if(genero=="F" and edad>30):
        contMujer+=1
    if(edad>mayor):
        mayor=edad

print("La mayor edad ingresada es "+str(mayor))
print("Cantidad de mujeres mayor a 30 años: "+str(contMujer))
if(contHombre!=0):
    prom=sumaHombre/contHombre
    print("El promedio de las edades de los hombres es "+str(prom))
else:
    print("No se ingresaron hombres")



