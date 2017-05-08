from ai import minimax
from board import Board, check_board

def main():
	board = Board(3)
	board.add_move('X', 0, 0)
	board.add_move('O', 1, 1)
	board.add_move('X', 1, 0)

	board.add_move('O', 2, 0)
	board.add_move('X', 0, 2)
	board.add_move('X', 1, 2)

	board.add_move('O', 0, 1)
	board.add_move('X', 2, 1)
	# board.add_move('O', 2, 2)
	board.draw()

	print(check_board(board))

if __name__ == "__main__":
	main()