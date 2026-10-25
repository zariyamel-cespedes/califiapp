# test_calificaciones.py - Cada criterio de aceptación es una prueba
# Se ejecutan desde la carpeta califiapp con:
#     python -m unittest discover -s tests -v
import os
import sys
import unittest

# Permite importar src/calificaciones.py aunque las pruebas vivan en tests/
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "src"))

from calificaciones import *


class HU01RegistrarAlumnos(unittest.TestCase):

    def test_registrar_alumno_valido(self):
        alumnos = []
        self.assertTrue(registrar_alumno(alumnos, "Ana López"))
        self.assertEqual(alumnos, ["Ana López"])

    def test_no_registrar_nombre_vacio(self):
        alumnos = []
        self.assertFalse(registrar_alumno(alumnos, "   "))
        self.assertEqual(len(alumnos), 0)

    def test_limite_30_alumnos(self):
        alumnos = ["Alumno"] * 30
        self.assertFalse(registrar_alumno(alumnos, "Luis"))
        self.assertEqual(len(alumnos), 30)


class HU02CapturarCalificaciones(unittest.TestCase):

    def test_calificacion_valida(self):
        self.assertEqual(validar_calificacion("8.5"), 8.5)
        self.assertEqual(validar_calificacion("0"), 0)
        self.assertEqual(validar_calificacion("10"), 10)

    def test_calificacion_fuera_de_rango(self):
        self.assertIsNone(validar_calificacion("11"))
        self.assertIsNone(validar_calificacion("-1"))

    def test_calificacion_no_numerica(self):
        self.assertIsNone(validar_calificacion("ocho"))


class HU03PromedioYEstatus(unittest.TestCase):

    def test_promedio_un_decimal(self):
        self.assertEqual(calcular_promedio([7, 8, 8]), 7.7)

    def test_estatus_aprobado_en_6(self):
        self.assertEqual(obtener_estatus(6.0), "APROBADO")

    def test_estatus_reprobado(self):
        self.assertEqual(obtener_estatus(5.9), "REPROBADO")


class HU04ReporteDelGrupo(unittest.TestCase):

    def test_fila_reporte(self):
        self.assertEqual(fila_reporte("Ana", 8.0), "Ana | 8.0 | APROBADO")

    def test_promedio_grupal(self):
        self.assertEqual(promedio_grupal([8.0, 6.0, 7.0]), 7.0)

    def test_promedio_grupal_sin_alumnos(self):
        self.assertEqual(promedio_grupal([]), 0.0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
