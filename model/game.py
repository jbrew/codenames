import random
from model.board import Board


class Game(object):

	def __init__(self, first_turn, word_list):

		self.savepath = 'saved/most_recent.txt'

		if first_turn == 'R':
			self.board = self.make_random_board(5,5, num_reds=9, num_blues=8, word_list=word_list)
		elif first_turn == 'B':
			self.board = self.make_random_board(5,5, num_reds=8, num_blues=9, word_list=word_list)

		self.current_turn = first_turn
		self.game_is_over = False
		self.start_prompt()
		self.next_turn()


	def next_turn(self):

		self.save_game_to_file()
		current_turn_prompt = '\nCURRENT TURN: %s' % self.current_turn
		print(current_turn_prompt)
		print('')
		print(self.board)
		
		clue, remaining_guesses = self.get_clue()
		remaining_guesses = int(remaining_guesses)
		print('\n\n')

		while remaining_guesses > 0:
			print(remaining_guesses, 'guesses remaining')
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

		print('Finished guessing!\n')

		self.switch_turn()

		if self.game_is_over:
			print(self.board)
			print('WINNER', self.current_turn, '!')
		else:
			self.next_turn()


	def get_clue(self):
		clue = input('Enter clue:\n')
		number = input('Enter number:\n')
		if number in list('123456789'):
			return clue, int(number)
		else:
			print('Invalid number')
			return self.get_clue()

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
		print('Changing turn!\n')
		if self.current_turn == 'B':
			self.current_turn = 'R'
		else:
			self.current_turn = 'B'

	def start_prompt(self):
		print(self.board)
		input('Press to reveal colors to clue givers...\n')
		print('\n'*50)
		print(self.board.only_colors())
		input('Press enter to reveal board to clue givers...\n')
		print('\n'*50)
		

		print('BOARD:')
		print(self.board.full_display())
		print()
		input('Press enter when ready to begin...\n')
		print('\n'*50)

	def view_full_board(self):
		print(self.board.full_display())


	def make_random_board(self, num_rows, num_columns, num_reds, num_blues, word_list):

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

		for square in board.get_all_squares():
			square.word = wordgetter.__next__()

		return board

	def save_game_to_file(self):
		with open(self.savepath, 'w') as f:
			f.write(self.board.full_display())





