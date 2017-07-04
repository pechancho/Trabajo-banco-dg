from Persona import *
from Cuenta import *
from Cliente import *

class Cajero():
    def __init__(self):
        self.listapersonas = []

    def agregarpersonas(self):
        self.listapersonas.append(Cliente.numcliente)

    def atender(self):
        salir = 0
        
        
        c=raw_input("ingrese el numero de cliente: ")
        a=Cliente()
        con=raw_input("ingrese la contrasenia: ")
        
        b=Cuenta(c,con)

        while salir == 0:
            tarea=raw_input("ELIJA UNA DE LAS OPCIONES: --consultar saldo-- --depositar dinero-- --extraer dinero-- --salir-- :")
            if tarea == "consultar saldo":
                b.consultar()
            if tarea == "depositar dinero":
                dinero=int(raw_input("ingrese cantidad de dinero a depositar: "))
                b.agregar_din_cuenta(dinero)
            if tarea == "extraer dinero":
                dinero=int(raw_input("ingrese cantidad de dinero a extraer: "))
                b.extraer_din_cuenta(dinero)
            if tarea == "salir":
                salir = 1  
