__author__ = 'Luzu'

class Empresa:

    def __init__(self, nombre_empresa, cif, razon_social):
        self.__nombre_empresa=nombre_empresa
        self.__cif=cif
        self.__razon_social=razon_social
        self.__departamentos= []