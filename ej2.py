# -*- coding: utf-8 -*-
#Lista la cantidad de Bibliotecas existentes.
from lxml import etree
doc = etree.parse('Biblioteca.xml')
raiz=doc.getroot()
contador=0
for biblio in raiz:
    contador=contador+1

print "La cantidad de bibliotecas es de: ",contador
