# Actividad de Condicionales y Ciclos en Python

Este repositorio contiene la **solución a 10 retos progresivos** desarrollados como parte del curso *Desarrollo de Software Web & Analítica de Datos* de **Riwi**, en el **Módulo 1: Fundamentos de Programación con Python**.

---

## Descripción general
El objetivo principal de la actividad es afianzar las habilidades en la construcción de programas con Python, enfocados en la toma de decisiones mediante condicionales (`if`, `elif`, `else`), validación de entradas, uso de ciclos (`while`) y aplicación de reglas de negocio sencillas en contextos realistas.

Cada reto modela un escenario diferente, desde ventas con descuentos y control de acceso hasta operaciones de restaurante, evaluaciones o gimnasios. Se espera que el estudiante analice el caso y construya el flujo más lógico y robusto posible.

---

## Estructura del repositorio

```
solución/
│ 1_panadería.py
│ 2_taquilla.py
│ 3_entrenamiento.py
│ 4_heladería.py
│ 5_librería.py
│ 6_parqueadero.py
│ 7_restaurante.py
│ 8_docente.py
│ 9_tienda.py
│ 10_acceso.py
userstory.md
README.md
```

---

## Ejercicios incluidos

### 1. Panadería: descuentos por volumen
- Calcula costo según cantidad, con descuentos escalonados y validaciones.

### 2. Taquilla: precio según edad
- Determina cobro de entrada por edad, manejo de rangos y control de registro.

### 3. Entrenamiento: disciplina semanal
- Valora días de ejercicio, entrega retroalimentación y suma puntos de energía.

### 4. Heladería: sabor y topping
- Permite escoger entre varios sabores y si se agrega topping, validando todo ingreso.

### 5. Librería: descuentos y cupones
- Aplica descuentos para estudiantes y/o por cupón (requiere código válido).

### 6. Parqueadero: cobro y multa
- Cobro estándar por hora y multa al exceder límite, calculando el monto exacto.

### 7. Restaurante: menú, bebidas e impuesto
- Suma precios según cantidades y aplica recargo/impuesto final.

### 8. Evaluación: nota ponderada
- Calcula promedio ponderado de dos pruebas y clasifica el resultado acorde.

### 9. Tienda: descuentos y envío mínimo
- Aplica descuentos por volumen y costo de envío si no se alcanza un umbral.

### 10. Acceso: control por edad y documento
- Permite o rechaza acceso según edad y presencia de documento.

---

## ¿Cómo ejecutar los ejercicios?

Requisitos previos:
- Tener Python 3 instalado.

Pasos sugeridos:

1. Clona este repositorio:
   ```bash
   git clone https://github.com/miguelrodrica/riwi_python_condicionales.git
   cd riwi_python_condicionales
   ```
2. Ve a la carpeta de soluciones:
   ```bash
   cd solución
   ```
3. Ejecuta el archivo del reto que quieras probar, por ejemplo:
   ```bash
   python 1_panadería.py
   # O bien: python3 1_panadería.py
   ```
---

## Notas y recomendaciones
- El archivo `userstory.md` incluye la descripción detallada de cada reto y sus reglas de negocio.
- Los scripts están preparados para pruebas manuales y uso en terminal.
- Utiliza siempre validaciones y sigue el flujo propuesto para practicar buenas prácticas.
- Este proyecto es de uso académico y libre adaptación, respaldando buenas bases en programación estructurada.

---

### Autoría y licencia
Desarrollado para la formación práctica en el marco del curso Riwi. Uso, copia y adaptación permitidos con fines educativos y de aprendizaje.
