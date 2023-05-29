while(True):#Valida cantidad de clientes
    try:
        n=int(input("Ingrese cantidad de clientes: "))
        if(n>0):
            break
        else:
            print("\tLa cantidad debe ser mayor a cero")
    except ValueError:
        print("\tLa cantidad debe ser un número entero")

cont=0
totalRecaudado=0
cantidadChuraSolo=0
cantidadChuraMayo=0
while(cont<n):
    cont+=1
    resp="S"
    total=0

    while(resp=="S"):
        print("******** Cliente   N° "+str(cont)+" ******** ")
        print("==============================")
        print("[1]-> Churrasco solo") 
        print("[2]-> Churrasco italiano")
        print("[3]-> Churrasco Mayo ")
        
        while(True):#valida opción
            try:
                opcion=int(input("\tElija Opción: "))
                if(opcion>=1 and opcion<=3):
                    break
                else:
                    print("\tLa opción debe estar en el rango 1 a 3")
            except ValueError:
                print("\tLa opción debe ser un número entero")
        while(True):#valida cantidad
            try:
                cantidad=int(input("\tcantidad: "))
                if(cantidad>=1 ):
                    break
                else:
                    print("\tLa cantidad debe ser mayor a 0")
            except ValueError:
                print("\tLa cantidad debe ser un número entero")
        while(True):#Valida resp
            resp=input("Desea llevar otro poroducto S/N: ").upper()
            if(resp=="S" or resp=="N"):
                break
            else:
                print("\tLa respuesta sólo puede ser S o N")
        
        if(opcion==1):
            cantidadChuraSolo+=cantidad
            valor=2500
            
        elif(opcion==2):
            valor=3800
            
        else:
            cantidadChuraMayo+=cantidad
            valor=3000
            
        subTotal=valor*cantidad
        total+=subTotal
        
    print("Total a pagar $"+str(total))
    totalRecaudado+=total
    
print("\n\tReportes")
print("Total recaudado $"+str(totalRecaudado))
print("Cantidad de churrasco solo: "+str(cantidadChuraSolo))
totalChurraMayo=cantidadChuraMayo*3000
print("Total recaudado churrasco mayo: "+str(totalChurraMayo))
