#class Persona:
#    def __init__(self):#inicializar
#        self.nombre = 'juan'#agregar atributos
#        self.apellido = 'enriquez'
#        self.edad = 19
#persona1 = Persona()
#print(persona1.edad)#para aceder a un atributo

class Persona:
    def __init__(self ,nombre, apellido, edad):#inicializar
        self.nombre = nombre#agregar atributos
        self.apellido = apellido
        self.edad = edad
        
    def mostrarDetalle(self):#metodo para imprimir el detalle de una persona
        print(f'Persona: {self.nombre} {self.apellido} {self.edad}')
        
        
persona1 = Persona('juan','perez',19)#dar valores

persona2 = Persona('karla','gomez',30)
persona1.nombre = 'jose'#cambiar el nombre ya establecido

persona1.mostrarDetalle()

persona2.mostrarDetalle()

Persona.mostrarDetalle(persona2)#otra forma de llamar a un metodo