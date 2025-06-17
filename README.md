# Sistema de Punto de Venta

Este repositorio contiene un ejemplo muy básico de un sistema de **punto de venta** escrito en Python.

## Requisitos

- Python 3.8 o superior

## Uso

Ejecute el script `pos.py` desde la línea de comandos:

```bash
python pos.py
```

Aparecerá un menú interactivo que permite:

1. Registrar productos con nombre y precio.
2. Añadir productos registrados a un carrito.
3. Mostrar el contenido del carrito y el total.
4. Cobrar (vaciar el carrito).
5. Salir del programa.

Este proyecto es solo un ejemplo simplificado y no guarda los datos de manera persistente.

## Autenticacion
Para acceder al sistema primero se solicitan credenciales de usuario. Ejecute `python pos.py` y siga las instrucciones de inicio de sesion.

## Administracion de sucursales
El sistema permite registrar varias sucursales (branches) para organizar los productos y las ventas.

### Ejemplo de alta de sucursal
```bash
python pos.py --agregar-sucursal "Sucursal Centro"
```

## Ventas a credito
Al realizar una venta se puede indicar si sera de contado o a credito. Las ventas a credito se registran con el monto pendiente.

### Ejemplo de venta a credito
```bash
python pos.py --vender "Producto X" --precio 10 --credito
```

## Interfaz web
Existe una interfaz web minima incluida en el directorio `web`. Para lanzarla utilice:
```bash
python -m http.server 8000
```
Luego abra `http://localhost:8000` en su navegador.

## Pruebas
Ejecute las pruebas unitarias con:
```bash
python -m unittest discover tests
```

