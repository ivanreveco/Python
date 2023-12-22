class Persona:
    def __init__(self,nombre,edad):
        self._nombre=nombre
        self._edad=edad
        
    @property
    def nombre(self):
        return self._nombre
    
    @property
    def edad(self):
        return self._edad
    
    @nombre.setter
    def nombre(self,nombre):
        self._nombre=nombre
    @edad.setter
    def edad(self,edad):
        self._edad=edad
    
class Empleado(Persona):
    def __init__(self,nombre,edad,sueldo):
        super().__init__(nombre,edad)
        self._sueldo = sueldo
    @property
    def sueldo(self):
        return self._sueldo
    @sueldo.setter
    def sueldo(self,sueldo):
        self._sueldo=sueldo
    
    def mostrarDetalle(self):
        print(f'empleado :{self._nombre}\nedad: {self.edad}\nsueldo: {self.sueldo}')

empleado1=Empleado('jose',20,250)
empleado1.nombre = 'jose'
empleado1.edad= 20
empleado1.sueldo = 1400 
empleado1.mostrarDetalle()
