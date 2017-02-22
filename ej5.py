# -*- coding: utf-8 -*-
#Introduce por teclado dia y que muestre las bibliotecas que abren ese dia, junto con su direccion y su localizacion en el mapa.
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
