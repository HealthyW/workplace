
print("++++++++++++++++++++++++")
print("   [C]:Corriente")
print("   [S]:Sesamo")
print("   [F]:Frica")
print("   [M]:Molde")
print("++++++++++++++++++++++++")

pan=input("¿Que tipo de pan desea?: ").lower()
print(" Efectivo/Tarjeta")
tipo_pago=input("¿Que tipo de pago realizara?: ").lower()
kilos=float(input("¿Cuanto kilo de pan va a llevar?: "))
precio_kilo=1000
total=0
descuento=0

if tipo_pago=="tarjeta":
    if pan=="c":
        descuento=0
        total=(precio_kilo*kilos)
    if pan=="s":
        descuento=10
        total=(precio_kilo*kilos)*0.9
    if pan=="f":
        descuento=15
        total=(precio_kilo*kilos)*0.85
    if pan=="m":
        descuento=8
        total=(precio_kilo*kilos)*0.92

if tipo_pago=="efectivo":
    if pan=="c":
        descuento=7
        total=(precio_kilo*kilos)*0.93
    if pan=="s":
        descuento=17
        total=(precio_kilo*kilos)*0.83
    if pan=="f":
        descuento=22
        total=(precio_kilo*kilos)*0.78
    if pan=="m":
        descuento=15
        total=(precio_kilo*kilos)*0.85

print("++++++++++++++++++++++++++++++++++++++++++++++++")
print("     Cantidad de kilos comprados:", kilos)
if pan=="c":
    print("     Tipo de pan: Corriente")
if pan=="s":
    print("     Tipo de pan: Sesamo")
if pan=="f":
    print("     Tipo de pan: Frica")
if pan=="m":
    print("     Tipo de pan: Molde")
print("     Total descuento: ", descuento, "%")
print("     Total a pagar: ", total)

print("++++++++++++++++++++++++++++++++++++++++++++++++")



