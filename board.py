# !/usr/local/bin/python3
import cnsts

class Board:
	""" Default board object the game will be played on
		
		Attributes:
			terminal (str) : the symbol used to denote empty positions on the table
			size (int) : the dimension of the board
			pieces (str, str) : the pieces that will be used on the board, default : player 1 = X, player 2 = O
	"""
	def __init__(self, size, p1='X', p2='O'):
		""" Initialize board
        Args:
            param1 (str): Size of board
            param2 (:obj:`str`, optional): piece used by player 1
            param3 (:obj:`str`, optional): piece used by player 2

        """
		self.terminal = '$'
		self.size = size
		self.grid = []
		self.pieces = (p1, p2)
		for i in range(size):
			tmp = [self.terminal for j in range(0, size)]
			self.grid.append(tmp)

	def add_move(self, piece, x_coord, y_coord):
		""" Adds a piece to the board at the specified position
        Args:
            param1 (str): piece to be added
            param2 (:obj:`int`): x coordinate of the position
                lines are supported.
            param3 (:obj:`int`): y coordinate of the position
			
			Raises:
				Function errors (ValueError) if piece is invalid (un-registered with board)
        """
		if(piece not in self.pieces):
			raise ValueError
		if(x_coord < self.size and y_coord < self.size):
			pos = self.grid[x_coord][y_coord]
			if(pos == self.terminal):
				self.grid[x_coord][y_coord] = piece

	def draw(self):
		""" Draw out the board with styling """
		for i in range(0, self.size):
			print('\n' + "----" * self.size)
			for j in range(0, self.size):
				print(self.grid[i][j] + ' |', end=" ")
		print('\n'+ "----" * self.size + '\n')

	def empty_spots(self):
		""" Return all empty positions on the board

		Returns:
			Function returns a list of tuples denoting all empty positions on the board
		"""
		ret = []
		for i in range(0, self.size):
			for j in range(0, self.size):
				if(self.grid[i][j] == self.terminal):
					ret.append((i,j))
		return ret

	def reset_position(self, x, y):
		""" Resets a position on the board back to the terminal """
		self.grid[x][y] = self.terminal

def check_board(board):
	""" Checks if there is a winner on the board
        Args:
            param1 (Board): the board to be verified
			
		Returns:
			Returns player 1's piece or player 2's piece if they are winners
			Returns DRAW or IN PROGRESS if the game is tied or in progress
	"""
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