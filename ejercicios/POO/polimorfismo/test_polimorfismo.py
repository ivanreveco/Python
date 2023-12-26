from Empleado import Empleado
from Gerente import Gerente

def imprmir_detalles(objeto):
    print(objeto)
    print(type(objeto))
    
empleado = Empleado('juan',5000)
imprmir_detalles(empleado)

gerente = Gerente('karla',6000,'sistemas')

imprmir_detalles(gerente)