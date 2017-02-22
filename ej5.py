# -*- coding: utf-8 -*-
#Introduce por teclado el codigo de la biblioteca y que muestre el nombre, la direccion, la descripcion del mismo y sus coordenadas en una url para poder acceder a la ubicacion.
from lxml import etree
doc = etree.parse('Biblioteca.xml')
raiz=doc.getroot()

dia=raw_input("Introduce el dia: ")
