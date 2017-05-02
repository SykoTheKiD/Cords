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

# grid[0][i] top col
# grid[i][0] left col
# grid[i][board_size - 1] right col
# grid[i][i] left diag
# grid[i][board_size - 1 - i] // right diag
# x x x
# x x x
# x x x
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
					break
			else:
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
					break
			else:
				break
		if(row):
			return row





def main():
	board = Board(3)
	board.add_move('O', 0, 0)
	board.add_move('O', 0, 1)
	board.add_move('O', 0, 2)
	board.print_board()

if __name__ == "__main__":
	main()



