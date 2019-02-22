#Snake and Ladders game!
import random

d = 0
p = 0

#Dictionary for snake and ladders.
snl={8:37,13:34,40:68,52:81,76:97,38:9,25:4,11:2,65:46,89:70,93:64}

#function to roll dice.
def roll():
	return random.randint(1,6)

#to get 1 or 6 to start the game.
while True:
	menu = input("Press r to roll and q to quit")
	if menu == "r":
		d = roll()
		print("You got ", d)

	if menu == "q":
		print("Thank you")
		quit()

	if d == 1 or d == 0:
		p = p+d
		print("Congratulations! You are int the game.")
		print ("you are at positon", p)
		break
	else:
		print("You need to get 1 or 6 to get in the game.")
#to change position in game based on dice value.
while True:
	menu = input("Press r to roll again")

	if menu == "r":
		d = roll()
		print("You got:", d)
		p = p+d

		if p ==100:
			print("You are at 100.\nHurray! You won the game!")
			exit()

		#Winning banner 
		if p>100:
			p= p-d
			print("You should get ", 100-p,"or less to make a move!")

		print("You are at", p)

		#Snake and ladders  
		if p in snl:
			if p < snl[p]:
				print("You climbed a ladder")
			if p > snl[p]:
				print("You got bitten by a snake")
			p = snl[p]
			print("Move to",p)
	#quitting option
	elif menu == "q":
		print("Thanks for playing.")
quit()
