__author__ = 'Luzu'

class Departamento:
    def __init__(self,nombre_depto,id_depto):
        self.__nombre_depto=nombre_depto
        self.__id_depto=id_depto
        self.__empleados= []

    def aniadir_empleado(self,empleado):
        self.__empleados.append(empleado)

    def get_salario_total(self):
        salario_total=0
        for i in self.__empleados:
            salario_total = salario_total + i.get_salario()
        return salario_total