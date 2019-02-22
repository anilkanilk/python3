import random
p=0
d=0

while True:
	r=input("press r to roll: ")
	
	if r=="r":
		d=random.randint(1,6)
		print("you got: ",d)

	if d==1 or d==6:
		p=d
		break

print("congratulations,you are in the game.you are at",p)
