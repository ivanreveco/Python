class MiClase:
    varibles_clase="valor de la varible de clase"
    
    def __init__(self,variable_instancia):
        self.varibles_instancia=variable_instancia
        
    @staticmethod
    def metodo_estatico():#metodo estatico no acede a varibles de instancia como self
        print(MiClase.varibles_clase)
        
    @classmethod
    def metodo_clase(cls):
        print(cls.varibles_clase)
miClase = MiClase("valor variable instancia")
print(miClase.varibles_instancia)

MiClase.metodo_estatico()
MiClase.metodo_clase()