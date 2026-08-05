continuar = True

while continuar:
    edad = int(input("Escriba la edad del cliente: "))

    if edad < 5:
        print("El ingreso es gratuito.")
    
    if edad >= 5 and edad <= 11:
        print("El precio de la entrada es $5.000")

    if edad >= 12 and edad <= 59:
        print("El precio de la entrada es $8.000")

    if edad >= 60:
        print("El precio de la entrada es $4.000")

    if edad < 0:
        print("Número inválido, intente nuevamente.")

    salir = int(input("¿Desea seguir comprando? 1=Si o 2=No"))
    if salir == 2:      
        continuar = False
