#Ejercicio 15
print ("A continuación usted deberá ingresar cuatro números distintos")
a=int(input("Por favor, ingrese el primer número "))
b=int(input("Por favor, ingrese el segundo número "))
c=int(input("Por favor, ingrese el tercer número "))
d=int(input("Por favor, ingrese el cuarto número "))

if (a<=b) and (a<=c) and (a<=d):
    print (a)
    if (b<=c) and (b<=d):
        print (b)
        if (c<=d):
            print (c)
            print (d)
        else: 
            print (d)
            print (c)
    if (c<=b) and (c<=d):
        print (c)
        if (b<=d):
            print (b)
            print (d)
        else: 
            print (d)
            print (b)
    if (d<=b) and (d<=c):
        print (d)
        if (b<=c):
            print (b)
            print (c)
        else: 
            print (c)
            print (b)
        

if (b<=a) and (b<=c) and (b<=d):
    print (b)
    if (a<=c) and (a<=d):
        print (a)
        if (c<=d):
            print (c)
            print (d)
        else: 
            print (d)
            print (c)
    if (c<=a) and (c<=d):
        print (c)
        if (a<=d):
            print (a)
            print (d)
        else: 
            print (d)
            print (a)
    if (d<=a) and (d<=c):
        print (d)
        if (a<=c):
            print (a)
            print (c)
        else: 
            print (c)
            print (a)

if (c<=a) and (c<=b) and (c<=d):
    print (c)
    if (a<=b) and (a<=d):
        print (a)
        if (b<=d):
            print (b)
            print (d)
        else: 
            print (d)
            print (b)
    if (b<=a) and (b<=d):
        print (b)
        if (a<=d):
            print (a)
            print (d)
        else: 
            print (d)
            print (a)
    if (d<=a) and (d<=b):
        print (d)
        if (a<=b):
            print (a)
            print (b)
        else: 
            print (b)
            print (a)
    

if (d<=a) and (d<=b) and (d<=c):
    print (d)
    if (a<=b) and (a<=c):
        print (a)
        if (b<=c):
            print (b)
            print (c)
        else: 
            print (c)
            print (b)
    if (b<=a) and (b<=c):
        print (b)
        if (a<=c):
            print (a)
            print (c)
        else: 
            print (c)
            print (a)
    if (c<=a) and (c<=b):
        print (c)
        if (a<=b):
            print (a)
            print (b)
        else: 
            print (b)
            print (a)
