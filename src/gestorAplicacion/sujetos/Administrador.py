from typing import List
from gestorAplicacion.servicios.Tienda import Tienda
from gestorAplicacion.servicios.Enums import Genero

class Persona:
    personas = []

    def __init__(self, nombre, id, edad, genero):
        self.nombre = nombre
        self.id = id
        self.edad = edad
        self.genero = genero
        Persona.personas.append(self)

class Administrador(Persona):
    def __init__(self, nombre=None, id=None, edad=None, genero=None, dinero=0):
        super().__init__(nombre, id, edad, genero)
        self.dinero = dinero
        self.tiendas = []

    def get_tiendas(self):
        return self.tiendas

    def get_facturas(self, tienda):
        # Método que debe estar implementado para devolver las facturas de la tienda
        return tienda.get_facturas()

    def get_tiendas_con_facturas(self):
        tienda_con_facturas = {}

        for tienda in self.tiendas:
            if tienda is not None:
                facturas = tienda.get_facturas()  # Obtener facturas de la tienda
                if facturas and len(facturas) > 0:
                    tienda_con_facturas[tienda] = len(facturas)  # Contar las facturas

        # Devolver la lista de tiendas únicas con al menos una factura
        return list(tienda_con_facturas.keys())

    def set_tiendas(self, tiendas: List[Tienda]):
        self.tiendas = tiendas

    def get_dinero(self):
        return self.dinero

    def set_dinero(self, dinero):
        self.dinero = dinero