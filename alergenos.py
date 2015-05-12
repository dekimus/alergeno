#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys, csv



def __main__():

    """Funcion principal del programa que gestiona el menu principal"""

    os.system('clear')
    print "\n#########################################################################"
    print "#Bienvenido al programa de gestion de alergenos y ingredientes. \n#"
    print "#                       Escrito por Israel Perez Valero. \n########################################################################## \n"
    print "1. Añadir productos al listado de ingredientes. \n2. Crea un archivo con los Productos y alergenos."
    print "3. Mostrar el listado de ingredientes.\n\nTeclea ESC en mayuscula para terminar... \n"
    eleccion = False
    while eleccion == False:
        eleccion = raw_input("Elige tu opcion: ").upper()
        if eleccion == "1":
            os.system('clear')
            eleccion = True
            listaIngredientes()
        elif eleccion == "2":
            os.system('clear')
            eleccion = True
            listaAlergenos()
        elif eleccion == "ESC":
            os.system('clear')
            print "Gracias por usarme, hasta la proxima."
            sys.exit()
        elif eleccion == "3":
            eleccion == True
            os.system('clear')
            mostrarArchivo()
        else:
            print "Introduce un valor valido por favor\n"
            eleccion = False




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
    pausa()

def listaAlergenos():
    """Genera un archivo.txt con la lista de ingredientes y alergenos"""

    try:
        fileRead = open('Listadoingredientes.csv', "r")
    except:
        print "Listado de ingredientes no encontrado, crea uno primero por favor."
        pausa()

    read = csv.reader(fileRead)
    fileWrite = open('Alergenos.txt', "w")
    for row in read:
        fileWrite.write(row[0]+":\n")
        for letra in range(len(row[0])):
            fileWrite.write("--")

        fileWrite.write("\nAlergenos: "+row[2]+"\n\n")
    fileRead.close()
    fileWrite.close()
    print "Archivo creado correctamente.\n"
    pausa()

def pausa():
    """Genera una pausa hasta que se pulse enter
    y vuelve al main"""

    pausa2 = False
    while pausa2 == False:
        pausa = raw_input("Pulsa 'Enter' para continuar.....")
        if pausa == "":
            pausa2 = True
    __main__()

def mostrarArchivo():
    """Funcion encargada de listar el archivo de ingredientes"""

    try:
        fileRead = open('Listadoingredientes.csv', "r")
    except:
        print "Listado de ingredientes no encontrado, genera uno primero por favor"
        pausa()
    read = csv.reader(fileRead)
    for row in read:
        print "  ".join(row)+"\n"
    pausa()

__main__()
