from tienda import Restaurante,Supermercado,Farmacia
from producto import Producto
import sys

opcion = int(input("¿Desea crear una tienda?\n1. Si\n2. No\n"))

if opcion == 1:
    tipo_tienda = int(input("Tipo de tienda:\n1. Restaurante\n2. Supermercado\n3. Farmacia\n"))
    nombre_tienda = input("\nFavor nombre de la tienda:\n")
    costo_delivery = int(input("\nFavor indique costo del delivery:\n"))
    if tipo_tienda == 1:
        Restaurante.crear_tienda(nombre_tienda, costo_delivery)
    elif tipo_tienda == 2:
        Supermercado.crear_tienda(nombre_tienda, costo_delivery)
    elif tipo_tienda == 3:
        Farmacia.crear_tienda(nombre_tienda, costo_delivery)
else:
    print("\nNo se ha creado ninguna tienda.")
opc_prod = int(input("\n¿Desea agregar productos a la tienda?\n1. Si\n2. No\n"))

if opc_prod == 1:
    opcion = int(input("\nFavor seleccione la tienda para agregar productos\n1. Restaurante\n2. Supermercado\n3. Farmacia\n"))
    while opcion == 1:
        nombre_prod = input("\nFavor nombre del producto:\n")
        precio_prod = int(input("\nIngrese precio del producto:\n"))
        stock_prod = int(input("\nIngrese cantidad de stock del producto:\n"))
        Producto.crear_prod_restaurante(nombre_prod,precio_prod,stock_prod)
        opcion = int(input("\n¿Desea agregar otro producto a la tienda?\n1. Restaurante\n2. Supermercado\n3. Farmacia\n4. Salir\n"))
    while opcion == 2:
        nombre_prod = input("\nFavor nombre del producto:\n")
        precio_prod = int(input("\nIngrese precio del producto:\n"))
        stock_prod = int(input("\nIngrese cantidad de stock del producto:\n"))
        Producto.crear_prod_supermercado(nombre_prod,precio_prod,stock_prod)
        opcion = int(input("\n¿Desea agregar otro producto a la tienda?\n1. Restaurante\n2. Supermercado\n3. Farmacia\n4. Salir\n"))
    while opcion == 3:
        nombre_prod = input("\nFavor nombre del producto:\n")
        precio_prod = int(input("\nIngrese precio del producto:\n"))
        stock_prod = int(input("\nIngrese cantidad de stock del producto:\n"))
        Producto.crear_prod_farmacia(nombre_prod,precio_prod,stock_prod)
        opcion = int(input("\n¿Desea agregar otro producto a la tienda?\n1. Restaurante\n2. Supermercado\n3. Farmacia\n4. Salir\n"))
    if opcion != 1 or opcion != 2 or opcion != 3:
        print('Salió de agregar productos')
else:
    print('No agregó productos a la tienda')
opc_vent = int(input("\n¿Desea comprar productos de la tienda?\n1. Si\n2. No\n"))
if opc_vent == 1:
    opc_comp = int(input("\nFavor seleccione la tienda para comprar productos\n1. Restaurante\n2. Supermercado\n3. Farmacia\n"))
    while opc_comp == 1:
        nombre_prod = input("\nFavor nombre del producto:\n")
        stock_prod = int(input("\nIngrese cantidad a comprar del producto:\n"))
        Restaurante.ventas(nombre_prod,stock_prod)
        opc_comp = int(input("\n¿Desea agregar otro producto a la compra?\n1. Restaurante\n2. Supermercado\n3. Farmacia\n4. Salir\n"))
    while opc_comp == 2:
        nombre_prod = input("\nFavor nombre del producto:\n")
        stock_prod = int(input("\nIngrese cantidad a comprar del producto:\n"))
        Supermercado.ventas(nombre_prod,stock_prod)
        opc_comp = int(input("\n¿Desea agregar otro producto a la compra?\n1. Restaurante\n2. Supermercado\n3. Farmacia\n4. Salir\n"))
    while opc_comp == 3:
        nombre_prod = input("\nFavor nombre del producto:\n")
        stock_prod = int(input("\nIngrese cantidad a comprar del producto:\n"))
        Farmacia.ventas(nombre_prod,stock_prod)
        opc_comp = int(input("\n¿Desea agregar otro producto a la compra?\n1. Restaurante\n2. Supermercado\n3. Farmacia\n4. Salir\n"))
    if opc_comp == 4:
        print('Salió de compras')
else:
    print('No agregó productos a la compra')

opc_inv = int(input("\n¿Desea ver stocks de productos de la tienda?\n1. Si\n2. No\n"))
if opc_inv == 1:
    opc = int(input("\nFavor seleccione la tienda para ver inventario de productos\n1. Restaurante\n2. Supermercado\n3. Farmacia\n"))
    if opc == 1:
        Restaurante.mostrar_productos()
        opc = int(input("\n¿Desea ver inventario de otra tienda?\n1. Restaurante\n2. Supermercado\n3. Farmacia\n4. Salir\n"))
    if opc == 2:
        Supermercado.mostrar_productos()
        opc = int(input("\n¿Desea ver inventario de otra tienda?\n1. Restaurante\n2. Supermercado\n3. Farmacia\n4. Salir\n"))
    if opc == 3:
        Farmacia.mostrar_productos()
        opc = int(input("\n¿Desea ver inventario de otra tienda?\n1. Restaurante\n2. Supermercado\n3. Farmacia\n4. Salir\n"))
    if opc == 4:
        print('Vuelva Pronto!')
else:
    print('Vuelva Pronto!')
    sys.exit()
