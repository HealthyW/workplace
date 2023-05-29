figura_indicada=0

while True:

    if figura_indicada>4 or figura_indicada<0:
        print("+++++++++++++++++++++++++++++++++++++++++++++++++")
        print("     Ingrese un numero valido, porfavor")
        print("+++++++++++++++++++++++++++++++++++++++++++++++++")
    
    if figura_indicada==4:
        break
        

    print("--------------------------")
    print("         Figuras          ")
    print("     1.-Triangulo")
    print("     2.-Cuadrado")
    print("     3.-Circulo")
    print("     4.-Salir")
    print("--------------------------")
    
    figura_indicada=int(input("Ingrese el numero de la figura indicada: "))
    if figura_indicada == 1:
    
        base=int(input("¿Cual es la base del triangulo?"))
        altura=int(input("¿Cual es la altura del triangulo?"))
        area_triangulo=(base*altura)/2
        print("El area del triangulo es:", area_triangulo)

    if figura_indicada == 2:
    
        lado_cuadrado=int(input("Ingrese el lado del cuadrado: "))
        area_cuadrado= lado_cuadrado**2
        print("El area del cuadrado es: ", area_cuadrado)
    
    if figura_indicada == 3:
    
        radio_circulo=int(input("Ingrese el radio del circulo: "))
        area_circulo= 3.14*radio_circulo**2 
        print("El area del circulo es :", area_circulo)
        


print("++++++++++++++++++++++++++++++++++++")
print("     Te salistes del programa")    
print("++++++++++++++++++++++++++++++++++++")

    





