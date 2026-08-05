continuar = True
energia = 0

while continuar:
    dias = int(input("¿Cuántos días entrenó esta semana? "))

    if dias >= 4:
        print("¡Excelente disciplina! Ganas 1 punto de energía")
        energia = energia+1

    if dias == 2 or dias == 3:
        print("Bien, pero puedes dar más")

    if dias == 0 or dias == 1:
        print("No aflojes, tú puedes mejorar")

    print(f"Actualmente tienes {energia} puntos de energia")

    continuar = False
