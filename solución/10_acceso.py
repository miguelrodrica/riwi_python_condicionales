edad = int(input("Ingrese su edad: "))
documento = input("Ingrese el número de su documento de identidad: ")

if edad >= 18 and documento != "":
    print("Bienvenido, puede ingresar.")
elif edad < 18:
    print("Acceso denegado.")
elif edad >= 18 and documento == "":
    print("Debe presentar su documento.")
