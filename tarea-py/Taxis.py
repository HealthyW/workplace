import random
import numpy
opcion=0
taxi=[]
taxiMay=0
taxiMen=0
for i in range(20):
    taxi.append(round(random.uniform(0,500),2))

while True:

    if opcion ==6:
        break

    print("******* HUBBER  ******")
    print("1.	 Kilómetros recorridos")
    print("2.	 Mayor y menor kilometro")
    print("3.	 Mayor que el promedio ")
    print("4.	 Total ganado")
    print("5.	 Jornada lenta")
    print("6.	 Salir")

    while True: #Valida opcion
        try:    
            opcion=int(input("      Elija opcion: "))
            if opcion>0 and opcion<=6:
                break
            if opcion<0:
                print("Ingrese un numero positivo")
        except ValueError:
            print("Ingrese una opcion valida")
    
    if opcion==1:
        for i in range (20):
            print("Taxi N° ", i+1, " => ", taxi[i] ,"Km")
    
    if opcion==2:
        mayor=-1
        menor=501
        for i in range (20):
            if taxi[i]>mayor:
                mayor=taxi[i]
                taxiMay+=1
            if taxi[i]<menor:
                menor=taxi[i]
                taxiMen+=1
        print("Taxi N° ", mayor," es el taxi con mayor kilometros recorridos")
        print("Taxi N° ",menor," es el taxo con menos kilometros recorridos")
    
    if opcion==3:
        pass


print("************************************")
print("     Salio del programa")
print("************************************")