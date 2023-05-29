cont=0
n=0 
juego_sabana=0
total_pagar=0
total_recaudado=0

while True:#Valida variable "n"
    try:
        n=int(input("Ingrese la cantidad de clientes: "))
        if n>0:
            break
        if n<0:
            print("\tIngrese un numero entero positivo")
    except ValueError:
        print("\tIngrese un digito valido")

while cont<n:
    cont+=1
    deseo="s"
    total_acumulado=0
    
    
    while deseo=="s" or deseo=="si":
        print("\n********    Cliente   N°    0"+ str(cont)+"     ******** ")
        print("     ==============================")
        print("     [1]-> Juegos Sábanas (1 plaza)")
        print("     [2]-> Juegos Sábanas (1.5 plazas)")
        print("     [3]-> Juegos Sábanas (2 plazas)")
        print("     [4]-> Juegos Sábanas (King)")
        
        while True:#Valida variable "opcion"
            try:
                opcion=int(input("         Elija Opción: "))
                if opcion>=1 and opcion<5:
                    break
                else:
                    print("\tIngrese una opcion valida")  
            except ValueError:
                print("\tIngrese una opcion valida")
        
        while True:#Valida variable "cantidad_s"
            try:
                cantidad_s=int(input("Ingrese cantidad de sabanas a lavar: "))
                if cantidad_s>0:
                    break
                if cantidad_s<0:
                    print("\tIngrese un numero entero positivo")
            except ValueError:
                print("\tIngrese una opcion valida")
        
        while True:#Valida variable "vip"
                try:
                    vip=(input("¿Usted es cliente VIP? si[S],no[N]: ")).lower()
                    if vip=="s" or vip=="n" or vip=="si" or vip=="no":
                        break
                    else:
                        print("\tIngrese una opcion valida")
                except ValueError:
                    print("\tIngrese una opcion valida")
        
        if vip=="n" or vip=="no":
            if opcion==1:
                juego_sabana=1500
                total_pagar=juego_sabana*cantidad_s
            
            if opcion==2:
                juego_sabana=2000
                total_pagar=juego_sabana*cantidad_s
            
            if opcion==3:
                juego_sabana=2500
                total_pagar=juego_sabana*cantidad_s
            
            if opcion==4:
                juego_sabana=3000
                total_pagar=juego_sabana*cantidad_s
        
        if vip=="s" or vip=="si":
            if opcion==1:
                juego_sabana=1500   
                total_pagar=(juego_sabana*cantidad_s)*0.8
            
            if opcion==2:
                juego_sabana=2000
                total_pagar=(juego_sabana*cantidad_s)*0.8
            
            if opcion==3:
                juego_sabana=2500
                total_pagar=(juego_sabana*cantidad_s)*0.8
            
            if opcion==4:
                juego_sabana=3000
                total_pagar=(juego_sabana*cantidad_s)*0.8
        
        while True:#Valida variable "deseo"
            try:
                deseo=(input("¿Desea lavar otro producto? si[S],no[N]: ")).lower()
                if deseo=="s" or deseo=="n" or deseo=="si" or deseo=="no":
                    break
                else:
                    print("\tIngrese una opcion valida")
            except ValueError:
                print("\tIngrese una opcion valida")
        
        total_acumulado+=total_pagar
        total_recaudado+=total_pagar
    print("\n+++++++++++++++++++++++++++++++++++++")
    print("     Total a pagar: $"+ str(total_acumulado))
    print("+++++++++++++++++++++++++++++++++++++")

print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("     Total Recaudado: $"+ str(total_recaudado))
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
