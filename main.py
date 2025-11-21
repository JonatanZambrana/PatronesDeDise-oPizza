from abc import ABC, abstractmethod

# =============================================================================
# 1. PATRÓN CREACIONAL: FACTORY METHOD
# =============================================================================
# Explicación: Se usa para encapsular la lógica de creación de objetos. 
# En lugar de usar 'new Pizza()' directamente, delegamos esa tarea a una Fábrica 
# que decide qué clase concreta instanciar basándose en un parámetro.

# Interfaz base (Producto)
class Pizza(ABC):
    @abstractmethod
    def get_descripcion(self) -> str:
        pass

    @abstractmethod
    def get_costo(self) -> float:
        pass

# Productos Concretos
class PizzaMargarita(Pizza):
    def get_descripcion(self):
        return "Pizza Margarita"
    
    def get_costo(self):
        return 50.00

class PizzaPeperoni(Pizza):
    def get_descripcion(self):
        return "Pizza Peperoni"
    
    def get_costo(self):
        return 60.00

# Creador (La Fábrica)
class PizzaFactory:
    @staticmethod
    def crear_pizza(tipo: str) -> Pizza:
        if tipo.lower() == "margarita":
            return PizzaMargarita()
        elif tipo.lower() == "peperoni":
            return PizzaPeperoni()
        else:
            raise ValueError("Tipo de pizza desconocido")

# =============================================================================
# 2. PATRÓN ESTRUCTURAL: DECORATOR
# =============================================================================
# Explicación: Permite agregar funcionalidades (ingredientes) a un objeto (pizza)
# dinámicamente sin alterar su estructura original. Envuelve la pizza original
# en una capa nueva que añade costo y descripción.

class IngredienteDecorador(Pizza):
    def __init__(self, pizza: Pizza):
        self._pizza = pizza

    @abstractmethod
    def get_descripcion(self):
        pass
    
    @abstractmethod
    def get_costo(self):
        pass

# Decoradores Concretos
class QuesoExtra(IngredienteDecorador):
    def get_descripcion(self):
        return self._pizza.get_descripcion() + ", con Queso Extra"
    
    def get_costo(self):
        return self._pizza.get_costo() + 10.00

class BordeRelleno(IngredienteDecorador):
    def get_descripcion(self):
        return self._pizza.get_descripcion() + ", con Borde Relleno"
    
    def get_costo(self):
        return self._pizza.get_costo() + 15.00

# =============================================================================
# 3. PATRÓN DE COMPORTAMIENTO: OBSERVER
# =============================================================================
# Explicación: Define una dependencia uno-a-muchos. La Cocina (Sujeto) cambia
# de estado y notifica automáticamente a los Clientes (Observadores) suscritos.

# Interfaz Observador
class Observador(ABC):
    @abstractmethod
    def actualizar(self, estado: str):
        pass

# Sujeto (La Cocina)
class Cocina:
    def __init__(self):
        self._observadores = []
        self._estado_pedido = ""

    def agregar_observador(self, observador: Observador):
        self._observadores.append(observador)

    def notificar_observadores(self):
        for obs in self._observadores:
            obs.actualizar(self._estado_pedido)

    def set_estado_pedido(self, nuevo_estado):
        self._estado_pedido = nuevo_estado
        print(f"\n--- ESTADO ACTUALIZADO: {self._estado_pedido} ---")
        self.notificar_observadores()

# Observador Concreto (El Cliente)
class Cliente(Observador):
    def __init__(self, nombre):
        self.nombre = nombre

    def actualizar(self, estado):
        print(f"Notificación para {self.nombre}: Tu pedido está ahora {estado}.")

# =============================================================================
# EJECUCIÓN PRINCIPAL (MAIN)
# =============================================================================
def main():
    print("=== SISTEMA DE PEDIDOS DE PIZZA CON PATRONES DE DISEÑO ===\n")

    # 1. Uso del FACTORY (Creacional)
    # El cliente pide una pizza base sin saber cómo se instancia internamente
    mi_pizza = PizzaFactory.crear_pizza("peperoni")
    print(f"1. Pedido base creado: {mi_pizza.get_descripcion()} | Costo: {mi_pizza.get_costo()}")

    # 2. Uso del DECORATOR (Estructural)
    # El cliente decide agregar queso extra y borde relleno
    mi_pizza = QuesoExtra(mi_pizza)
    mi_pizza = BordeRelleno(mi_pizza)
    
    print(f"2. Pedido final (decorado): {mi_pizza.get_descripcion()}")
    print(f"   Costo Total a Pagar: {mi_pizza.get_costo()}")

    # 3. Uso del OBSERVER (Comportamiento)
    # Configuramos la cocina y el cliente espera su pedido
    cocina = Cocina()
    cliente1 = Cliente("Juan Perez")
    
    # El cliente se suscribe a las notificaciones de la cocina
    cocina.agregar_observador(cliente1)

    # La cocina cambia los estados y el cliente es notificado automáticamente
    cocina.set_estado_pedido("En preparación")
    cocina.set_estado_pedido("En el horno")
    cocina.set_estado_pedido("Listo para entregar")

if __name__ == "__main__":
    main()