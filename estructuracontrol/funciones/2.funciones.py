

""" def nombre(nombre):

        print(f"mi nombre es{nombre}")


    name=input("ingresa tu nombre:")


    nombre(nombre)
    
"""


def suma(num1,num2):
   
   resultado =  num1 + num2

   return resultado 

print(suma(1,2))


def resta(num1,num2):
   
   resultado = num1 - num2

   return resultado

print(resta(1,2))
print("\n")
print(resta(2,1))

def matematica(num1,num2):
   
   resultado = (f"{suma(num1,num2)} , {resta(num1,num2)}")

   return resultado

numero1= int(input("ingresa el numero 1:"))
numero2= int(input("ingresa el numero 2:"))

print(f"{suma(numero1,numero2)},{resta(numero1,numero2)}")

print("\n")

print(matematica(numero1,numero2))








