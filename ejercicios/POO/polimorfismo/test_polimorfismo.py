from Empleado import Empleado
from Gerente import Gerente

def imprmir_detalles(objeto):
    print(objeto)
    print(type(objeto))
    
    if isinstance(objeto, Gerente):# hace referencia a que si es una instancia de un objeto en este caso gerente que te imprima el departamento de lo contrario no lo hara
        print(objeto.departamento)
    
empleado = Empleado('juan',5000)
imprmir_detalles(empleado)

gerente = Gerente('karla',6000,'sistemas')

imprmir_detalles(gerente)