# 🍕 Sistema de Pedidos de Pizza con Patrones de Diseño

Este proyecto es una implementación educativa en Python que demuestra el uso de tres Patrones de Diseño clave (Creacional, Estructural y Comportamental) aplicados a un sistema básico de pedidos de pizza.

## 🌟 Patrones de Diseño Implementados

El código ejemplifica cómo los patrones pueden resolver problemas comunes de arquitectura de software, mejorando la **flexibilidad**, **escalabilidad** y el **mantenimiento** del sistema.

### 1. 🏗️ Factory Method (Creacional)

* **Propósito:** Encapsula la lógica de creación de objetos. Permite crear instancias de varios tipos de productos sin exponer la lógica de instanciación al código cliente.
* **Aplicación:** La clase `PizzaFactory` se encarga de instanciar las diferentes clases de pizzas (`PizzaMargarita`, `PizzaPeperoni`) basándose en un parámetro simple (`tipo`). Esto desacopla el cliente de las clases concretas.

### 2. 🧩 Decorator (Estructural)

* **Propósito:** Agrega responsabilidades o funcionalidades adicionales a un objeto de forma dinámica y transparente, sin modificar su estructura original (como una alternativa flexible a la herencia).
* **Aplicación:** Las clases `QuesoExtra` y `BordeRelleno` son decoradores que envuelven el objeto `Pizza` base. Esto permite añadir ingredientes y actualizar dinámicamente tanto la **descripción** como el **costo total** del pedido, sin tener que crear una subclase para cada combinación de ingredientes.

### 3. 📢 Observer (Comportamiento)

* **Propósito:** Define una dependencia uno-a-muchos entre objetos para que, cuando un objeto (el Sujeto) cambia de estado, todos sus dependientes (los Observadores) sean notificados y actualizados automáticamente.
* **Aplicación:** La clase `Cocina` actúa como el **Sujeto** (observable) y la clase `Cliente` como el **Observador**. Cuando el estado del pedido en la cocina cambia (`set_estado_pedido`), todos los clientes suscritos son notificados instantáneamente sobre el progreso de su pizza.

---

## 🛠️ Estructura del Proyecto

El proyecto está contenido en un único archivo Python (`pizzas_patrones.py`) y sigue la siguiente estructura de clases:

| Clase / Interfaz | Rol en el Patrón | Descripción |
| :--- | :--- | :--- |
| `Pizza` | Producto/Componente (Factory/Decorator) | Interfaz base para todas las pizzas e ingredientes. |
| `PizzaMargarita`, `PizzaPeperoni` | Productos Concretos (Factory) | Implementaciones de la pizza base. |
| `PizzaFactory` | Creador (Factory) | Clase estática que crea la pizza base solicitada. |
| `IngredienteDecorador` | Decorador Abstracto (Decorator) | Hereda de `Pizza` y envuelve la instancia de pizza. |
| `QuesoExtra`, `BordeRelleno` | Decoradores Concretos (Decorator) | Añaden costo y descripción al pedido. |
| `Observador` | Interfaz Observador (Observer) | Define el método `actualizar()`. |
| `Cocina` | Sujeto (Observer) | Mantiene la lista de observadores y notifica cambios de estado. |
| `Cliente` | Observador Concreto (Observer) | Recibe las notificaciones sobre el estado del pedido. |



### Diagrama de Clases (Representación Simplificada)

Esta representación ASCII muestra las relaciones clave entre las clases.

#### Factory Method
+---------------+ +-------------------+ | <<Abstract>> |<-----| PizzaFactory | | Pizza |<-----| (Método estático) | +---------------+ +-------------------+ ^ | Implements +------------------+ | | +-------------------+ +--------------------+ | PizzaMargarita | | PizzaPeperoni | +-------------------+ +--------------------+


#### Decorator


[Image of Decorator pattern structure]

+---------------+ (Decorado) | <<Abstract>> |<------ (Envuelve) | Pizza |<--+ +---------------+ | ^ | | Implements | +-----------------------+ +-------------------+ | <<Abstract>> |<--| QuesoExtra | | IngredienteDecorador | +-------------------+ +-----------------------+ +-------------------+ | BordeRelleno | +-------------------+
#### Observer
+-------------------+ +-------------------+ | <<Abstract>> | | Sujeto | | Observador |<-------| Cocina | +-------------------+ +-------------------+ ^ | | Implements | Notifies | v +--------------+ +-------------------+ | Cliente | | Lista de Observadores | +--------------+ +-------------------+

---

## 💻 Tecnologías Utilizadas

| Tecnología | Versión | Descripción |
| :--- | :--- | :--- |
| **Python** | 3.x | Lenguaje de programación principal utilizado. |
| **abc** | Estándar | Módulo para definir Clases Base Abstractas. |
| **`README.md`** | N/A | Documentación escrita en formato Markdown. |

---

## 🚀 Cómo Ejecutar el Proyecto

### Requisitos

* [**Python 3.x**](https://www.python.org/downloads/)

### Instrucciones

1.  Guarda el código fuente en un archivo llamado `pizzas_patrones.py`.
2.  Abre tu terminal o línea de comandos.
3.  Navega hasta el directorio donde guardaste el archivo.
4.  Ejecuta el script con el siguiente comando:

    ```bash
    python pizzas_patrones.py
    ```

### Salida Esperada

Al ejecutar el script, la función `main()` demostrará secuencialmente el uso de los tres patrones:
=== SISTEMA DE PEDIDOS DE PIZZA CON PATRONES DE DISEÑO ===

Pedido base creado: Pizza Peperoni | Costo: 60.0

Pedido final (decorado): Pizza Peperoni, con Queso Extra, con Borde Relleno Costo Total a Pagar: 85.0

--- ESTADO ACTUALIZADO: En preparación --- Notificación para Juan Perez: Tu pedido está ahora En preparación.

--- ESTADO ACTUALIZADO: En el horno --- Notificación para Juan Perez: Tu pedido está ahora En el horno.

--- ESTADO ACTUALIZADO: Listo para entregar --- Notificación para Juan Perez: Tu pedido está ahora Listo para entregar.

---

## ✍️ Contribución

Siéntete libre de clonar este repositorio, experimentar con el código o añadir más patrones de diseño (como un **Builder** para pedidos complejos o un **Strategy** para diferentes métodos de pago).

1.  Haz un *fork* del repositorio.
2.  Crea una nueva rama (`git checkout -b feature/nueva-funcionalidad`).
3.  Realiza tus cambios y *commitea* (`git commit -am 'Add new feature'`).
4.  Sube tus cambios (`git push origin feature/nueva-funcionalidad`).
5.  Abre un **Pull Request**.

---

## 📄 Licencia

Este proyecto está bajo la Licencia MIT.
