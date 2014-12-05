__author__ = 'Luzu'


class Empleado:
    def __init__(self, nombre, apellidos, dni, direccion, edad, email, salario):
        """Constructor

        Metodo constructor de la clase Empleado.

        :param nombre:
        :param apellidos:
        :param dni:
        :param direccion:
        :param edad:
        :param email:
        :param salario:
        :return:
        """
        self.__nombre = nombre
        self.__apellidos = apellidos
        self.__dni = dni
        self.__direccion = direccion
        self.__edad = edad
        self.__email = email
        self.__salario = salario

    def get_salario(self):
        """Get salario

        Metodo que devuelve el salario del empleado.

        :return: salario
        """
        return self.__salario

    def get_dni(self):
        """Get dni

        Metodo que devuelve el dni del empleado.

        :return: dni
        """
        return self.__dni

    def get_nombre_apellidos(self):
        """Get nombre y apellidos

        Metodo que devuelve el nombre y apellidos del empleado..

        :return: nombre y apellidos
        """
        return self.__nombre + " " + self.__apellidos

    def get_edad(self):
        """Get edad

        Metodo que devuelve la edad del empleado.

        :return: edad
        """
        return self.__edad

    def get_email(self):
        """Get email

        Metodo que devuelve el email del empleado.

        :return: email
        """
        return self.__email

    def get_direccion(self):
        """Get direccion

        Metodo que devuelve la direccion del empleado.

        :return: direccion
        """
        return self.__direccion

    def get_salario_mensual(self):
        """Get salario mensual

        Metodo que devuelve el salario mensual del empleado.

        :return: salario mensual
        """
        return self.__salario / 12
