# -*- coding: utf-8 -*-
#Introduce por teclado dia y hora y que muestre las bibliotecas que abren ese dia a esa hora, junto con su direccion y su localizacion en el mapa.
from lxml import etree
doc = etree.parse('Biblioteca.xml')
raiz=doc.getroot()
horario=raiz.find("biblioteca/horario")


dia=raw_input("Introduce un dia de la semana: ")
hora=int(raw_input("Introduce la hora 24H para ver que biblioteca esta abierta: "))
no="false"
for cod in raiz:
    for codigo in cod:
        for dias in codigo:
            lista=dias.text.split("-")
            horain=int(lista[0].split(":")[0])
            horafin=int(lista[1].split(":")[0])
            if dias.tag==dia and horain<=hora and horafin>=hora:
                print "-La Biblioteca se llama:",codigo.getparent().find("nombre").text
                print "-Tiene la siguiente direccion:",codigo.getparent().find("direccion").text
                print "Su URL es la siguiente: http://www.openstreetmap.org/#map=19/",codigo.getparent().find("latitud").text,"/",codigo.getparent().find("longitud").text
                print 10*"-"
                no="true"
if no=="false":
    print "No hay ninguna biblioteca que este abierta ese dia a esa hora"
