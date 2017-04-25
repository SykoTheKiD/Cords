# !/usr/python3



class Board:

	def __init__(self, size):
		self.terminal = '$'
		self.size = size
		self.board = []

		for i in range(size):
			tmp = ['$' for j in range(0, size)]
			self.board.append(tmp)

	def add_move(self, piece, x, y):
		x -=1
		y -=1
		if(x < self.size and y < self.size):
			pos = self.board[x][y]
			if(pos == self.terminal):
				self.board[x][y] = piece

	def print_board(self):
		print(self.board)
		for i in range (0, self.size):
			for j in range (0, self.size):
				print(self.board[i][j])

# bruh
def check_board(board):
	board_size = board.size
	current_character = None

	for i in range(0, board_size):
		char = board[0][i]
		if(not current_character):
			current_character = char

		if(current_character != char):
			break

		return current_character

	for i in range(0, board_size):
		board[board_size][i]

		if(not current_character):
			current_character = char

		if(current_character != char):
			break

		return current_character

	for i in range(0, board_size):
		board[i][0]

		if(not current_character):
			current_character = char

		if(current_character != char):
			break

		return current_character

	for i in range(0, board_size):
		board[i][board_size]

		if(not current_character):
			current_character = char

		if(current_character != char):
			break

		return current_character


def main():
	board = Board(3)
	board.print_board()


if __name__ == "__main__":
	main()



