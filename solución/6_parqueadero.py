pay_hora = 2000
multa = 5000
horas = int(input("¿Cuántas horas usó el parqueadero? "))

if horas >=0 and horas <= 5:
    pay1 = pay_hora * horas
    print(f"El cliente debe pagar {pay1}")

if horas > 5:
    pay2 = (pay_hora * horas) + multa
    print(f"El cliente debe pagar {pay2}")
