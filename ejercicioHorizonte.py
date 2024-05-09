import unittest

class Trabajador:
    def _init_(self, nombre, sueldo_basico, horas_trabajadas, horas_extra, minutos_tardanza, tardanzas, faltas):
        self.nombre = nombre
        self.sueldo_basico = sueldo_basico
        self.horas_trabajadas = horas_trabajadas
        self.horas_extra = horas_extra
        self.minutos_tardanza = minutos_tardanza
        self.tardanzas = tardanzas
        self.faltas = faltas

    def calcular_sueldo(self): 
        return

    def calcular_bonificaciones(self):
        return 

    def calcular_descuentos(self):
        return 

def main():
    # Ingreso de datos
    nombre_trabajador = input("Ingrese el nombre del trabajador: ")
    sueldo_basico = float(input("Ingrese el sueldo básico del trabajador: "))
    horas_trabajadas = int(input("Ingrese las horas trabajadas: "))
    horas_extra = int(input("Ingrese las horas extra trabajadas: "))
    minutos_tardanza = int(input("Ingrese los minutos de tardanza: "))
    tardanzas = int(input("Ingrese el número de tardanzas: "))
    faltas = int(input("Ingrese el número de faltas: "))

    # Creación del objeto Trabajador
    trabajador = Trabajador(nombre_trabajador, sueldo_basico, horas_trabajadas, horas_extra, minutos_tardanza, tardanzas, faltas)

    # Cálculo del sueldo a pagar
    sueldo_a_pagar = trabajador.calcular_sueldo()

    # Imprimir boleta de pago
    imprimir_boleta_pago(nombre_trabajador, sueldo_a_pagar)

def imprimir_boleta_pago(nombre_trabajador, sueldo_neto):
    print("***BOLETA DE PAGO***")
    print("")
    print(f"Nombre del trabajador: {nombre_trabajador}")

if _name_ == "_main_":
    main()