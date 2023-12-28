from dominio.pelicula import Pelicula
from servicio.catalogo import Catalogo as cp
opcion = None
while opcion != 4:
    try:
        print('Opciones: ')
        print('1. Agregar Pelicula')
        print('2. Listar Pelicula')
        print('3. Eliminar Pelicula')
        print('4. Salir')
        
        opcion= int(input('Seleccione su opcion: '))
        
        if opcion ==1:
            nombre_pelicula= input("nombre de la pelicula:  ")
            pelicula = Pelicula(nombre_pelicula)
            cp.agregar_pelicula(pelicula)
        elif opcion ==2:
            cp.listar_peliculas()
        elif opcion ==3:
            cp.eliminar_pelicula()
            
    except Exception:
        print("ocurrio un error")
        opcion = None
        
else:
    print('saliendo del programa')