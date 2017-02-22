# -*- coding: utf-8 -*-
#Introduce por teclado el codigo de la biblioteca y que muestre el nombre, la direccion, la descripcion del mismo y sus coordenadas en una url para poder acceder a la ubicacion.
from lxml import etree
doc = etree.parse('Biblioteca.xml')
raiz=doc.getroot()

dia=raw_input("Introduce el dia: ")

for cod in raiz:
    for codigo in cod:
        for dias in codigo:
            if dias.tag==dia:
                print "-La Biblioteca se llama:",codigo.getparent().find("nombre").text
                print "-Tiene la siguiente direccion:",codigo.getparent().find("direccion").text
                print "Su URL es la siguiente: http://www.openstreetmap.org/#map=19/",codigo.getparent().find("latitud").text,"/",codigo.getparent().find("longitud").text
