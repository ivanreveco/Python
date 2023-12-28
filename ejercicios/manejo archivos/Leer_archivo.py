try:
    archivo=open('prueba.txt','r')#r para lectura a para agregar informacion x par crear
    print(archivo.read())
except Exception as e:
    print('hubo un error')
finally:
    print("fin del proceso ")