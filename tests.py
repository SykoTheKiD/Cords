from ai import minimax
from board import Board, check_board

def main():
	board = Board(3)
	board.add_move('X', 0, 0)
	board.add_move('O', 1, 1)
	board.add_move('X', 1, 0)
	board.draw()
	move, score = minimax(board, 'O')
	board.add_move('O', move[0], move[1])
	board.draw()
	board.add_move('X', 0, 1)

	move, score = minimax(board, 'O')
	board.add_move('O', move[0], move[1])

	board.draw()

if __name__ == "__main__":
	main()




















