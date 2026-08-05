precio = 300

while True: 
    cantidad = int(input("¿Cuántos panes desea comprar? "))

    if cantidad <= 20 and cantidad > 0:
        costo_total = cantidad * precio
        print(f"Usted compró {cantidad} panes, no tiene descuento. El precio total es {costo_total}.")

    if cantidad > 20 and cantidad < 50:
        costo_total = cantidad * precio
        costo_descuento = costo_total * 0.9
        ahorro = costo_total - costo_descuento
        print(f"Usted compró {cantidad} panes. El precio total es {costo_total}, pero con el descuento del 10% le quedan en {costo_descuento}. Se ahorró {ahorro}.")

    if cantidad > 50:
        costo_total = cantidad * precio
        costo_descuento = costo_total * 0.8
        ahorro = costo_total - costo_descuento
        print(f"Usted compró {cantidad} panes. El precio total es {costo_total}, pero con el descuento del 20% le quedan en {costo_descuento}. Se ahorró {ahorro}.")

    if cantidad <= 0:
        print("Cantidad inválida, intente nuevamente.")
        continue

    continuar = int(input("¿Desea seguir comprando? 1=Si o 2=No"))
    if continuar == 1:      
        continue
    else:
        break
