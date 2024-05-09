#segundo refinamiento
import unittest

class Trabajador:
    def __init__(self, nombre, sueldo_basico, dias_falta, minutos_tardanza, horas_extras):
        self.nombre = nombre
        self.sueldo_basico = sueldo_basico
        self.dias_falta = dias_falta
        self.minutos_tardanza = minutos_tardanza
        self.horas_extras = horas_extras

    def calcular_bonificaciones(self):
        sueldo_normal_por_hora = self.sueldo_basico / 30 / 8
        pago_horas_extras = 1.50 * self.horas_extras * sueldo_normal_por_hora
        movilidad = 1000
        bonificacion_suplementaria = 0.03 * self.sueldo_basico
        bonificaciones = movilidad + bonificacion_suplementaria + pago_horas_extras
        return bonificaciones

    def calcular_descuentos(self):
        remuneracion_computable = self.sueldo_basico + 1000 + 0.03 * self.sueldo_basico
        descuento_faltas = remuneracion_computable / 30 * self.dias_falta
        descuento_tardanzas = remuneracion_computable / 30 / 8 / 60 * self.minutos_tardanza
        descuentos = descuento_faltas + descuento_tardanzas
        return descuentos

    def calcular_sueldo_neto(self):
        bonificaciones = self.calcular_bonificaciones()
        descuentos = self.calcular_descuentos()
        sueldo_neto = self.sueldo_basico + bonificaciones - descuentos
        return sueldo_neto

    def generar_boleta_pago(self):
        bonificaciones = self.calcular_bonificaciones()
        descuentos = self.calcular_descuentos()
        sueldo_neto = self.sueldo_basico + bonificaciones - descuentos

        print("\n*** Boleta de Pago ***")
        print("Nombre del trabajador:", self.nombre)
        print("Sueldo básico:", self.sueldo_basico)
        print("Bonificaciones:")
        print("- Pago por horas extras:", bonificaciones - 1000 - 0.03 * self.sueldo_basico)
        print("- Bonificación por movilidad: 1000")
        print("- Bonificación suplementaria:", 0.03 * self.sueldo_basico)
        print("Total de bonificaciones:", bonificaciones)
        print("Descuentos:")
        print("- Descuento por faltas:", descuentos)
        print("- Descuento por tardanzas:", descuentos - (self.sueldo_basico + 1000 + 0.03 * self.sueldo_basico))
        print("Total de descuentos:", descuentos)
        print("Sueldo neto a pagar:", sueldo_neto)


def main():
    # Entrada de datos
    nombre_trabajador = input("Ingrese el nombre del trabajador: ")
    sueldo_basico = float(input("Ingrese el sueldo básico del trabajador: "))
    dias_falta = int(input("Ingrese la cantidad de días de falta del trabajador: "))
    minutos_tardanza = int(input("Ingrese la cantidad de minutos de tardanza del trabajador: "))
    horas_extras = int(input("Ingrese la cantidad de horas extras trabajadas: "))

    # Crear instancia de Trabajador
    trabajador = Trabajador(nombre_trabajador, sueldo_basico, dias_falta, minutos_tardanza, horas_extras)

    # Generar boleta de pago
    trabajador.generar_boleta_pago()


class TestTrabajador(unittest.TestCase):
    def test_calcular_bonificaciones(self):
        trabajador = Trabajador("Juan", 2000, 2, 0, 8)
        self.assertEqual(trabajador.calcular_bonificaciones(), 1160)

    def test_calcular_descuentos(self):
        trabajador = Trabajador("Juan", 2000, 2, 0, 8)
        self.assertEqual(trabajador.calcular_descuentos(), 204)

    def test_calcular_sueldo_neto(self):
        trabajador = Trabajador("Juan", 2000, 2, 0, 8)
        self.assertEqual(trabajador.calcular_sueldo_neto(), 2956)

if __name__ == "__main__":
    main()
    unittest.main()