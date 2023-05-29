'''
1.	Ingresar N números enteros y luego mostrar:
•	Cantidad de números pares ingresados
•	Suma de los números positivos
•	Promedio de los números impares ingresados
'''

while True:
    try:
        a=int(input("Ingrese N numeros: "))
        break
    except ValueError:
        print("\tIngrese N numeros, porfavor")

cont=0
cont_par=0
suma_par=0
cont_impar=0
impar=0
promedio=0


while cont<a:
    cont+=1
    while True:
        try:
            b=int(input("Ingrese Numero: "))
            break
        except ValueError:
            print("\tIngrese un Numero, porfavor~~")
    if b%2==0:
        cont_par+=1
    if b>0:
        suma_par=b+suma_par
    if b%2!=0:
        cont_impar+=1
        impar=impar+b
        promedio=impar/cont_impar



print("+++++++++++++++++++++++++++++++++++++++++++++++++")
print("     Cantidad de numeros pares ingresados: ", cont_par)
print("     Suma de los numeros positivos: ", suma_par)
print("     Promedio de los numeros impares ingresados: ", promedio)
print("+++++++++++++++++++++++++++++++++++++++++++++++++")