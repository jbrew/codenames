
bluecode = '\033[94m'
redcode = '\033[91m'
endcode = '\033[0m'

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


	"""
	def full_string(self):
		if self.color.upper() == 'B':
			startcode = '\033[94m'
		elif self.color.upper() == 'R':
			startcode = '\033[91m'
		elif self.color.upper() == 'X':
			startcode = '\033[95m'
		else:
			startcode = ''
		
		endcode = '\033[0m'

		color = self.color.upper() if self.shown else self.color.lower()
		return '%s%s - %s%s' % (startcode, color.upper(), self.word, endcode)
	"""