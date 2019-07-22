from model.square import Square


class Board(object):

	def __init__(self, num_rows, num_columns):

		self.rows = [
					[Square() for r in range(num_rows)]
						for c in range(num_columns)]

		self.col_width = 25

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
		to_return = ''
		for row in self.rows:
			row_string = ''
			for i, square in enumerate(row):
				row_string += square.appearance()
				dist_to_next_col = (self.col_width * (i+1)) - len(row_string)
				if dist_to_next_col > 0:
					row_string += dist_to_next_col * ' '
			to_return += row_string + '\n'
		return to_return


	def full_display(self):
		col_width = 25
		to_return = ''
		for row in self.rows:
			row_string = ''
			for i, square in enumerate(row):
				row_string += square.full_string()
				dist_to_next_col = (self.col_width * (i+1)) - len(row_string)
				if dist_to_next_col > 0:
					row_string += dist_to_next_col * ' '
			to_return += row_string + '\n'
		return to_return

	def only_colors(self):
		col_width = 25
		to_return = ''
		for row in self.rows:
			row_string = ''
			for i, square in enumerate(row):
				row_string += square.color
				dist_to_next_col = (self.col_width * (i+1)) - len(row_string)
				if dist_to_next_col > 0:
					row_string += dist_to_next_col * ' '
			to_return += row_string + '\n'
		return to_return

	def list_view(self):

		reds = 	[square.full_string for square in self.get_all_squares() if square.color == 'R']
		blues = [square.full_string for square in self.get_all_squares() if square.color == 'B']
		kills = [square.full_string for square in self.get_all_squares() if square.color == 'X']
		others = [square.full_string for square in self.get_all_squares() if square.color == 'O']

		print('\033[94m' + '\n'.join(blues) 
					+ '\033[0m\n\n\033[91m'
					+ '\n'.join(reds)
					+ '\033[0m\n\n\033[95m'
					+ '\n'.join(kills)
					+ '\n\n'
					+ '\n'.join(others))


