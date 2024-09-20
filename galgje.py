#
# Programma: Galgje
# Module: 	 [S1-2] Programmeren 1
# ICT Academie Apeldoorn
#

import random

def kies_woord_intern():
	# kies een woord uit de interne woordenlijst
	woordenlijst = [ "boek", "computer", "beeldscherm","toetsenbord", "python", "ICTAcademieApeldoorn"]
	woord = random.choice(woordenlijst)
	return woord.strip().upper()

def kies_woord_uit_bestand():
	with open("woordenlijst.txt", 'r') as fp:
		woordenlijst = fp.readlines()

	index = random.randint(0, len(woordenlijst) - 1)
	woord = woordenlijst[index].strip().upper()
	return woord

def print_woord(woord,geraden):
	for letter in woord:
         if letter in geraden:
             print(letter, end="")
         else:
             print("_", end="")
         print(" ", end="")
	print("")

def vraag_letter(gebruikt):
     while True:
         nieuwe_letter = input("Type een letter: ").upper()

         if nieuwe_letter in gebruikt:
             print("Al gebruikt. Probeer het nogmaals")
         else:
             return nieuwe_letter

def nog_letters_te_raden(woord,geraden):
	if len(geraden) == 0:
		return True

	for letter in woord:
		if letter in geraden:
			continue
		else:
			return True
	return False

def nieuwe_letter_in_woord(nieuweletter,woord):
	if nieuweletter in woord:
		return True
	else:
		return False

def speel_galgje():
	max_pogingen = 5
	aantal_pogingen = 0
	geraden = []
	gebruikt = []
	woord = kies_woord_intern()
	print("Welkom bij Galgje. Ik heb een woord gekozen...")
	while aantal_pogingen < max_pogingen and nog_letters_te_raden(woord,geraden) == True:
		print_woord(woord, geraden)
		nieuwe_letter = vraag_letter(gebruikt)
		gebruikt.append(nieuwe_letter)

		if nieuwe_letter_in_woord(nieuwe_letter,woord) == False:
			aantal_pogingen = aantal_pogingen + 1
			print("Je hebt nog " + str(max_pogingen - aantal_pogingen) + " pogingen over")
		else:
			geraden.append(nieuwe_letter)

	print("Het woord is: " + woord)
	if aantal_pogingen < max_pogingen:
		print("Gefeliciteerd!")


speel_galgje()