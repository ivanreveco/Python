class Persona:
    def __init__(self ,nombre, apellido, edad):#inicializar
        self._nombre = nombre#si el atributo cuenta con un _ no se debe aceder directamente  esto es solo una sugerencia al programador pero si cuenta con __ no se podra editar
        self._apellido = apellido
        self._edad = edad
        
        
    @property #decorador para poder aceder al metodo como si fuera un atributo    
    def nombre(self):#metodo get
        return self._nombre
    
    @property #decorador para poder aceder al metodo como si fuera un atributo    
    def apellido(self):#metodo get
        return self._apellido
    
    @property #decorador para poder aceder al metodo como si fuera un atributo    
    def edad(self):#metodo get
        return self._edad
    
    @apellido.setter#decorador para metodo set
    def apellido(self,apellido):#metodo set 
        self._apellido=apellido
        
    @edad.setter#decorador para metodo set
    def edad(self,edad):#metodo set 
        self._edad=edad
    
    #si quitamos el metodo set no se podra modificar el valor del atributo
    @nombre.setter#decorador para metodo set
    def nombre(self,nombre):#metodo set 
        self._nombre=nombre
        
    def mostrarDetalle(self):#metodo para imprimir el detalle de una persona
        print(f'Persona: {self._nombre} {self.apellido} {self.edad}')
        
if __name__ == '__main__':   
    persona1 = Persona('juan','perez',19)#dar valores
    #persona1._nombre= 'juan carlos'#sugerencia para el desarrollador
    #persona1.__nombre= 'juan carlos'#no se puede editar fuera del metodo self
    #persona1.mostrarDetalle()
    print(persona1.nombre)
    persona1.nombre='juan carlos'
    persona1.apellido='perez'
    persona1.edad='30'
    persona1.mostrarDetalle()


    print(__name__)