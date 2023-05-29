'''
1.	Ingresar las medidas de los lados de un triángulo y 
luego mostrar que tipo de triángulo es según sus lados. 
Será equilátero si todas las medidas son iguales. 
Será escaleno si todas las medidas son distintas y 
será isósceles si sólo dos medidas son iguales.
'''
print("Ingrese las medidas del triángulo")
a=float(input("Lado1: "))
b=float(input("Lado2: "))
c=float(input("Lado3: "))
if(a==b and b==c and a==c):
    print("El triángulo es equilatero")
elif(a!=b and b!=c and a!=c):
    print("El triángulo es escaleno")
else:
    print("El triángulo es isósceles")