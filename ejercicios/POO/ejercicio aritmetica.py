class Aritmetica:
    """
    Clase aritmetica para realizar operaciones de sumar restar etc
    """
    def __init__(self,operandoA, operandoB):
        self.operandoA= operandoA
        self.operandoB= operandoB
        
    def sumar(self):
        return self.operandoA+ self.operandoB
    def restar(self):
        return self.operandoA-self.operandoB
    def multiplicar(self):
        return self.operandoA*self.operandoB
    def dividir(self):
        return self.operandoA/self.operandoB
Aritmetica1= Aritmetica(5,3)
print(f"suma: {Aritmetica1.sumar()}")
print(f"resta :{Aritmetica1.restar()}")
print(f"multiplicacion: {Aritmetica1.multiplicar()}")
print(f"divicion: {Aritmetica1.dividir():.2f}")#.2f para mostrar solo 2 decimales
################################################################################################
################################################################################################
class AreaRectangulo:
    """
    Clase para calcular el area de un rectangulo
    """
    def __init__(self, base, altura):
        self.base=base
        self.altura=altura
    def calcularArea(self):
        return self.altura*self.base
    
print("ingrese la base del rectangulo")
base1=int(input())
print("ingrese la altura del rectangulo")
altura1=int(input())

arearectangulo=AreaRectangulo(base1,altura1)

print(f"el area del rectangulo es: {arearectangulo.calcularArea()}")
