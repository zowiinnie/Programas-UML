from cafeteria import *

productos = [
    Producto("Flat White", 58, 80),
    Producto("Mocha Blanco", 65, 40),
    Producto("Galleta de Avena", 38, 25, es_vegano=True),
    Producto("Panqué de Almendra", 52, 12, sin_gluten=True),
    Producto("Chocolate Caliente", 48, 60),
    Producto("Té Chai Latte", 50, 35),
    Producto("Bagel Integral", 42, 30),
    Producto("Sandwich Vegetariano", 70, 18, es_vegano=True)
]


print("----------------- MENÚ CAFETERÍA ------------------")
for i in range(len(productos)):
    p = productos[i]

    info = f"({'V' if p.es_vegano else ''}{'SG' if p.sin_gluten else ''})"
    print(f"{i + 1} - {p.nombre} (${p.precio}) {info if info != '()' else ''}")

opcion = int(input("\nElige un producto (1-8): ")) - 1
producto_elegido = productos[opcion]


control_suministros = Inventario()


ingrediente = "Harina" if "Galleta" in producto_elegido.nombre or "Panqué" in producto_elegido.nombre or "Bagel" in producto_elegido.nombre else "Cafe"

if control_suministros.reducir_stock(ingrediente, 1):
    
    instrucciones = input("¿Instrucciones especiales?: ")
    desea_extra = input("¿Desea agregar un extra por $15? (si/no): ")
    precio_extra = 15 if desea_extra.lower() == "si" else 0

    
    empleado1 = Empleado(101, "Jorge", "jorgis@cafe.com", "E-500", "Barista")
    nombre_c = input("Tu nombre: ")
    cliente1 = Persona(1, nombre_c, "correo@ejemplo.com")

    
    pedido1 = Pedido(800, cliente1.nombre)
    
    if pedido1.agregar_producto(producto_elegido, instrucciones, precio_extra):
        
        
        empleado1.cambiar_estado_pedido(pedido1, "PREPARANDO")
        empleado1.cambiar_estado_pedido(pedido1, "ENTREGADO")

        
        print("\n----------------- TICKET DE VENTA ------------------")
        print("Atendido por:", empleado1.nombre)
        print("Cliente:", cliente1.nombre)
        print("Producto:", producto_elegido.nombre)
        print("Notas:", instrucciones)
        print("Total a pagar: $", pedido1.total)
        print("Estado final:", pedido1.estado)
        print("----------------------------------------------------")
        
    
        print(f"Suministros restantes de {ingrediente}: {control_suministros.ingredientes[ingrediente]}")

else:
    print(f"No se puede preparar: falta {ingrediente} en inventario.")
    