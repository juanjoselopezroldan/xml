# -*- coding: utf-8 -*-
#Introduce por teclado el nombre de una biblioteca y que muestre el horario.
from lxml import etree
doc = etree.parse('Biblioteca.xml')
raiz=doc.getroot()

bi=str(raw_input("Introduce el nombre: ")).title()
horario=raiz.find("biblioteca/horario")

for biblioteca in raiz:
    if bi in biblioteca.find("nombre").text:
        print "La Biblioteca se llama:",biblioteca.find("nombre").text
        print "Tiene un horario de: "
        for hora in horario:
            print "Dia",hora.tag,"tiene un horario de ",hora.text