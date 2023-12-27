from dispositivo_entrada import *

class Raton(DispositivoEntrada):
    
    
    contador_raton = 0
    def __init__(self, marca, tipo_entrada):
        Raton.contador_raton +=1
        self._id_raton = Raton.contador_raton
        super().__init__(marca, tipo_entrada)
        
    def __str__(self):
        return f'Id: {self._id_raton}, Marca: {self._marca}, Tipo_entrada: {self._tipo_entrada} '
if __name__ == '__main__':    
    raton1 = Raton('logitech', 'USB')
    print(raton1)