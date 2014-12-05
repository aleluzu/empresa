import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from unittest import TestCase

from mockito import *

from src.Departamento import *
from src.Empleado import *


__author__ = 'Luzu'


class TestDepartamento(TestCase):
    def test_get_salario_total(self):
        """Test unitario get salario total

        Test que comprueba el funcionamiento del metodo
        "get_salario_total" de la clase Departamento.

        :return:
        """
        dep = Departamento('dep1', 1)
        emp1 = mock(Empleado)
        emp2 = mock(Empleado)
        emp3 = mock(Empleado)
        when(emp1).get_salario().thenReturn(1000)
        when(emp2).get_salario().thenReturn(2000)
        when(emp3).get_salario().thenReturn(3000)

        dep.aniadir_empleado(emp1)
        dep.aniadir_empleado(emp2)
        dep.aniadir_empleado(emp3)

        self.assertEqual(dep.get_salario_total(), 6000)

    def test_get_salario_total_mensual(self):
        """Test unitario get salario total mensual

        Test que comprueba el funcionamiento del metodo
        "get_salario_total_mensual" de la clase Departamento.

        :return:
        """
        dep = Departamento('dep1', 1)
        emp1 = mock(Empleado)
        emp2 = mock(Empleado)
        emp3 = mock(Empleado)
        when(emp1).get_salario_mensual().thenReturn(100)
        when(emp2).get_salario_mensual().thenReturn(200)
        when(emp3).get_salario_mensual().thenReturn(300)

        dep.aniadir_empleado(emp1)
        dep.aniadir_empleado(emp2)
        dep.aniadir_empleado(emp3)

        self.assertEqual(dep.get_salario_total_mensual(), 600)
