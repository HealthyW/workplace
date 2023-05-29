
from calendar import c


a=int(input("ingrese la cantidad de computadores que compró: "))
b=int(input("ingrese el valor de cada computador: "))
c=input("forma de pago: Efectivo o tarjeta: ").lower()

totalcompra=a*b
recargo=0
descuento2=0

if a<5:
    descuento=totalcompra*0.07
elif(a>=5 and a<10):
    descuento=totalcompra*0.25
else:
    descuento=totalcompra*0.45


if (c=="tarjeta"):
    recargo=totalcompra*0.1
else:
    descuento2=totalcompra*0.15
pago=totalcompra-descuento+descuento2+recargo
print("total a pagar $:"+str(pago))


    

