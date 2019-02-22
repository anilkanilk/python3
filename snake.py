import random
#this is a dictionary
d={5:37,13:2,13:34,28:4,38:9,40:48,56:68,75:76,75:85,85:65,85:98}


k=random.choice([2,5,13,48,56,85])

print("you got",k)

if k in d:
	if k>d[k]:
		print("snake")
	else:
		print("ladder")

	print("you can go to",k)