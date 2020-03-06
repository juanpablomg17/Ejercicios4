class Empleado:
    def __init__(self, id,tipo_id,cargo,sueldo,email,telefono):
        """Constructor de clase Empleado"""
        self.__id = id
        self.__tipo_id = tipo_id
        self.__cargo = cargo
        self.__sueldo = sueldo
        self.__email = email
        self.__telefono = telefono
    
    def getid(self):
        return self.__id

    def gettipo_id(self):
        return self.__tipo_id
  
    def setid(self, id):
        self.__id = id

    def setTipo_id(self, tipo_id):
        self.__tipo_id = tipo_id




class Principal(Empleado):
     



