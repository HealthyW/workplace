
import math

print("Ingrese las notas del alumno")
nota1=float(input("Primera prueba: "))
nota2=float(input("Segunda prueba: "))
nota3=float(input("Terecera prueba: "))

nota1= nota1*0.25
nota2= nota2*0.35
nota3= nota3*0.4

notafinal = float(nota1+nota2+nota3)

print("Su nota de presentacion es: " +str(round(notafinal, 1)))
