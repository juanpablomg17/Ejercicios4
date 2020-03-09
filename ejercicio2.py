class Estudiante:
    def __init__(self,id,tipo_id,nombres,programa,semestre,institucion):
        self.__id = id
        self.__tipo_id = tipo_id
        self.__nombres = nombres
        self.__programa = programa
        self.__semestre = semestre
        self.__institucion = institucion
    def __init__(self):
        pass

    #métodos get
    def getId(self):
        return self.__id
    def getTipoId(self):
        return self.__tipo_id
    def getNombres(self):
        return self.__nombres
    def getPrograma(self):
        return self.__programa
    def getSemestre(self):
        return self.__semestre
    def getInstitucion(self):
        return self.__institucion

    #métodos set
    def setId(self, id):
        self.__id = id
    def setTipoId(self,tipo_id):
        self.__tipo_id = tipo_id
    def setNombres(self,nombres):
        self.__nombres = nombres
    def setPrograma(self,programa):
        self.__programa = programa
    def setSemestre(self,semestre):
        self.__semestre = semestre
    def setInstitucion(self,institucion):
        self.__institucion = institucion



class Principal(Estudiante):

    pass


p1 = Principal()

id = int(input("digite su id: "))
tipo_id = input("digite el tipo de su id: ")
nombres = input("digite su nombre completo: ")
programa = input("digite su programa académico: ")
semestre = input("digite su semestre: ")
institucion = input("digite su institución: ")


p1.setId(id)
p1.setTipoId(tipo_id)
p1.setNombres(nombres)
p1.setPrograma(programa)
p1.setSemestre(semestre)
p1.setInstitucion(institucion)
print("\n Datos: ")
print(f"\n Id: {p1.getId()} \n Tipo id: {p1.getTipoId()}  \n Nombre completo: {p1.getNombres()}\n Programa: {p1.getPrograma()} \n Semestre: {p1.getSemestre()} \nInstitucion: {p1.getInstitucion}")







        
