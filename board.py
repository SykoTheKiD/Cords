# !/usr/local/bin/python3
import cnsts

class Board:

	def __init__(self, size, p1='X', p2='O'):
		self.terminal = '$'
		self.size = size
		self.grid = []
		self.pieces = (p1, p2)
		for i in range(size):
			tmp = [self.terminal for j in range(0, size)]
			self.grid.append(tmp)

	def add_move(self, piece, x, y):
		if(piece not in self.pieces):
			return
		if(x < self.size and y < self.size):
			pos = self.grid[x][y]
			if(pos == self.terminal):
				self.grid[x][y] = piece

	def draw(self):
		for i in range(0, self.size):
			print('\n' + "----" * self.size)
			for j in range(0, self.size):
				print(self.grid[i][j] + ' |', end=" ")
		print('\n'+ "----" * self.size + '\n')

	def empty_spots(self):
		ret = []
		for i in range(0, self.size):
			for j in range(0, self.size):
				if(self.grid[i][j] == self.terminal):
					ret.append((i,j))
		return ret

	def reset_position(self, x, y):
		self.grid[x][y] = self.terminal

def check_board(board):
	grid = board.grid
	board_size = board.size
	# Get diagonals
	left_diag = [grid[i][i] for i in range (0, board_size)]
	right_diag = [grid[i][board_size - 1 - i] for i in range (0, board_size)]

	# Check columns and rows
	for i in range(0, board_size):
		prev_character_col = grid[0][i]
		for j in range(0, board_size):
			current_character_col = grid[j][i]
			if(current_character_col == board.terminal or current_character_col != prev_character_col):
				prev_character_col = None
				break
		if(prev_character_col):
			return prev_character_col

	for i in range(0, board_size):
		prev_character_row = grid[i][0]
		for j in range(0, board_size):
			current_character_row = grid[i][j]
			if(current_character_row == board.terminal or current_character_row != prev_character_row):
				prev_character_row = None
				break
		if(prev_character_row):
			return prev_character_row

	# Check diagonals
	left_diag = list(set(left_diag))
	right_diag = list(set(right_diag))

	if(len(left_diag) == 1 and left_diag[0] != board.terminal):
		return left_diag[0]

	if(len(right_diag) == 1 and right_diag[0] != board.terminal):
		return right_diag[0]

	avail_positions = board.empty_spots()
	if(len(avail_positions) == 0):
		return cnsts.DRAW
	else:
		return cnsts.IN_PROGRESS