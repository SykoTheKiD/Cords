# !/usr/local/bin/python3

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
			print('\n-----------')
			for j in range(0, self.size):
				print(self.grid[i][j] + ' |', end=" ")
		print('\n-----------\n')

def check_board(board):
	grid = board.grid
	board_size = board.size

	# Get diagonals
	left_diag = [grid[i][i] for i in range (0, board_size)]
	right_diag = [grid[i][board_size - 1 - i] for i in range (0, board_size)]

	# Check columns and rows
	for i in range(0, board_size):
		column = None
		row = None
		for j in range(0, board_size):
			current_character_col = grid[j][i]
			current_character_row = grid[i][j]
			if(current_character_col != board.terminal and (not column or current_character_col == column)):
				column = current_character_col
			else:
				column = None
				break

			if(current_character_row != board.terminal and (not row or current_character_row == row)):
				row = current_character_row
			else:
				row = None
				break

		if(column):
			return column

		if(row):
			return row

	# Check diagonals
	left_diag = list(set(left_diag))
	right_diag = list(set(right_diag))

	if(len(left_diag) == 1 and left_diag[0] != board.terminal):
		return left_diag[0]

	if(len(right_diag) == 1 and right_diag[0] != board.terminal):
		return right_diag[0]

def main():
	board = Board(3)
	board.add_move('X', 0, 0)
	board.add_move('X', 0, 1)
	board.add_move('X', 0, 2)
	board.draw()

	print(check_board(board))

if __name__ == "__main__":
	main()



