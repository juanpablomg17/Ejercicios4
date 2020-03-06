class Vehiculo:
    def __init__(self,ref_Motor,modelo,matricula):
        self.__ref = ref_Motor
        self.__model = modelo
        self.__matricula = matricula
        
    def __init__(self):
        pass
    
    def getRef(self):
        return self.__ref
    
    def getModel(self):
        return self.__model
    
    def getMatricula(self):
        return self.__matricula
    
    def setRef(self,ref):
        self.__ref = ref
        
    def setModel(self,model):
        self.__model = model
        
    def setMatricula(self,matricula):
        self.__matricula = matricula




class VehiculoTerrestre(Vehiculo):
    def VT()

class VehiculoAereo(Vehiculo):
    pass

class Avion(VehiculoAereo):
    pass

class Helicoptero(VehiculoAereo):
    pass

class Dron(VehiculoAereo):
    pass

class Auto(VehiculoTerrestre):
    pass

class Motocicleta(VehiculoTerrestre):
    pass

class Bicicleta(VehiculoTerrestre):
    pass

