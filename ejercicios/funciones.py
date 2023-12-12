#def miFuncion(nombre, apellido):
 #   print("inicio de funcion")
 #   print(f"hola {nombre} , {apellido}")
#miFuncion("pedro", "gimenes")
#=========================================
#def sumar(a, b):
 #   return a+b

#resultado=sumar(7,3)
#print(resultado)
#==========================================
#def listarNombres(*nombres):
#   for nombre in nombres:
#        print(nombre)
#listarNombres('pedro','juan')
#==============================================
#def sumar(*args):#*args se utiliza para definir que no se sabe cuantos valores se van a utilizar
#    resultado=0
#    for numeros in args:
#        resultado += numeros
#   print(resultado)
    
#print(sumar(3,5,9))
#=================================================
#def multiplicar(*args):
#    resultado=1
#   for numeros in args:
#        resultado= resultado * numeros
#    print(resultado)
#multiplicar(3,2)
#===================================================
#def lista(**kwargs):#para elementos infinitos de tipo diccioonario 
#    for llave,valor in kwargs.items():
#        print(llave+valor)
#lista(ide='integradet',db='base de datos')
#===================================================
def nombres_lista(nombres):
    for nombre in nombres:
        print (nombre)
nombres=['juan','karla','gustavo']
nombres_lista(nombres)
nombres_lista('pedro')
nombres_lista(('11','12'))#para transformar en tupla
nombres_lista(['22','33'])# para transformar en una lista
