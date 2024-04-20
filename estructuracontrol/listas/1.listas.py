

"""closet = ["pantalon","camisas", "harina pan"]
#closet =     0           1        2

print(closet[0])"""


netflix= ["Batman","Simon","Ley de los audaces"]


running = True

while running:

    print("1.Añadir\n2.ver listas\n3.Borrar elemento\n4.Salir\n")

    opcion=int(input("Añade una pelicula: "))

    if opcion == 1: 
       pelicula=input("Añade una pelicula: ")
       netflix.append(pelicula)

    if opcion == 2:
        print(netflix)

    if opcion == 3: 
        indice= int(input("ingrese el numero que desa borrar")) 
        netflix.pop(indice)

    if opcion == 4:
        print("Vuelva pronto")
        running = False

    print("\n")

 


