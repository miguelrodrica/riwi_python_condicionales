# User Stories - Actividad 2 (Reconstruidas desde las soluciones)

A continuación se presentan historias de usuario y criterios de aceptación deducidos a partir del comportamiento implementado en cada ejercicio.

---

## Ejercicio 1 — Panadería con descuentos

**Historia de usuario**  
Como cajero de una panadería, quiero calcular automáticamente el total de una compra de panes según la cantidad, para aplicar descuentos por volumen y mostrar el ahorro al cliente.

**Criterios de aceptación**
- Dado un precio unitario de pan, cuando la cantidad es válida y está en rango bajo, se cobra sin descuento.
- Cuando la cantidad supera el primer umbral, se aplica 10% de descuento.
- Cuando la cantidad supera el segundo umbral, se aplica 20% de descuento.
- Si la cantidad es menor o igual a 0, se informa que es inválida.
- El sistema pregunta si se desea registrar otra compra.

---

## Ejercicio 2 — Entrada por edades

**Historia de usuario**  
Como encargado de boletería, quiero asignar el precio de entrada según la edad del cliente, para cobrar la tarifa correcta por categoría.

**Criterios de aceptación**
- Menores de 5 años ingresan gratis.
- Entre 5 y 11 años pagan tarifa infantil.
- Entre 12 y 59 años pagan tarifa general.
- Mayores o iguales a 60 años pagan tarifa preferencial.
- Si la edad es negativa, se informa valor inválido.
- Se puede continuar registrando clientes hasta que se indique salida.

---

## Ejercicio 3 — Progreso de entrenamiento

**Historia de usuario**  
Como usuario de una app de hábitos, quiero recibir retroalimentación según cuántos días entrené en la semana, para medir mi disciplina.

**Criterios de aceptación**
- Si entrenó 4 o más días, recibe felicitación y gana 1 punto de energía.
- Si entrenó 2 o 3 días, recibe mensaje de motivación intermedia.
- Si entrenó 0 o 1 día, recibe mensaje para mejorar.
- Siempre se muestra el total actual de puntos de energía.

---

## Ejercicio 4 — Pedido de helado

**Historia de usuario**  
Como vendedor de heladería, quiero registrar sabor y topping del helado para calcular correctamente el total del pedido.

**Criterios de aceptación**
- Se permite elegir entre sabores disponibles (chocolate o vainilla).
- Se puede agregar topping con costo adicional fijo.
- El precio final cambia según sabor y selección de topping.
- Si el sabor no está disponible, se informa y se solicita nuevo intento.

---

## Ejercicio 5 — Venta de libros con beneficios

**Historia de usuario**  
Como cajero de librería, quiero aplicar descuentos por perfil de estudiante y por cupón para cobrar el valor final correcto.

**Criterios de aceptación**
- Si el comprador es estudiante, recibe descuento base.
- Si además tiene cupón y el código es válido, recibe descuento adicional.
- Si el cupón no es válido, solo aplica descuento base de estudiante.
- Si no es estudiante, paga precio completo.

---

## Ejercicio 6 — Cobro de parqueadero

**Historia de usuario**  
Como operador de parqueadero, quiero cobrar por horas de uso y aplicar multa al superar el tiempo permitido, para liquidar correctamente el servicio.

**Criterios de aceptación**
- Se calcula cobro por hora para estancias dentro del rango permitido.
- Si las horas exceden el límite, se suma una multa fija.
- Se muestra el total a pagar.

---

## Ejercicio 7 — Facturación de almuerzos y bebidas

**Historia de usuario**  
Como administrador de restaurante, quiero calcular la cuenta según cantidad de almuerzos, bebidas opcionales e impuesto, para entregar el total final al cliente.

**Criterios de aceptación**
- Se calcula subtotal por cantidad de almuerzos.
- Si el cliente agrega bebidas, se suma su costo al subtotal.
- Al subtotal final se aplica un recargo/impuesto porcentual.
- Se muestra total a pagar.

---

## Ejercicio 8 — Evaluación ponderada

**Historia de usuario**  
Como docente/reclutador, quiero obtener una nota final ponderada con dos pruebas, para clasificar el resultado del evaluado.

**Criterios de aceptación**
- La prueba técnica pesa 70%.
- La prueba lógica pesa 30%.
- Con base en la nota final:
  - Aprobado en rango superior.
  - Revisión en rango intermedio.
  - Reprobado en rango bajo.
- Si el dato sale de rango esperado, se informa inconsistencia.

---

## Ejercicio 9 — Descuentos por volumen y envío

**Historia de usuario**  
Como sistema de tienda, quiero aplicar descuentos por cantidad comprada y luego evaluar costo de envío, para calcular el pago total del cliente.

**Criterios de aceptación**
- Si la cantidad alcanza umbral alto, se aplica descuento mayor.
- Si la cantidad está en umbral medio, se aplica descuento menor.
- Si no alcanza umbral, se cobra sin descuento.
- Si el total queda por debajo del mínimo de despacho, se agrega costo fijo de envío.
- Se muestra total final.

---

## Ejercicio 10 — Validación de acceso

**Historia de usuario**  
Como controlador de acceso, quiero permitir entrada solo a personas mayores de edad que presenten documento, para cumplir requisitos de seguridad.

**Criterios de aceptación**
- Si la persona tiene 18 o más y presenta documento, puede ingresar.
- Si es menor de edad, acceso denegado.
- Si es mayor de edad pero no presenta documento, se solicita documento.

---

## Nota de reconstrucción

Estas historias fueron **reconstruidas** a partir de las soluciones implementadas en los archivos `.py`, para reemplazar el planteamiento original extraviado.
