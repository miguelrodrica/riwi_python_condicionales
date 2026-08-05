tecnica = float(input("Ingrese la nota de su prueba técnica: "))
logica = float(input("Ingrese la nota de su prueba lógica: "))

nota_final = (tecnica * 0.7) + (logica * 0.3)

if nota_final >= 3 and nota_final <= 5:
    print(f"Su nota final es {nota_final}, ¡APROBADO!")
elif nota_final >=2 and nota_final < 3:
    print(f"Su nota final es {nota_final}. Está en proceso de Revisión.")
elif nota_final < 2:
    print(f"Su nota final es {nota_final}. Reprobado.")
else:
    print("Datos errados.")
