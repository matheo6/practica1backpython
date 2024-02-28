from calculadora import * 

option = input("""
Seleccione una operación
1. Suma 
2. Resta
3. Division
""")
a= input("ingrese el primer numero ")
b= input("ingrese el segundo numero ")

try:
    option = int(option)
    a= int(a)
    b=int(b)
except:
    print ("valor no valido")

if option not in [1,2,3]:
    print ("Valor no valido")
    exit()

if option== 1:
    print(suma(a,b))
elif option == 2:
    print(resta(a,b))
else :
    print(division(a,b))

