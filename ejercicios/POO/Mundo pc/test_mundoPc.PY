from Teclado import *
from Raton import *
from Computadora import *
from Monitor import *
from Orden import *

teclado1= Teclado('REDDRAGON', 'USB')     
raton1= Raton('HP','USB')  
monitor1=Monitor('LG',15)
computadora1=Computadora('HP',monitor1,teclado1,raton1)

teclado2= Teclado('logitech', 'USB')     
raton2= Raton('razer','USB')  
monitor2=Monitor('LG',15)
computadora2=Computadora('HP',monitor1,teclado1,raton1)

computadoras1=[computadora1,computadora2]
orden1 = Orden(computadoras1)

print(orden1)