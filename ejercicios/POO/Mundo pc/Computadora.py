from Teclado import Teclado
from Raton import Raton
from Monitor import Monitor


class Computadora:
    contador_computadoras=0
    
    def __init__(self,nombre,monitor,teclado,raton):
        Computadora.contador_computadoras+=1
        self._id_computadora=Computadora.contador_computadoras
        self._nombre=nombre
        self._monitor=monitor
        self._teclado=teclado
        self._raton=raton
    
    def __str__(self):# 3 comillas para poder escribir en distinta lineas hacia abajo sin necesidad de usar el salto de linea de python(\n)
        return f'''
        {self._nombre}: {self._id_computadora}
        monitor: {self._monitor}
        teclado: {self._teclado}
        raton: {self._raton}
        '''
if __name__ =='__main__':    
    teclado1= Teclado('REDDRAGON', 'USB')     
    raton1= Raton('HP','USB')  
    monitor1=Monitor('LG',15)
    computadora1=Computadora('HP',monitor1,teclado1,raton1)

    print(computadora1)
