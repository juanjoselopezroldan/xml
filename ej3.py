# -*- coding: utf-8 -*-
from lxml import etree
doc = etree.parse('Biblioteca.xml')
raiz=doc.getroot()

bi=str(raw_input("Introduce el nombre: ")).title()

