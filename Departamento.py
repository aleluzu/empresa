__author__ = 'Luzu'

class Departamento:
    def __init__(self,nombre_depto,id_depto):
        """Constructor

        Metodo constructor de la clase Departamento.

        :param nombre_depto:
        :param id_depto:
        :return:
        """
        self.__nombre_depto=nombre_depto
        self.__id_depto=id_depto
        self.__empleados= []


    def aniadir_empleado(self,empleado):
        """Anadir empleado

        Metodo que anade un empleado a la lista de empleados.

        :param empleado:
        :return:
        """
        self.__empleados.append(empleado)

    def get_salario_total(self):
        """Get salario total

        Metodo que calcula el salario total de todos los empleados de la lista de empleados.

        :return: salario total
        """
        salario_total=0
        for i in self.__empleados:
            salario_total = salario_total + i.get_salario()
        return salario_total

    def get_nombre_depto(self):
        """Get nombre departamento

        Metodo que devuelve el nombre del departamento.

        :return: nombre departamento
        """
        return self.__nombre_depto

    def get_salario_total_mensual(self):
        """Get salario total mensual

        Metodo que devuelve el salario total mensual de todos los empleados de la lista de empleados.

        :return: salario total mensual
        """
        salario_total_mensual=0
        for i in self.__empleados:
            salario_total_mensual = salario_total_mensual + i.get_salario_mensual()
        return salario_total_mensual