# User Stories – Actividad de Condicionales y Ciclos en Python

## Objetivo general
Diseñar y resolver problemas cotidianos mediante scripts en Python que utilicen condicionales (`if`, `elif`, `else`), bucles (`while`) y validaciones, simulando situaciones reales de venta, control y toma de decisiones. Cada ejercicio representa un caso independiente en el que se espera del estudiante:
- Interpretar y plantear un flujo lógico de solución.
- Desarrollar validaciones y manejar entradas de usuario.
- Calcular resultados aplicando reglas de negocio concretas.
- Presentar salidas claras y responder adecuadamente a errores o entradas inválidas.

---

## User Stories por ejercicio

### Ejercicio 1 — Panadería: cálculo y descuentos por volumen
**Historia de usuario**  
Como cajero de una panadería, quiero calcular el total de una compra de panes y aplicar descuentos según la cantidad comprada, para ofrecer automáticamente el mejor precio al cliente y mostrarle su ahorro.

**Criterios de aceptación**
- El sistema solicita la cantidad de panes y repite el ciclo mientras el usuario lo desee.
- Si la cantidad es mayor a cero y hasta 20 panes, se cobra precio normal.
- De 21 a 49 panes, se aplica un 10% de descuento sobre el total.
- Para 50 o más panes, se aplica un 20% de descuento.
- Si la cantidad ingresada es menor o igual a cero, muestra mensaje de error y vuelve a solicitar el dato.
- Muestra claramente el precio total y el ahorro si corresponde.

---

### Ejercicio 2 — Taquilla: precio de entrada según edad
**Historia de usuario**  
Como responsable de taquilla, quiero asignar el precio de entrada según la edad del cliente, de forma que cada visitante pague la tarifa correspondiente y se controle el acceso adecuadamente.

**Criterios de aceptación**
- Solicita la edad y permite registrar varios clientes en ciclo.
- Menores de 5 años ingresan gratis.
- De 5 a 11 años: tarifa reducida.
- De 12 a 59 años: tarifa estándar.
- Mayores de 60 años: tarifa preferencial.
- Si la edad ingresada es negativa, informa ingreso inválido.
- Permite terminar el registro a decisión del usuario.

---

### Ejercicio 3 — Seguimiento de entrenamiento semanal
**Historia de usuario**  
Como usuario interesado en mantener disciplina de entrenamiento, quiero ingresar los días entrenados en la semana y recibir retroalimentación positiva o motivacional, junto con una acumulación de puntos de energía.

**Criterios de aceptación**
- Solicita la cantidad de días y muestra el mensaje adecuado:
  - Si entrenó 4 o más días: felicitación y suma 1 punto de energía.
  - Si entrenó 2 o 3 días: mensaje de ánimo.
  - Si entrenó 0 o 1 día: mensaje de mejora.
- Siempre muestra el total de puntos de energía actuales.
- Permite una sola iteración por defecto.

---

### Ejercicio 4 — Heladería: selección de sabor y topping
**Historia de usuario**  
Como vendedor de helados, quiero registrar el sabor elegido y si desea topping para calcular el precio final del pedido.

**Criterios de aceptación**
- Ofrece al menos dos sabores (chocolate, vainilla).
- Permite agregar topping opcional con costo extra.
- El precio varía según la combinación seleccionada.
- Si elige un sabor no disponible, informa error y repite solicitud.

---

### Ejercicio 5 — Librería: descuentos por perfil y cupón
**Historia de usuario**  
Como cajero, quiero aplicar descuentos a estudiantes y permitir el uso de un cupón válido para ofrecer el mejor precio posible en la compra de libros.

**Criterios de aceptación**
- Pregunta si el comprador es estudiante para aplicar descuento base.
- Si es estudiante y tiene cupón válido, suma un descuento adicional (requiere validación de código).
- Si el cupón no es válido, sólo aplica el descuento de estudiante.
- Si no es estudiante, cobra el precio completo del libro.
- Siempre muestra el valor a pagar.

---

### Ejercicio 6 — Parqueadero: cobro regular y multa
**Historia de usuario**  
Como operador de parqueadero, quiero calcular el pago por hora utilizada y sumar una multa si se pasan del límite permitido, para cobrar de forma correcta y transparente al cliente.

**Criterios de aceptación**
- Solicita la cantidad de horas usadas.
- Hasta 5 horas: cobra tarifa estándar por hora.
- Más de 5 horas: cobra tarifa estándar multiplicada por horas más una multa fija.
- Muestra siempre el monto total a pagar.

---

### Ejercicio 7 — Restaurante: cuenta con bebidas e impuesto
**Historia de usuario**  
Como administrador de restaurante, quiero calcular la cuenta total considerando almuerzos, posibles bebidas adicionales e impuesto, para entregar el cobro correcto al cliente.

**Criterios de aceptación**
- Solicita la cantidad de menús y si desea bebidas.
- Si elige bebidas, solicita cantidad y las suma al subtotal.
- Aplica un recargo del 8% (impuesto) al total.
- Muestra el total final a pagar.

---

### Ejercicio 8 — Evaluación: nota ponderada
**Historia de usuario**  
Como docente/reclutador, quiero calcular la nota final ponderada a partir de una prueba técnica y una lógica, para clasificar a la persona en aprobado, revisión o reprobado.

**Criterios de aceptación**
- Solicita la nota de ambas pruebas.
- Calcula nota final: técnica (70%) + lógica (30%).
- Si la nota está en 3 a 5: aprobado.
- Si la nota está en 2 a <3: proceso de revisión.
- Si la nota es menor a 2: reprobado.
- Si se ingresan datos fuera de rango esperado, informa datos errados.

---

### Ejercicio 9 — Tienda: descuentos y envío mínimo
**Historia de usuario**  
Como sistema de venta, quiero aplicar descuentos por cantidad y evaluar si corresponde sumar costo fijo de envío, para garantizar una facturación adecuada y transparente.

**Criterios de aceptación**
- Solicita cantidad comprada.
- 30 o más: aplica mayor descuento (15%).
- 10 a 29: descuento intermedio (5%).
- Menos de 10: sin descuento.
- Si el total queda por debajo de cierto umbral, se suma costo fijo de envío.
- Siempre comunica el monto final discriminando descuentos y recargos.

---

### Ejercicio 10 — Acceso por edad y documento
**Historia de usuario**  
Como controlador de acceso, quiero permitir solamente la entrada a personas mayores de edad con documento válido, de modo que se cumpla el control de seguridad.

**Criterios de aceptación**
- Solicita edad y documento.
- Si la persona es mayor de edad y presenta documento, permite ingreso.
- Si es menor de edad, niega acceso.
- Si es mayor pero no presenta documento, solicita que lo presente.
- Responde siempre con mensaje de acuerdo a cada situación.

---