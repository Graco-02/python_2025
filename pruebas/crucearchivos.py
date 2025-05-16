# programa para realizar cruces entre dos ficheros, recibiendo de entrada los nombres de cada 1 por entrada ademas de la clave de cruce indicado posicion de entrada inicial y final por fichero
# los ficheros deben estar ordenados por cla clave antes 
# la entrada seria Fichero1 cl_init1 cl_fin1 Fichero2 cl_ini2 cl_fin2


#()
#importaciones de librerias
import sys

def set_salto_linea():
    print()
    print()

def cerrar_ficheros():
    fichero1.close()
    fichero2.close()


def set_listar_existentes_inexistentes(listafichero1,listafichero2):
    existentes = open("archivos\existentes.txt", "w")
    inexistentes = open("archivos\inexistentes.txt", "w")

    for x in listafichero1:
        if x in listafichero2:
            if len(str(x)) == 19:
                print("clave existente : " + str(x))
                existentes.write(str(listafichero1.get(str(x))))
        else:
            if len(str(x)) == 19:
                print("clave inexistente : " + str(x))
                inexistentes.write(str(listafichero1.get(str(x))))

def tratar_ficheros(fichero1,clave1_ini,clave1_fin,fichero2,clave2_ini,clave2_fin):
    print("******* CARGA DE FICHEROS ***********")
    print("******* CARGANDO FICHERO 1 ***********")
    listafichero1 = carga_fichero(fichero1,clave1_ini,clave1_fin)
    set_salto_linea()
    print("******* CARGANDO FICHERO 2 ***********")
    listafichero2= carga_fichero(fichero2,clave2_ini,clave2_fin)

    set_salto_linea()
    print(type(listafichero1))
    print(type(listafichero2))
    set_salto_linea()
    set_listar_existentes_inexistentes(listafichero1,listafichero2)


def carga_fichero(fichero,clave_ini,clave_fin):
    lista = {}
    linea = fichero.readline()
    lista[str(linea[clave_ini:clave_fin])] = str(linea)    
    while linea != '':
        print(linea, end='')
        linea = fichero.readline()
        lista[str(linea[clave_ini:clave_fin])] = str(linea)    
    return  lista   


######################################################################
#reicibiendo los parametros de entrada
total_de_parametros = len(sys.argv)

print("Número de parámetros: " +str(total_de_parametros))
print("Lista de argumentos: ")
print(sys.argv)

if(total_de_parametros == 7):
    fichero1 = open(str(sys.argv[1]),'r')
    fichero2 = open(str(sys.argv[4]),'r')

    fichero1_carga = []
    fichero2_carga = []

    clave1_ini = int(sys.argv[2])
    clave1_fin = int(sys.argv[3])

    clave2_ini = int(sys.argv[5])
    clave2_fin = int(sys.argv[6])

    try:
        tratar_ficheros(fichero1,clave1_ini,clave1_fin,fichero2,clave2_ini,clave2_fin)
        cerrar_ficheros()
    except:
        print("Error al llamar parafo tratar_ficheros")
else:
    set_salto_linea()
    print("-------------------------------------------")
    print("Número de parámetros Erroneo, debe ser 6")
    print("ARCHIVO1,Inic_clave1,Fin_clave1,ARCHIVO2,Inic_clave2,Fin_clave2")
    print("-------------------------------------------")


