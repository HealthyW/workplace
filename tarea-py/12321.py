while True:
    try:
        a=int(input("Ingrese un numero entre 103 y 987: "))
        if (a>0) and a >102 and a<988:
            break
        else:
            print("\tIngrese un digito valido")
    except ValueError:
        print("\tIngrese un digito valido")



if a>0 and a in range(103,988):
    x=a//10 # x equivale a 12
    a=a/10  # a equivale a 12.3
    b=a-x   # b equivale a 0.3
    c=b*10  # c equivale 3, por lo tanto z es el tercer numero (ejemplo: 123, 12->3<-)
    
    y=x//10 # y equivale a 1
    x=x/10  # x equivale a 1.2
    d=x-y   # d equivale a 0.2
    e=d*10  # f equivale a 2
    
    z=y//10 #z equivale a 0
    y=y/10  #y equivale a 0.1
    f=y-z   #f equivale a 0.1
    g=f*10  #g equivale a 1
    
    final=c*10  #final equivale a 30
    final2=final+e #final2 equivale a 32
    final3=final2*10    #final 3 equivale a 320
    end=final3+g    #end equivale a 321     
                    #tambien funciona como (((c * 10)+e) * 10)+g0
    print(("\t"),round(end))


