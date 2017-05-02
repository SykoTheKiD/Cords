# !/usr/python3

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
		print(self.grid)
		for i in range (0, self.size):
			for j in range (0, self.size):
				print(self.grid[i][j])

def winning_piece(*lists):
	for each_list in lists:
		if(len(each_list) > 0):
			reduced = list(set(each_list))
			if(each_list[0] == '$' and len(reduced) != 1):
				break
			return reduced[0]

def check_board(board):
	grid = board.grid
	board_size = board.size
	top  = [grid[0][i] for i in range (0, board_size)]
	left = [grid[i][0] for i in range (0, board_size)]
	left_diagonal = [grid[i][i] for i in range (0, board_size)]
	right_diagonal = [grid[i][board_size -1 - i] for i in range (0, board_size)]
	return winning_piece(top, left, left_diagonal, right_diagonal)

def main():
	board = Board(3)
	check_board(board)


if __name__ == "__main__":
	main()



