
try:
    archivo = open('prueba.txt','w', encoding='utf8')#w es para escribir de w
    archivo.write('hola mi sangre')
    archivo.write('\nadios')
except Exception as e:
    print(e)
finally:
    archivo.close()