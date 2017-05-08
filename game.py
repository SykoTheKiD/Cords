# !/usr/local/bin/python3

from board import Board, check_board
from ai import minimax

def main():
	board_size = 3
	board = Board(board_size)
	game_in_progress = True
	print("TIC TAC TOE\nP1 is 'X' \nP2 is 'O'")
	while(game_in_progress):
		board.draw()
		# Ask p1
		p1_move = input("Player 1 where do you want to place your X? i.e 2,3:\n")
		p1_move = list(map(int, p1_move.split()))
		board.add_move('X', p1_move[0], p1_move[1])
		board.draw()

		winner = check_board(board)
		if(winner):
			print(winner + " won!")
			break

		# Ask p2
		# p2_move = input("Player 2 where do you want to place your O? i.e 2,3:\n")
		print("P2 plays...\n")
		score_res = minimax(board, board.pieces[1])
		print(score_res)
		p2_move = score_res[0]
		board.add_move('O', p2_move[0], p2_move[1])
		# check board
		winner = check_board(board)
		if(winner):
			print(winner + " won!")
			break
		# end game or not
	board.draw()

if __name__ == "__main__":
	main()