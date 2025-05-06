# programa para realizar cruces entre dos ficheros, recibiendo de entrada los nombres de cada 1 por entrada ademas de la clave de cruce indicado posicion de entrada inicial y final por fichero
# los ficheros deben estar ordenados por cla clave antes 
# la entrada seria Fichero1 cl_init1 cl_fin1 Fichero2 cl_ini2 cl_fin2


#()
#importaciones de librerias
import sys

#reicibiendo los parametros de entrada

print("Número de parámetros: " +str(len(sys.argv)))
print("Lista de argumentos: ")
print(sys.argv)

 
fichero1 = open(str(sys.argv[1]),'r')
fichero2 = open(str(sys.argv[4]),'r')

fichero1_carga = []
fichero2_carga = []

clave1_ini = int(sys.argv[2])
clave1_fin = int(sys.argv[3])

clave2_ini = int(sys.argv[5])
clave2_fin = int(sys.argv[6])


#tratar_ficheros()

def cerrar_ficheros():
    fichero1.close()
    fichero2.close()

def tratar_ficheros():
    print("******* CARGA DE FICHEROS ***********")
    
    print("******* CARGANDO FICHERO 1 ***********")
    carga_fichero(fichero1,fichero1_carga)


def carga_fichero(fichero,lista):
    linea = fichero.readline()
    while linea != '':
        print(linea, end='')
        linea = fichero.readline()    
