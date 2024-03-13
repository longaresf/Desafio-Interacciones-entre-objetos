from abc import ABC, abstractmethod
#from producto import Producto

class Tienda(ABC):
    productos = []
    def __init__(self, nombre:str, costo_delivery:int):
        self.__nombre = nombre
        self.__costo_delivery = costo_delivery

    @property
    def nombre(self) -> str :
        return self.__nombre

    @property
    def costo_delivery(self) -> int :
        return self.__costo_delivery

    @abstractmethod
    def crear_tienda(tienda): pass
    
    @abstractmethod
    def agregar_producto(self, prod)->None:
        pass

    def __add__(prod_rest):
        return  prod_rest.stock + prod.stock


    def __sub__(prod_rest):
        return  prod_rest.stock - prod.stock


    def __eq__(prod_rest):
        return  prod_rest.nombre == prod.nombre
    
    def __eq__(prod_rest):
        return  prod_rest.stock > prod.stock

class Restaurante(Tienda):
    productos:list
    def __init__(self, nombre:str, costo_delivery:int):
        self.__nombre = nombre
        self.__costo_delivery = costo_delivery
        super().__init__(nombre, costo_delivery)
        
    @property
    def nombre(self) -> str :
        return self.__nombre

    @property
    def costo_delivery(self) -> int :
        return self.__costo_delivery

    @staticmethod
    def crear_tienda(nombre_tienda, costo_delivery):
        tienda_rest = Restaurante(nombre_tienda, costo_delivery)
        print(f'Se creó con éxito tienda tipo: Restaurante, de nombre: {tienda_rest.nombre}')

    def agregar_producto(prod) -> None:
        for i in Restaurante.productos:
            if (i==prod.nombre).__eq__(True):
                print(f'Producto {i} existe en stock')
                break
        else:
            Restaurante.productos.append(prod.nombre)
            Restaurante.productos.append(prod.precio)
            Restaurante.productos.append(prod.stock)

    def mostrar_productos():
        for i in Restaurante.productos:
            if type(i) is str:
                indice=Restaurante.productos.index(i)
                print(f'Producto: {Restaurante.productos[indice]}\nPrecio: {Restaurante.productos[indice+1]}')

    def ventas(prod_venta, cant_venta) -> None:
        for i in Restaurante.productos:
            if (i==prod_venta).__eq__(True):
                indice=Restaurante.productos.index(i)
                print(f'\nVenta exitosa del producto: {Restaurante.productos[indice]}\nCantidad solicitada: {cant_venta}\nMonto a pagar: {Restaurante.productos[indice+1] * cant_venta}\n')
            else:
                print('Producto no encontrado')


class Supermercado(Tienda):
    productos:list
    def __init__(self, nombre:str, costo_delivery:int):
        self.__nombre = nombre
        self.__costo_delivery = costo_delivery
        super().__init__(nombre, costo_delivery)
        
    @property
    def nombre(self) -> str :
        return self.__nombre

    @property
    def costo_delivery(self) -> int :
        return self.__costo_delivery

    @staticmethod
    def crear_tienda(nombre_tienda, costo_delivery):
        tienda_rest = Supermercado(nombre_tienda, costo_delivery)
        print(f'Se creó con éxito tienda tipo: Supermercado, de nombre: {tienda_rest.nombre}')

    def agregar_producto(prod) -> None:
        for i in Supermercado.productos:
            if (i==prod.nombre).__eq__(True):
                print(f'Producto {i} existe en stock')
                break
        else:
            Supermercado.productos.append(prod.nombre)
            Supermercado.productos.append(prod.precio)
            Supermercado.productos.append(prod.stock)

    def mostrar_productos():
        for i in Supermercado.productos:
            if type(i) is str:
                indice=Supermercado.productos.index(i)
                print(f'Producto: {Supermercado.productos[indice]}\nPrecio: {Supermercado.productos[indice+1]}\nStock: {Supermercado.productos[indice+2]}')
                print('' if Supermercado.productos[indice+2] > 10 else 'Pocos productos disponibles')

    def ventas(prod_venta, cant_venta) -> None:
        for i in Supermercado.productos:
            if (i==prod_venta).__eq__(True):
                print(f'Producto encontrado: {prod_venta}')
                indice=Supermercado.productos.index(i)
                if Supermercado.productos[indice+2] >= cant_venta or Supermercado.productos[indice+2] == cant_venta:
                    print(f'\nVenta exitosa del producto: {Supermercado.productos[indice]}\nCantidad solicitada: {cant_venta}\nMonto a pagar: {Supermercado.productos[indice+1] * cant_venta}\n')
                else:
                    print(f"No hay suficiente stock: {Supermercado.productos[indice+2]}")
            else:
                print('Producto no encontrado')


class Farmacia(Tienda):
    productos:list
    def __init__(self, nombre:str, costo_delivery:int):
        self.__nombre = nombre
        self.__costo_delivery = costo_delivery
        super().__init__(nombre, costo_delivery)
        
    @property
    def nombre(self) -> str :
        return self.__nombre

    @property
    def costo_delivery(self) -> int :
        return self.__costo_delivery

    @staticmethod
    def crear_tienda(nombre_tienda, costo_delivery):
        tienda_rest = Farmacia(nombre_tienda, costo_delivery)
        print(f'Se creó con éxito tienda tipo: Farmacia, de nombre: {tienda_rest.nombre}')

    def agregar_producto(prod) -> None:
        for i in Farmacia.productos:
            if (i==prod.nombre).__eq__(True):
                print(f'Producto {i} existe en stock')
                break
        else:
            Farmacia.productos.append(prod.nombre)
            Farmacia.productos.append(prod.precio)
            Farmacia.productos.append(prod.stock)

    def mostrar_productos():
        for i in Farmacia.productos:
            if type(i) is str:
                indice=Farmacia.productos.index(i)
                print(f'Producto: {Farmacia.productos[indice]}\nPrecio: {Farmacia.productos[indice+1]}')
                print('Envío gratis al solicitar este producto' if Farmacia.productos[indice+1] > 15000 else '')

    def ventas(prod_venta, cant_venta) -> None:
        for i in Farmacia.productos:
            if (i==prod_venta).__eq__(True):
                print(f'Producto encontrado: {prod_venta}')
                indice=Farmacia.productos.index(i)
                if cant_venta <= 3 and Farmacia.productos[indice+1] >= cant_venta:
                    print(f'\nVenta exitosa del producto: {Farmacia.productos[indice]}\nCantidad solicitada: {cant_venta}\nMonto a pagar: {Farmacia.productos[indice+1] * cant_venta}\n')
                else:
                    print(f'Cantidad de productos excede a 3 unidades o no hay suficiente stock del producto\nUsted solicitó: {cant_venta} y hay stock {Farmacia.productos[indice+1]}')
            else:
                print('Producto no encontrado')