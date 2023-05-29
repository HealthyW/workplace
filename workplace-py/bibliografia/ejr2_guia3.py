cantComp=int(input("Cantidad de computadores: "))
precio=int(input("Precio del computador: "))
forma=input("Forma de pago: Efectivo o tarjeta ").lower()
totalCompra=cantComp*precio
recargo=0
desc2=0
if(cantComp<5):
    desc1=totalCompra*0.07
elif(cantComp>=5 and cantComp<10):
    desc1=totalCompra*0.25
else:
    desc1=totalCompra*0.45
if(forma=="tarjeta"):
    recargo=totalCompra*0.1
else:
    desc2=totalCompra*0.15
pago=totalCompra-desc1-desc2+recargo
print("Total a pagar $"+str(pago))
