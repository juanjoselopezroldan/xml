# -*- coding: utf-8 -*-
from lxml import etree
doc = etree.parse('Biblioteca.xml')
raiz=doc.getroot()

bi=raw_input("Introduce la ID: ")

for codigo in raiz:
    if codigo.find("idbiblio").text==bi:
        print "-La Biblioteca se llama:",codigo.find("nombre").text
        print "-Tiene la siguiente direccion:",codigo.find("direccion").text
        print "-Informacion sobre la Biblioteca:",codigo.find("descripcion").text
        print "Su URL es la siguiente: http://www.openstreetmap.org/#map=19/",codigo.find("latitud").text,"/",codigo.find("longitud").text