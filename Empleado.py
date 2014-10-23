__author__ = 'Luzu'

class Empleado:
    def __init__(self,nombre,apellidos,dni,direccion,edad,email,salario):
        self.__nombre=nombre
        self.__apellidos=apellidos
        self.__dni=dni
        self.__direccion=direccion
        self.__edad=edad
        self.__email=email
        self.__salario=salario


    def get_salario(self):
        return self.__salario

    def get_dni(self):
        return self.__dni

    def get_nombre_apellidos(self):
        return self.__nombre + " " + self.__apellidos

    def get_edad(self):
        return self.__edad

    def get_email(self):
        return self.__email

    def get_direccion(self):
        return self.__direccion

    def get_salario_mensual(self):
        return self.__salario/12

