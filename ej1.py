# -*- coding: utf-8 -*-
#Lista las Bibliotecas.
from lxml import etree
doc = etree.parse('Biblioteca.xml')
raiz=doc.getroot()

for biblio in raiz:
    print biblio.find("nombre").text
