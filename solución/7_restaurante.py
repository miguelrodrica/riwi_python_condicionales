precio_menu = 12000
precio_bebida = 3000

cant_menu = int(input("¿Cuántos almuerzos compró? "))
bebida = input("¿Desea agregar bebidas? ").lower()

if bebida == "si":
    cant_bebida = int(input("¿Cuántas bebidas desea agregar? "))
    pay1 = ((precio_menu * cant_menu) + (precio_bebida * cant_bebida)) * 1.08
    print(f"El cliente debe pagar {pay1}")
else:
    pay2 = (precio_menu * cant_menu) * 1.08
    print(f"El cliente debe pagar {pay2}")
