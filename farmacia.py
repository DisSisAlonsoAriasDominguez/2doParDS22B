#!/usr/bin/python
# -*- coding: uft-8 -*-

import os

def menu():
	print ("Bienvenido")
	print("Selecciona una opción")
	print ("\t1 - Medicamentos Orales")
	print ("\t2 - Medicamentos inyectables")
	print ("\t3 - Soluciones de perfusion")
	print ("\t4 - Vacunas, inmunoglobulinas y sueros")
	print ("\t5 - Medicamentos de uso externo y antisépticos")
	print ("\t6 - Desinfectantes")
	print ("\t9 - salir")
 
 
while True:
	# Mostramos el menu
	menu()
 
	# solicituamos una opción al usuario
	opcionMenu = input("Inserte una opcion:  ")
 
	if opcionMenu=="1":
		print ("")
		input("1- Paracetamol 	Cantidad: 30")
		input("2- Diclofenaco 	Cantidad: 25")
		input("3- Ibuprofeno 	Cantidad: 5")
		input("4- Omeprazol 		Cantidad: 10")
		input("5- Ketorolaco 	Cantidad: 10")

	elif opcionMenu=="2":
		print ("")
		input("1- Tribedoce		Cantidad: 20")
		input("2- Ketorolaco	Cantidad: 10")
		input("3- Diclofenaco 	Cantidad: 7")
		input("4- Butormin 		Cantidad: 12")
		input("5- Neuroflax		Cantidad: 35")
	elif opcionMenu=="3":
		print ("")
		input("1- Glucosa		Cantidad: 40")
		input("2- Insotone		Cantidad: 5")
		input("3- Cloruro de Sodio 	Cantidad: 10")
		input("4- Isotonica		Cantidad: 20")
		input("5- Gelafundin 4%	Cantidad: 35")
	elif opcionMenu=="4":
		print ("")
		input("1- Suerox		Cantidad: 70")
		input("2- Electrolit	Cantidad: 80")
		input("3- Pedialyte 	Cantidad: 20")
		input("4- Inmunoglobulina Cantidad: 20")
		input("5- Gammasum UNC	Cantidad: 25")
	elif opcionMenu=="5":
		print ("")
		input("1- Alcohol		Cantidad: 40")
		input("2- Agua oxigenada	Cantidad: 35")
		input("3- Alcohol Etilico 	Cantidad: 20")
		input("4- Mycrodacin		Cantidad: 10")
		input("5- Antibenzil		Cantidad: 5")
	elif opcionMenu=="6":
		print ("")
		input("1- Desinfectante Fenolico Cantidad: 30")
		input("2- Lysol				     Cantidad: 50")
		input("3- Cif				   	 Cantidad: 10")
		input("4- Asevi					 Cantidad: 15")
		input("5- Gafidex				 Cantidad: 35")
	elif opcionMenu=="9":
		break
	else:
		print ("")
		input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")