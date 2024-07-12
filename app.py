from utilidades import *

trabajadores = ["Juan Pérez”,”María García”,”Carlos López”,”Ana Martínez”,”Pedro Rodríguez”,”Laura Hernández”,”Miguel Sánchez”,”Isabel Gómez”,”Francisco Díaz”,”Elena Fernández"]

while True:
    
    print("elija la opcion a seguir: ")
    print("1-. para asignar los sueldos aleatorios.")
    print("2-. Para Clasificar los sueldos.")
    print("3-. Ver estadisticas.")
    print("4-. Reporte de sueldos.")
    print("5-. Para salir del programa.")
    opcion=input("ingrese la opcion: ")
    
    if opcion==1:
        asignarSueldosAleatorios(sueldo)
    elif opcion==2:
        clasificarSueldos(sueldo)
    elif opcion==3:
        verEstadisticas(sueldo)
    elif opcion==4:
        reporteSueldo(producto)
    else: opcion==5
    print("saliendo del programa...")
    print("Desarrollado por Gabriel Astorga")
    print("RUT 21.860.314-9")
    break


#no se pq no me deja colocar el argumento, no cambia de color, ademas de que cuando elijo una opcion me salta autmaticamente al break