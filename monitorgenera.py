#!/usr/bin/python
# -*- coding: utf-8 -*-
#EDGAR ESPINOSA OCTUBRE 2021
#github.com/eddgar10/codigosdebarrapersonalizado
#fuentes: 
#https://www.geeksforgeeks.org/how-to-generate-barcode-in-python/
#https://www.geeksforgeeks.org/read-a-file-line-by-line-in-python/
#https://barcode-labels.com/getting-started/barcodes/types/
#https://www.geeksforgeeks.org/python-randint-function/
#https://www.mclibre.org/consultar/python/lecciones/python-for.html
#https://www.programiz.com/python-programming/methods/string/strip
#https://careerkarma.com/blog/python-compare-strings/
#https://programminghistorian.org/es/lecciones/trabajar-con-archivos-de-texto

# importar biblioteca EAN13 de modulo barcode

from barcode import Code128
  
# import ImageWriter para generar un archivo imagen

from barcode.writer import ImageWriter

#importar biblioteca aleatoria

import random

cantidadagenerar= input("cantidad de codigos a generar: ")#en esta variable se asignan la cantidad de codigos nuevos a generar leidos de teclado

banderaexistente = 0 #bandera que determina si el codigo ya ha sido generado para evitar duplicarlo

#generando N cantidad de codigos leida

for i in range(int(cantidadagenerar)):
    textocodigo=("SERV"+str(random.randint(0,9))+"M"+str(random.randint(10,99))+"O"+str(random.randint(100,999))+"N") #sintaxis de codigo genrado: "SERV"+ 0-9 + M + 10-99 + O + 100-999 + N
    print ("codigo nuevo generado: "+textocodigo)
    print("Buscando codigo repetido... ")
    buscarepetido = open('codigosgeneradosmonitor.txt', 'r')	#apertura de archivo existente para realizar busqueda de codigo generado
    Lines=buscarepetido.readlines()		#apertura de archivo para lectura liena a linea
    for line in Lines:
        if textocodigo == line.strip():	#comparacion codigo generado con linea leida de archivo cpu
            banderaexistente = 1		#indica que el codigo generado ya existia en el archivo
            print("el codigo ya existe en la lista \n")
            break
        else:
            banderaexistente = 0      	#indica que el codigo generado no existe en el archivo
    buscarepetido.close()			#cierre de archivo de lectura	
    if banderaexistente == 0:			#bandera en 0 = no existe codigo generado en archivo
        escribenuevocodigo=open('codigosgeneradosmonitor.txt','a')	#apertura de archivo para a??adir el nuevo codigo generado a la lista
        print("codigo nuevo agregado: "+textocodigo)
        print ("*********************")
        escribenuevocodigo.write(textocodigo+"\n")
        escribenuevocodigo.close()		#cierre de archivo despues de a??adir el nuevo codigo
        my_code = Code128(textocodigo, writer=ImageWriter())	#generacion de imagen con codigo de barras para el nuevo codigo generado 
        my_code.save("MON"+textocodigo)			#escritura de file imagen con el codigo de barras


   

