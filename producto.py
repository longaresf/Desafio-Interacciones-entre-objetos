from tienda import Tienda, Restaurante,Supermercado,Farmacia

class Producto():
    prod_restaurante = []
    prod_supermercado = []
    prod_farmacia = []

    def __init__(self, nombre:str, precio:int, stock:int):
        self.__nombre = nombre
        self.__precio = precio
        self.__stock = stock
 
    @property
    def nombre(self) -> str :
        return self.__nombre

    @property
    def precio(self) -> int :
        return self.__precio

    @property
    def stock(self) -> int :
        return self.__stock
    
    @staticmethod
    def crear_prod_restaurante(nombre_prod,precio_prod,stock_prod):
        stock_prod=0
        prod = Producto(nombre_prod,precio_prod,stock_prod)
        print(f'Se creó el producto: {prod.nombre} de precio {prod.precio} con stock {prod.stock}')
        Restaurante.agregar_producto(prod)
    
    def crear_prod_supermercado(nombre_prod,precio_prod,stock_prod):
        prod = Producto(nombre_prod,precio_prod,stock_prod)
        print(f'Se creó el producto: {prod.nombre} de precio {prod.precio} con stock {prod.stock}')
        Restaurante.agregar_producto(prod)
  
    def crear_prod_farmacia(nombre_prod,precio_prod,stock_prod):
        prod = Producto(nombre_prod,precio_prod,stock_prod)
        print(f'Se creó el producto: {prod.nombre} de precio {prod.precio} con stock {prod.stock}')
        Restaurante.agregar_producto(prod)
