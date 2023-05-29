primeras_filas=180000
diamante=165000
diamante_lateral=145000
platea_baja=115000
cont=0
cont_internet=0
valor_totalpf=0
valor_totald=0
valor_totaldl=0
valor_totalpb=0
mayor=0
cont_pf=0
total_recaudado=0
opcion=0
total_pf=0
total_d=0
total_dl=0
total_pb=0

while True:
    
    if opcion==6:
        break
    
    print("\n ******* MOVISTAR ARENA ******* ")
    print("==============================")
    print("     [1]-> Primeras Filas")
    print("     [2]-> Diamante")
    print("     [3]-> Diamante Lateral")
    print("     [4]-> Platea Baja Diamante ")
    print("     [5]-> Reportes")
    print("     [6]-> Salir del Sistema ")
    print("==============================")
    
    while True:#valida
        try:
            opcion=int(input("      Elija Opcion: "))
            if opcion>0:
                break
            if opcion>6 and opcion<1:
                print("\tIngrese una opcion valida")
            if opcion<0:
                print("\tIngrese una opcion valida")
        except ValueError:
            print("\tElija una opcion valida")
    
    if opcion==5:
        print("\n------------------------------ Reportes ---------------------------------------")
        print("•	Cantidad de clientes que compraron por internet: ", cont_internet)
        print("•	Total recaudado :    $", total_recaudado)
        print("•	Total recaudado por ubicación: ")
        print("     • Primeras filas:       $", total_pf)
        print("     • Dimante:              $", total_d)
        print("     • Diamante Lateral:     $", total_dl)
        print("     • Platea Baja Diamante: $", total_pb)
        print("•	Mayor valor total cancelado: $", mayor)
        print("•	Cantidad total de entradas vendidas en ubicación primeras filas: ", cont_pf)
        print("-------------------------------------------------------------------------------")
    
    if opcion<5 and opcion>=1:
        while True:#valida
            try:
                entradas=int(input("¿Cuantas entradas quiere?: "))
                if entradas>0:
                    break
                if entradas<0:
                    print("\tIngrese un numero positivo")
                else:
                    ("\tIngrese un numero entero ")
            except ValueError:
                print("\tIngrese un numero")
        
        while True:#valida
            try:
                tipo_compra=input("¿Como compro la entrada?([P] Presencial/[I] Internet): ").lower()
                if tipo_compra=="p" or tipo_compra=="i":
                    break
                else:
                    print("\tIngrese un caracter valido")
            except ValueError:
                print("\tIngrese un caracter valido")
        
        if tipo_compra=="i":
            cont_internet+=1
            if opcion==1:
                cont_pf+=1
                valor_totalpf=primeras_filas*entradas
                print("\n++++++++++++++++++++++++++++++++++++++++++++")
                print("     Ubicacion: Primeras Filas")
                print("     Valor total a cancelar: ",valor_totalpf)
                print("++++++++++++++++++++++++++++++++++++++++++++")
            if opcion==2:
                valor_totald=diamante*entradas
                print("\n++++++++++++++++++++++++++++++++++++++++++++")
                print("     Ubicacion: Diamante")
                print("     Valor total a cancelar: ",valor_totald)
                print("++++++++++++++++++++++++++++++++++++++++++++")
            if opcion==3:
                valor_totaldl=diamante_lateral*entradas
                print("\n++++++++++++++++++++++++++++++++++++++++++++")
                print("     Ubicacion: Diamante Lateral")
                print("     Valor total a cancelar: ",valor_totaldl)
                print("++++++++++++++++++++++++++++++++++++++++++++")
            if opcion==4:
                valor_totalpb=platea_baja*entradas
                print("\n++++++++++++++++++++++++++++++++++++++++++++")
                print("     Ubicacion: Platea Baja Diamante")
                print("     Valor total a cancelar: ",valor_totalpb)
                print("++++++++++++++++++++++++++++++++++++++++++++")
        
        if tipo_compra=="p":
            if opcion==1:
                cont_pf+=1
                valor_totalpf=(entradas*primeras_filas+18000)
                print("\n++++++++++++++++++++++++++++++++++++++++++++")
                print("     Ubicacion: Primeras Filas")
                print("     Valor total a cancelar: ",valor_totalpf)
                print("++++++++++++++++++++++++++++++++++++++++++++")
            if opcion==2:
                valor_totald=(entradas*diamante+18000)
                print("\n++++++++++++++++++++++++++++++++++++++++++++")
                print("     Ubicacion: Diamante")
                print("     Valor total a cancelar: ",valor_totald)
                print("++++++++++++++++++++++++++++++++++++++++++++")
            if opcion==3:
                valor_totaldl=(entradas*diamante_lateral+18000)
                print("\n++++++++++++++++++++++++++++++++++++++++++++")
                print("     Ubicacion: Diamante Lateral")
                print("     Valor total a cancelar: ",valor_totaldl)
                print("++++++++++++++++++++++++++++++++++++++++++++")
            if opcion==4:
                valor_totalpb=(entradas*platea_baja+18000)
                print("\n++++++++++++++++++++++++++++++++++++++++++++")
                print("     Ubicacion: Platea Baja Diamante")
                print("     Valor total a cancelar: ",valor_totalpb)
                print("++++++++++++++++++++++++++++++++++++++++++++")
        

        total_pf=total_pf+valor_totalpf
        total_d=total_d+valor_totald
        total_dl=total_dl+valor_totaldl
        total_pb=total_pb+valor_totalpb


        total_recaudado=(valor_totalpf+valor_totald+valor_totaldl+valor_totalpb)+total_recaudado
        if mayor<valor_totalpf:
            mayor=valor_totalpf
        if mayor<valor_totald:
            mayor=valor_totald
        if mayor<valor_totaldl:
            mayor=valor_totaldl
        if mayor<valor_totalpb:
            mayor=valor_totalpb

print("\n*******************************")
print("     Salio del programa")
print("*******************************")
