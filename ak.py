import random

i=0
while i<2:
	d=6

	r=input("press r to roll,press q to quit: ")
	if r=="r":
		print("you got;",d)
		d=d/3

	r=input("press r to roll,press q to quit: ")
	if r=="r":
		print("you got;",d)
		d=d+1
		
	r=input("press r to roll,press q to quit: ")
	if r=="r":
		print("you got;",d)
	i=i+1
print("hurray!you won")