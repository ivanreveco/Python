class persona:
    def __init__(self,nombre):
        self.nombre = nombre
    def __add__(self, other):
        return self.nombre + other.nombre
#obj1 + obj2
#obj1.__add__(obj2)
persona1 = persona("juan")
persona2 = persona("pedro")
print(persona1+persona2)
