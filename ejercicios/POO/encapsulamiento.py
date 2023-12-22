class Persona:
    def __init__(self ,nombre, apellido, edad):#inicializar
        self._nombre = nombre#si el atributo cuenta con un _ no se debe aceder fuera del metodo self esto es solo una sugerencia al programador pero si cuenta con __ no se podra editar
        self.apellido = apellido
        self.edad = edad
        
        
    @property #decorador para poder aceder al metodo como si fuera un atributo    
    def nombre(self):#metodo get
        return self._nombre
        
    @nombre.setter#decorador para metodo set
    def nombre(self,nombre):#metodo set 
        self._nombre=nombre
        
    def mostrarDetalle(self):#metodo para imprimir el detalle de una persona
        print(f'Persona: {self._nombre} {self.apellido} {self.edad}')
        
        
persona1 = Persona('juan','perez',19)#dar valores
#persona1._nombre= 'juan carlos'#sugerencia para el desarrollador
#persona1.__nombre= 'juan carlos'#no se puede editar fuera del metodo self
#persona1.mostrarDetalle()
print(persona1.nombre)
persona1.nombre='juan carlos'
print(persona1.nombre)


