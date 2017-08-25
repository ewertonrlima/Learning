import random

def main ():

'comment added for test purpose

	print "Este jogo ajuda voce a adivinhar um numero"
	print "Digite um numero e depois Enter"
	randonnumber = random.randint(1,100)
	found = False # flag variable

	while not found:

		userguess = input("Digite o numero:  ")
		if userguess == randonnumber:
			print "Parabens esquilinho o numero era" randonnumber
			found = True
			print "Obrigado por jogar conosco"

		elif	userguess > randonnumber:
			print "Tente um numero MENOR"
		else: print "Tente um numero MAIOR"



if __name__ == "__main__":
	main()
