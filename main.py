# !/usr/local/bin/python3

PIECES = {'X' : 1, 'O': 2}

class Board:

	def __init__(self, size):
		self.terminal = '$'
		self.size = size
		self.grid = []
		PIECES[self.terminal] = -1
		for i in range(size):
			tmp = ['$' for j in range(0, size)]
			self.grid.append(tmp)

	def add_move(self, piece, x, y):
		x -=1
		y -=1
		if(x < self.size and y < self.size):
			pos = self.grid[x][y]
			if(pos == self.terminal):
				self.grid[x][y] = piece

	def print_board(self):
		for i in range(0, self.size):
			print('\n-----------')
			for j in range(0, self.size):
				print(self.grid[i][j] + ' |', end=" ")
		print('\n')

def check_board(board):
	grid = board.grid
	board_size = board.size

	left_diag = [grid[i][i] for i in range (0, board_size)]
	right_diag = [grid[i][board_size - 1 - i] for i in range (0, board_size)]

	# Check columns
	for i in range(0, board_size):
		column = None
		for j in range(0, board_size):
			current_character = grid[j][i]
			if(current_character != '$'):
				if(not column or current_character == column):
					column = current_character
				else:
					column = None
					break
			else:
				column = None
				break
		if(column):
			return column

	for i in range(0, board_size):
		row = None
		for j in range(0, board_size):
			current_character = grid[i][j]
			if(current_character != '$'):
				if(not row or current_character == row):
					row = current_character
				else:
					row = None
					break
			else:
				row = None
				break
		if(row):
			return row

	left_diag = list(set(left_diag))
	right_diag = list(set(right_diag))

	if(len(left_diag) == 1 and left_diag[0] != '$'):
		return left_diag[0]

	if(len(right_diag) == 1 and right_diag[0] != '$'):
		return right_diag[0]

def main():
	board = Board(3)
	board.add_move('O', 0, 2)
	board.add_move('O', 1, 1)
	board.add_move('O', 2, 0)
	board.print_board()

	print(check_board(board))

if __name__ == "__main__":
	main()



