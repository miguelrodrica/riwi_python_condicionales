libro = 25000
desc_estud = 0.85

estudiante = input("¿El comprado es estudiante? ").lower()

if estudiante == "si":
    pay1 = libro * desc_estud
    conf_cupon = input("¿El comprador cuenta con un cupón de descuento adicional? ").lower()

    if conf_cupon == "si":
        cupon = input("Escriba el código del cupón correspondiente: ").lower()

        if cupon == "libro10":
            pay2 = pay1 *0.9
            print(f"El cliente debe pagar {pay2}.")
        else:
            print(f"El cliente debe pagar {pay1}.")
    else:
        print(f"El cliente debe pagar {pay1}.")
else:
    print(f"El cliente debe pagar {libro}.")
