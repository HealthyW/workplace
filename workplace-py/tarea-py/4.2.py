'''
2.	Ingresar la edad y género ([M]: Masculino, [F]: Femenino) de N personas y luego mostrar:
-	Promedio de las edades de los hombres
-	Cantidad de mujeres con edad mayor a 30 años
-	Mayor edad ingresada
'''

while True:
    try:
        cant_pers=int(input("Ingrese la cantidad de personas que desea registrar: "))
        if cant_pers>0:
            break
        elif cant_pers<0:
            print("\tIngrese un numero verdadero")
        else:
            print("\tIngrese un digito valido")
    except ValueError:
        print("\t Ingrese un digito valido")


cont=0
cont_m=0
cont_f=0
edad=0
acu_m=0
promedio_m=0
cont_fmayor30=0
mayor=0

while cont<cant_pers:
    cont+=1
    print("+++++++++++++++++++++++++++++++++++++")
    print("     [M] Masculino")
    print("     [F] Femenino")
    print("+++++++++++++++++++++++++++++++++++++")
    while True:
        try:
            genero=input("Ingrese el genero de la persona: ").lower()
            cantidad_caracteres= len(genero)
            if genero=="m" or genero=="f":
                break
            else:
                print("\tIngrese un caracter")
        except ValueError:
            print("Ingrese un caracter")
    while True:
        try:
            edad=int(input("Ingrese la edad de la persona: "))
            if edad>0:
                break
        except ValueError:
            print("\tIngrese un numero entero")
    
    if genero=="m":
        cont_m+=1
        acu_m=edad+acu_m
        promedio_m=acu_m/cont_m
    if genero=="f":
        cont_f+=1
    if genero=="f" and edad>30:
        cont_fmayor30+=1
    if (edad>mayor):
        mayor=edad
    



print("+++++++++++++++++++++++++++++++++++++")
if cont_m!=0:
    print("     Promedio de las edades de los hombres: ", promedio_m)
else:
    print("     No se ingresaron hombres    ")
print("     Cantidad de mujeres con edad mayot a 30 años: ", cont_fmayor30)
print("     Mayor edad ingresada: ", mayor)
print("+++++++++++++++++++++++++++++++++++++")






