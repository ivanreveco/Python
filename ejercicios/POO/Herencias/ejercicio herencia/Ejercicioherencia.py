class vehiculo:
    def __init__(self,color,ruedas):
        self._color = color
        self._ruedas = ruedas
    def __str__(self):#metodo para sobre escribir
        return f"color: {self._color}\nruedas: {self._ruedas}"
    #metodos get   
    @property
    def color(self):
        return self._color
    @property 
    def ruedas(self):
        return self._ruedas
    
    #metodos set 
    @color.setter
    def color(self,color):
        self._color=color
    @ruedas.setter
    def color(self,ruedas):
        self._ruedas=ruedas
        
class coche(vehiculo):
    def __init__(self,color,ruedas,velocidad):
        super().__init__(color,ruedas)#PARA TRAER ATRIBUTOS DE LA CLASE PADRE VEHICULO
        self._velocidad= velocidad
    
    def __str__(self):
        return f'{super().__str__()}velocidad: {self._velocidad}'
    
    #metodo get
    @property
    def velocidad(self):
        return self._velocidad
    
    #metodo set
    
    @velocidad.setter
    def velocidad(self,velocidad):
        self._velocidad = velocidad

class bicicleta(vehiculo):#siempre especificar la clase padre
    def __init__(self,color,ruedas,tipo):
        super().__init__(color, ruedas)
        self._tipo = tipo
    def __str__(self):
        return f"{super().__str__()}tipo: {self._tipo}"
    #metodo get
    @property 
    def tipo(self):
        return self._tipo
    
    #metodo get
    @tipo.setter
    def tipo(self,tipo):
        self._tipo = tipo

Vehiculo = vehiculo('rojo',4)

Coche = coche('Azul',4 ,50)

Bicicleta = bicicleta('naranja',2,"montain bike")
    
print(Coche)

print(Bicicleta)

print(Vehiculo)