'''
1.	Realizar un programa que permita ingresar apellido 
paterno (debe tener como mínimo tres letras), 
edad (entre 18 y 45 años), color de ojos 
(azules, verdes, cafés o negros, en forma aleatoria), 
sexo (f: femenino, m: masculino, en forma aleatoria), 
estatura (entre 1,30 y 2,00). Validar donde corresponda.
El ingreso se realizará hasta que el usuario lo desee
El programa debe ser capaz de mostrar:
-	Apellido paterno, Color de ojos y sexo de cada persona
-	Cantidad de mujeres
-	Cantidad de hombres mayores a 35 años y su apellido tenga más de 6 caracteres
-	Promedio de las estaturas 
-	Cantidad de hombres con estatura menor a 1,50 mts  
'''
import random
resp="S"
cont=0
contMuj=0
contHom=0
sumaEsta=0
contBajos=0
while(resp=="S"):
    cont+=1
    print("\n\n\t**** Datos Persona N° "+str(cont)+" ****")
    while(True):#Valida apellido
        apellido=input("Ingrese apellido paterno: ").strip()
        if(len(apellido)>=3):
            break
        else:
            print("El appellido debe tener como mínimo 3 caracteres")
    colorOjos=random.choice(["Café","Verde","Azul","Negro"])
    sexo=random.choice("MF")
    while(True):#Valida estatura
        try:
            estatura=float(input("Estatura: "))
            if(estatura>=1.3 and estatura<2):
                break
            else:
                print("\n\tLa estatura debe estar en el rango 1.3 a 2 mts.")
        except ValueError:
            print("\n\tLa estatura debe ser numérica")
    while(True):#Valida edad
        try:
            edad=int(input("Edad: "))
            if(edad>=18 and edad<=45):
                break
            else:
                print("La edad debe estar en el rango 18-45 años")
        except ValueError:
            print("\n\tDebe ser un número entero")

    while(True):#valida resp
        resp=input("¿Desea ingresar a otra persona S/N?: ").upper()
        if(resp=="S" or resp=="N"):
            break
        else:
            print("\n\tLa respuesta debe ser S o N")

    print("\n\tApellido Paterno: "+apellido+"\tSexo: "+sexo+"\tColor de ojos: "+colorOjos)
    if(sexo=="F"):
        contMuj+=1
    if(sexo=="M" and edad>35 and len(apellido)>6):
        contHom+=1
    sumaEsta+=estatura
    if(sexo=="M" and estatura<1.5):
        contBajos+=1
print("\n\n\tCantidad de mujeres: "+str(contMuj))
print("\nCantidad de hombres mayores a 35 y apellido con más de 6 caracteres: "+str(contHom))
prom=sumaEsta/cont
print("\tPromedio de las estaturas: "+str(prom))
print("\tCantidad de hombres con estatura menor a 1.5: "+str(contBajos))