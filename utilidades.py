import random
import csv
trabajadores = ["Juan Pérez”,”María García”,”Carlos López”,”Ana Martínez”,”Pedro Rodríguez”,”Laura Hernández”,”Miguel Sánchez”,”Isabel Gómez”,”Francisco Díaz”,”Elena Fernández"]
#definimos la funcion para asignar los sueldos aleatorios
def asignarSueldosAleatorios(sueldo):
    for x in trabajadores:
        sueldo = random.uniform(300000, 2500000)
        sueldo=sueldo.append()

#los casificamos, es decir que motramos los que son menores a un numero o mayores.
def clasificarSueldos(sueldo):
    if sueldo < 800000:


def verEstadisticas(sueldo):
    print()

def reporteSueldo(sueldo):
    print()

#No se porque me mando tantos errores... las lineas rojas debajo del def.