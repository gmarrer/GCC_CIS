#-------------------------------------------------------------------------------
# Name:        Menus.py
# Purpose:
#
# Author:      Gary
#
# Created:     10/04/2013
# Copyright:   (c) Gary 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#import tkinter
#import tkinter.messagebox
import sys

def clearScreen():
    for i in range( 1,50):
        print(" ")

def browseMenu():
    selection = "0"
    while selection != "r" :
        #clearScreen()

        print(" Browse Menu")
        print("")
        print(" a. Browse  Drama")
        print(" b. Browse Mystery")
        print(" c. Browse Sci-Fi")
        print(" d. Browse Non-Fiction")
        print(" e. Browse Biography")
        print(" f.  Browse Humor")
        print("")
        print("r - Return to Main Menu")
        print


        selection =  input("                   Enter Choice >> ")

        if selection == "a":
            clearScreen()
            print("Option A")
            #tkMessagebox.showInfo("ENtry","Option A")
        elif selection == "b":
            clearScreen()
            print("Option B")
        elif selection == "c":
            clearScreen()
            print("Option C")
        elif selection == "d":
            clearScreen()
            print("Option D")
        elif selection == "e":
            clearScreen()
            print("Option E")
        elif selection == "f":
            clearScreen()
            print("Under Construction - Humor Selected")
        elif selection == "r":
            mainMenu()
        else:
            clearScreen()
            myDisplay = str(input( "Invalid Choice = Must be a, b, c, d, e, f, R "))

def searchMenu():
	selection = "0"
	while selection != "R":
		print("Search Menu")
		print()
		print(" a. Search by Keyword")
		print(" b. Search by Title")
		print(" c. Search by Author")
		print(" d. Search by Book Type (i.e. drama, mystery, etc.)")
		print()
		print( "r - Return to Main Menu")
		print

		selection =  input("                   Enter Choice >> ")

		if selection == "a":
			clearScreen()
			print("Option A")
		elif selection == "b":
			clearScreen()
			print("Option B")
		elif selection == "c":
			clearScreen()
			print("Option C")
		elif selection == "d":
			clearScreen()
			print("Option D")
		elif selection == "r":
			mainMenu()
		else:
			clearScreen()
			myDisplay = str(input( "Invalid Choice = Must be a, b, c, d, R "))

def mainMenu():
	selection = "0"
	while selection != "q":
		clearScreen()
		print("Main Menu")
		print()
		print(" 1. Browse Books and Audio Tapes")
		print(" 2. Search Books and Audio Tapes")
		print(" 3. Checkout Shopping Cart")
		print()
		print("q to Quit program")
		print
		selection =  input("Enter Choice >> ")

		if selection == "1":
			clearScreen()
			browseMenu()
		elif selection == "2":
			clearScreen()
			searchMenu()
		elif selection == "3":
			clearScreen()
			print("Under Construction - Cart Checkout")
			msg =  input("Hit Enter to Continue")
		elif selection == "q":
			myDisplay = input(" Goodbye! ")
			sys.exit()
		else:
			# clearScreen()
			myDisplay = str(input( "Invalid Choice = Must be 1, 2, 3, Q "))
#start of python
mainMenu()
clearScreen()