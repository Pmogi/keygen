# keygen/PW maker
# Dec 31st 2016

import random

characterList = [1,2,3,4,5,6,7,8,9,0,'a','b','c','d','e','f','g','h','i','j','k','l','m','n']

def main():
	key = []
	
	while len(key) < 8:
		key.append(random.choice(characterList))
	
	#go through all the elements in key and make em strings
	#stackoverflow link helped a lot with making each element to a string
	#http://stackoverflow.com/questions/1614236/in-python-how-do-i-convert-all-of-the-items-in-a-list-to-floats
	
	key = [str(x) for x in key]
	
	#make key into string
	
	key = ''.join(key)
	
	print key
main()
