

cantidad_numeros=int(input("ingrese la cantidad de numeros: "))
contador=0
cantidad_pares=0
suma_positivos=0
contador_impare=0
promedio_impare=0


while contador < cantidad_numeros:
    
    numero_entero=int(input("Ingrese un numero entero: "))
    contador+=1
    
    if numero_entero %2 == 0:
        cantidad_pares+=1
    else:
          
        contador_impare+=1
        promedio_impare= (promedio_impare+ numero_entero)
        
    
    if numero_entero > 0:
        suma_positivos= suma_positivos + numero_entero
        

total_impare=promedio_impare/contador_impare
        

print("La cantidad de numeros pares ingresados es igual a: ", cantidad_pares)
print("La suma de los numeros positivos es igual a: ", suma_positivos)
print("El promedio de los numeros impares es: ", total_impare)


        
        
        



        
    