# Punto de Venta simple en Python
from dataclasses import dataclass
from typing import Dict, List

@dataclass
class Producto:
    nombre: str
    precio: float

class PuntoDeVenta:
    def __init__(self) -> None:
        self.productos: Dict[str, Producto] = {}
        self.carrito: List[Producto] = []

    def agregar_producto(self, nombre: str, precio: float) -> None:
        self.productos[nombre] = Producto(nombre, precio)
        print(f"Producto '{nombre}' registrado con precio {precio}")

    def agregar_al_carrito(self, nombre: str) -> None:
        producto = self.productos.get(nombre)
        if producto:
            self.carrito.append(producto)
            print(f"Se añadió '{nombre}' al carrito")
        else:
            print("Producto no encontrado")

    def mostrar_carrito(self) -> None:
        if not self.carrito:
            print("Carrito vacío")
            return
        print("\nArtículos en el carrito:")
        total = 0.0
        for prod in self.carrito:
            print(f"- {prod.nombre}: ${prod.precio:.2f}")
            total += prod.precio
        print(f"Total: ${total:.2f}\n")

    def cobrar(self) -> None:
        self.mostrar_carrito()
        if self.carrito:
            self.carrito.clear()
            print("Gracias por su compra!")


def menu():
    pdv = PuntoDeVenta()
    while True:
        print("\n=== Menú Punto de Venta ===")
        print("1. Registrar producto")
        print("2. Añadir al carrito")
        print("3. Mostrar carrito")
        print("4. Cobrar")
        print("5. Salir")
        opcion = input("Seleccione opción: ")
        if opcion == '1':
            nombre = input("Nombre: ")
            precio = float(input("Precio: "))
            pdv.agregar_producto(nombre, precio)
        elif opcion == '2':
            nombre = input("Nombre del producto: ")
            pdv.agregar_al_carrito(nombre)
        elif opcion == '3':
            pdv.mostrar_carrito()
        elif opcion == '4':
            pdv.cobrar()
        elif opcion == '5':
            break
        else:
            print("Opción inválida")


if __name__ == "__main__":
    menu()
