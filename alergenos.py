# -*- coding: utf-8 -*-
import os, sys, csv




def __main__():

    os.system('clear')
    print "\n#########################################################################"
    print "#Bienvenido al programa de gestion de alergenos y ingredientes. \n#"
    print "#                       Escrito por Israel Perez Valero. \n########################################################################## \n"
    print "1. Añadir productos al listado de ingredientes. \n"
    print "ESC para terminar \n"
    eleccion = False
    while eleccion == False:
        eleccion = str(raw_input("Elige tu opcion: "))
        if eleccion == "1":
            os.system('clear')
            eleccion = True
            listaIngredientes()
        elif eleccion == "ESC":
            os.system('clear')
            print "Gracias por usarme, hasta la proxima."
            sys.exit()




def listaIngredientes():

    fichero = open("Listadoingredientes.csv", "a")
    print ""
    print ""
    print ""
    print ""
    print "Por favor, introduce los productos en el siguiente orden."
    print "Producto, ingredientes, alergenos"
    print "Introduce 'ESC' en mayusculas para terminar"
    print "muchas gracias"
    print ""
    print ""
    print ""

    producto = " "
    while producto != "ESC":
        producto = raw_input("Introduce el siguiente producto: ")
        if producto != "ESC":
            fichero.write(producto + "\n")

    fichero.close()
    print "gracias"
    __main__()

def listaAlergenos():
    fileRead = open('Listadoingredientes.csv', "r")
    read = csv.reader(fileRead)
    fileWrite = open('Alergenos.txt', "w")
    for row in read:
        fileWrite.write(row[0]+":\n")
        fileWrite.write("Alergenos: "+row[2]+"\n\n")
    fileRead.close()
    fileWrite.close()
    print "Archivo creado correctamente.\n"
    pausa2 = False
    while pausa2 == False:
        pausa = raw_input("Pulsa 'Enter' para continuar.....")
        if pausa == "":
            pausa2 = True
    __main__()
__main__()


