print ("Ingrese los lados del triangulo")
a=float(input("lado 1:"))
b=float(input("lado 2:"))
c=float(input("lado 3:"))

if (a==b and b==c):
    print("el triangulo es equilatero")
elif (a!=b and b!=c and a!=c):
    print("el triangulo es escaleno")
else:
    ("el triangulo es isosceles")
