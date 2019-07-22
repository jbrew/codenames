import random
from model.game import Game



if __name__ == '__main__':

	#print('\033[94m This is red text \033[0m')
	
	with open('resources/colorado.txt') as f:
		words = [line.strip() for line in f.readlines()]

	g = Game('R', words)





	