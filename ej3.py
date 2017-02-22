# -*- coding: utf-8 -*-
#Introduce por teclado una letra y que muestre las Bibliotecas que coinciden con esos caracteres introducidos.
from lxml import etree
doc = etree.parse('Biblioteca.xml')
raiz=doc.getroot()

bi=str(raw_input("Introduce el nombre: ")).title()
no="false"
for biblioteca in raiz:
    if bi in biblioteca.find("nombre").text:
        print "La Biblioteca se llama:",biblioteca.find("nombre").text
        no="true"
if no=="false":
    print "Biblioteca no encontrada"