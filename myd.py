import random

def myd():
	a = random.randint(1, 10)

	if a <= 7:
		x = random.randint(10, 25)

	elif a == 8:
		x = random.randint(0, 10)

	else:
		x = random.randint(25, 40)


	if x in range(30, 41):
		emote = "WutFace"

	elif x in range(20, 31):
		emote = "TriHard"

	elif x in range(12, 21):
		emote = "SeemsGood"

	elif x in range(7, 13):
		emote = "haHAA"

	else:
		emote = "MingLee"

	return str(x) + " cm long " + emote