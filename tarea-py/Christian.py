entrada=0
valor=0       
cont=0
cargo_servicio=0
valor_total=0
resp=""
compra_online=0
mayor_valor=0
total_primera_fila = 0
total_diamante = 0
total_diamante_lateral = 0
total_platea_baja_diamante = 0
max_valor_total = 0
entradas_primera_fila = 0
while True:
    print("\n***********MOVISTAR ARENA***************")
    print("1.-Primera Fila")
    print("2.-Diamante")
    print("3.-Diamante Lateral")
    print("4.-Platea Baja Diamante")
    print("5.-Reportes")
    print("6.-Salir del Sistema.")
    while True:
        try:
            opcion=int(input("Escoja una Opción: "))
            if opcion>=1 and opcion<=6:
                break
        except ValueError:
            print("ingrese una opción valida. ")

    while True:
        if valor_total > max_valor_total:
            max_valor_total = valor_total
        
        if opcion ==1:
            entradas_primera_fila+=1
            total_primera_fila += valor_total
            entrada=int(input("¿Cuantas entradas desea comprar?: "))
            print("1.- Compra presencial")
            print("2.- Compra Online")
            while True:
                try:
                    compra=int(input("Escoja una Opción: "))
                    if compra==1 or compra==2:
                        break
                except ValueError:
                    print("Ingrese una opción válida.")
            if compra ==1:
                cargo_servicio=18000
                valor_total= entrada*180000+cargo_servicio
                print("\nUbicación: Primera filas ")
                print("Valor total a cancelar: $"+ str(valor_total))
            else:
                compra_online+=1
                valor_total= entrada*180000
                print("\nUbicación: Primera filas ")
                print("Valor total a cancelar: $"+ str(valor_total))    
            break
        
        if opcion ==2:
            total_diamante += valor_total
            entrada=int(input("¿Cuantas entradas desea comprar?: "))
            print("1.- Compra presencial")
            print("2.- Compra Online")
            while True:
                try:
                    compra=int(input("Escoja una Opción: "))
                    if compra==1 or compra==2:
                        break
                except ValueError:
                    print("Ingrese una opción válida.")
            if compra==1:
                cargo_servicio=16500
                valor_total= entrada*165000+cargo_servicio
                print("\nUbicación: Diamante ")
                print("Valor total a cancelar: $"+ str(valor_total))
            else:
                compra_online+=1
                valor_total= entrada*165000
                print("\nUbicación: Diamante ")
                print("Valor total a cancelar: $"+ str(valor_total))    
            break
        
        if opcion ==3:
            total_diamante_lateral += valor_total
            entrada=int(input("¿Cuantas entradas desea comprar?: "))
            print("1.- Compra presencial")
            print("2.- Compra Online")
            while True:
                try:
                    compra=int(input("Escoja una Opción: "))
                    if compra==1 or compra==2:
                        break
                except ValueError:
                    print("Ingrese una opción válida.")
            if compra ==1:
                cargo_servicio=14500
                valor_total= entrada*145000+cargo_servicio
                print("\nUbicación: Diamante Lateral ")
                print("Valor total a cancelar: $"+ str(valor_total))
            else:
                compra_online+=1
                valor_total= entrada*145000
                print("\nUbicación: Diamante Lateral ")
                print("Valor total a cancelar: $"+ str(valor_total))    
            break
        
        if opcion ==4:
            total_platea_baja_diamante += valor_total
            entrada=int(input("¿Cuantas entradas desea comprar?: "))
            print("1.- Compra presencial")
            print("2.- Compra Online")
            while True:
                try:
                    compra=int(input("Escoja una Opción: "))
                    if compra==1 or compra==2:
                        break
                except ValueError:
                    print("Ingrese una opción válida.")
            if compra ==1:
                cargo_servicio=11500
                valor_total= entrada*115000+cargo_servicio
                print("\nUbicación: Platea Baja Diamante ")
                print("Valor total a cancelar: $"+ str(valor_total))
            else:
                compra_online+=1
                valor_total= entrada*115000
                print("\nUbicación: Platea Baja Diamante ")
                print("Valor total a cancelar: $"+ str(valor_total))    
            break
        
        if opcion==5:
            print("\nReportes: ")
            print("• Cantidad de clientes que compraron por internet: "+ str(compra_online))
            print("• Total recaudado por ubicación: " )
            print("  - Primera fila: $" + str(total_primera_fila))
            print("  - Diamante: $" + str(total_diamante))
            print("  - Diamante Lateral: $" + str(total_diamante_lateral))
            print("  - Platea Baja Diamante: $" + str(total_platea_baja_diamante))
            print("• Mayor valor total cancelado: "+str(max_valor_total))
            print("• Cantidad total de entradas vendidas en ubicación primeras filas: "+str(entradas_primera_fila))        
        break
    if opcion==6:
        break