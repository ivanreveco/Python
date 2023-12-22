class Persona:
    def __init__(self,nombre,edad):
        self._nombre=nombre
        self._edad=edad
    def __str__(self):#sobre escribir en clase hija
        return f'Persona :{self.nombre}\nedad: {self.edad}'
        
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
        super().__init__(nombre,edad)#para inicializar los atributos de la clase padre en empleados
        self._sueldo = sueldo
    def __str__(self):#sobre escribir en clase hija
        return f'{super().__str__()}\nSueldo: {self._sueldo}'# utilizamos super para poder acedder al metodo __str__ de la clase padre que contiene el nombre y la edad del empleado
        
    @property
    def sueldo(self):
        return self._sueldo
    @sueldo.setter
    def sueldo(self,sueldo):
        self._sueldo=sueldo
    
    def mostrarDetalle(self):
        print(f'empleado :{self._nombre}\nedad: {self.edad}\nsueldo: {self.sueldo}')

#empleado1=Empleado('jose',20,250)
#empleado1.nombre = 'jose'
#empleado1.edad= 20
#empleado1.sueldo = 1400 
#empleado1.mostrarDetalle()
