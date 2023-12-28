from ManejoArchivos import ManejoRecursos

try:
   # with open('prueba.txt','r',encoding='utf8') as archivo: 
    with ManejoRecursos('prueba.txt') as archivo:
        print(archivo.read())
        
except Exception as e:
    print("algo salio mal")
    