import random

class Game(object):

	def __init__(self, first_turn, word_list):

		if first_turn == 'R':
			self.board = make_random_board(5,5, num_reds=9, num_blues=8, word_list=word_list)
		elif first_turn == 'B':
			self.board = make_random_board(5,5, num_reds=8, num_blues=9, word_list=word_list)

		self.current_turn = first_turn
		self.game_is_over = False

		self.start_prompt()

		self.next_turn()


	def next_turn(self):


		current_turn_prompt = '\nCURRENT TURN: %s' % self.current_turn
		print(current_turn_prompt)
		print('')
		print(self.board)
		
		clue, remaining_guesses = self.get_clue()

		remaining_guesses = int(remaining_guesses)

		while remaining_guesses > 0:
			guess = self.get_guess()

			if guess in ['q','Q']:
				break
			else:
				result = self.guess_word(guess)

				print('Guess result: ' + result + '\n')

				if result in ['GAME OVER', 'WRONG']:
					break

				elif result == 'RIGHT':
					remaining_guesses -= 1

				elif result == 'WORD NOT IN GRID':
					pass
				
				print(self.board)

		self.switch_turn()

		if self.game_is_over:
			print(self.board)
			print('WINNER', self.current_turn, '!')
		else:
			self.next_turn()


	def get_clue(self):
		clue = input('Enter clue:\n')
		number = input('Enter number:\n')
		return clue, number

	def get_guess(self):
		return input("Enter guess ('q' to pass):\n")
		

	def guess_word(self, word):

		for square in self.board.get_all_squares():
			if word == square.word:
				square.shown = True
				if square.color == 'X':
					self.game_is_over = True
					return 'GAME OVER'
				elif square.color == self.current_turn:
					return 'RIGHT'
				else:				 # split into two cases
					return 'WRONG'
		return 'WORD NOT IN GRID'


	def switch_turn(self):
		if self.current_turn == 'B':
			self.current_turn = 'R'
		else:
			self.current_turn = 'B'

	def start_prompt(self):
		print('\n'*50)
		input('Press enter when clue givers ready...\n')

		print('BOARD STATE:')
		print(self.board.full_display())
		print()
		input('Press enter when clue givers have written down board')
		print('\n'*50)

	def view_full_board(self):
		print(self.board.full_display())



class Board(object):

	def __init__(self, num_rows, num_columns):

		self.rows = [
					[Square() for r in range(num_rows)]
						for c in range(num_columns)]

	def get_square_at_index(self, r, c):
		return self.rows[r][c]

	def set_word_at_index(self, r, c, word):
		self.rows[r][c].word = word

	def set_color_at_index(self, r, c, color):
		self.rows[r][c].color = color

	# return a list of all squares
	def get_all_squares(self):
		return [s for row in self.rows for s in row]

	def __str__(self):
		col_width = 20
		to_return = ''
		for row in self.rows:
			row_string = ''
			for i, square in enumerate(row):
				row_string += square.appearance()
				dist_to_next_col = (col_width * (i+1)) - len(row_string)
				if dist_to_next_col > 0:
					row_string += dist_to_next_col * ' '
			to_return += row_string + '\n'
		return to_return


	def full_display(self):
		col_width = 20
		to_return = ''
		for row in self.rows:
			row_string = ''
			for i, square in enumerate(row):
				row_string += square.full_string()
				dist_to_next_col = (col_width * (i+1)) - len(row_string)
				if dist_to_next_col > 0:
					row_string += dist_to_next_col * ' '
			to_return += row_string + '\n'
		return to_return


class Square(object):

	def __init__(self, word=None, color=None):

		self.word = word
		self.color = color
		self.shown = False

	def appearance(self):
		return self.color if self.shown else self.word

	def full_string(self):
		color = self.color.upper() if self.shown else self.color.lower()
		return '%s - %s' % (color.upper(), self.word)


def make_random_board(num_rows, num_columns, num_reds, num_blues, word_list):

	board = Board(num_rows, num_columns)
	unused_squares = [(r,c) for c in range(num_columns) for r in range(num_rows)]

	# Fill board randomly with specified numbers
	for red in range(num_reds):
		r, c = random.choice(unused_squares)
		board.set_color_at_index(r,c, 'R')
		unused_squares.remove((r,c))

	for blue in range(num_blues):
		r, c = random.choice(unused_squares)
		board.set_color_at_index(r,c, 'B')
		unused_squares.remove((r,c))

	r, c = random.choice(unused_squares)
	board.set_color_at_index(r,c, 'X')
	unused_squares.remove((r,c))

	for r, c in unused_squares:
		board.set_color_at_index(r,c, 'O')

	# Fill board with words
	wordgetter = iter(word_list)
	random.shuffle(word_list)

	for row in board.rows:
		for square in row:
			square.word = wordgetter.__next__()

	return board






if __name__ == '__main__':

	with open('resources/nouns.txt') as f:
		words = [line.strip() for line in f.readlines()]

	g = Game('R', words)
	#b = make_random_board(5,5,9,8, words)

	#print(b)
	#print(b.full_display())
	#print(b.get_all_squares())
	



	