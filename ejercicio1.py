class Empleado:
    def __init__(self, id, tipo_id, cargo, sueldo, email, telefono, empresa):
        """Constructor de clase Empleado"""
        self.__id = id
        self.__tipo_id = tipo_id
        self.__cargo = cargo
        self.__sueldo = sueldo
        self.__email = email
        self.__telefono = telefono
        self.__empresa = empresa

    # métodos get

    def getid(self):
        return self.__id

    def gettipo_id(self):
        return self.__tipo_id

    def getcargo(self):
        return self.__cargo

    def getSueldo(self):
        return self.__sueldo

    def getEmail(self):
        return self.__email

    def getTelefono(self):
        return self.__telefono

    def getEmpresa(self):
        return self.__empresa

    # métodos set

    def setid(self, id):
        self.__id = id

    def setTipo_id(self, tipo_id):
        self.__tipo_id = tipo_id

    def setcargo(self, cargo):
        self.__cargo = cargo

    def setSueldo(self, sueldo):
        self.__sueldo = sueldo

    def setEmail(self, email):
        self.__email = email

    def setTelefono(self, telefono):
        self.__telefono = telefono

    def setEmpresa(self, empresa):



class Pricipal(Empleado):
    pass

def main():
    p1 = Pricipal(1213,32423,234234,4324234,234234,324324,234324)

    print(p1.getid)


main()
