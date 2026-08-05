pedido = ""
chocolate = 4000
vainilla = 3500
topping = 1000
continuar = True

while continuar:
    print("LISTA DE SABORES DE HELADO")
    print("C = Cholocate")
    print("V = Vainilla")
    pedido = input("¿Qué sabor desea? ").lower()

    if pedido == "c" or pedido == "v":
        agregar = int(input("¿Desea agregar un topping? 1=Si o 2=No "))
        if agregar == 1 and pedido == "c":
            precio_final = chocolate + topping
            print(f"Usted compró helado de cholote y un topping, el precio final es {precio_final}.")
        if agregar == 2 and pedido == "c":
            print(f"Usted compró helado de cholote, el precio final es {chocolate}.")
        if agregar == 1 and pedido == "v":
            precio_final = vainilla + topping
            print(f"Usted compró helado de vainilla y un topping, el precio final es {precio_final}.")
        if agregar == 2 and pedido == "v":
            print(f"Usted compró helado de vainilla, el precio final es {vainilla}.")              

    elif pedido != "c" or pedido != "v":
            print("Sabor no disponible, elija nuevamente.")
            print("")
            continue
    
    continuar = False
