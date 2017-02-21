# -*- coding: utf-8 -*-
from lxml import etree
doc = etree.parse('Biblioteca.xml')
raiz=doc.getroot()

bi=raw_input("Introduce la ID: ")

for codigo in raiz:
    if codigo.find("idbiblio").text==bi:
        print "-La Biblioteca se llama:",codigo.find("nombre").text
        print "-Tiene la siguiente direccion:",codigo.find("direccion").text