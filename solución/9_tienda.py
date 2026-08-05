precio_producto = 2000

cantidad = int(input("¿Cuántos productos compró? "))

if cantidad >= 30:
    pay1 = (cantidad * precio_producto) * 0.85
elif cantidad >= 10 and cantidad < 30:
    pay1 = (cantidad * precio_producto) * 0.95
else:
    pay1 = cantidad * precio_producto

if pay1 < 50000:
    pay2 = pay1 + 5000
    print(f"El cliente debe pagar {pay2}")
else:
    print(f"El cliente debe pagar {pay1}")
