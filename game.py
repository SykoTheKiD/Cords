# !/usr/local/bin/python3

import cnsts

from ai import minimax
from board import Board, check_board

def main():
	board_size = 3
	board = Board(board_size)
	player1, player2 = board.pieces
	print("TIC TAC TOE\nP1 is '" + player1 + "' \nP2 is '" + player2 + "'")
	while(True):
		board.draw()
		# Ask p1
		p1_move = input("Player 1 where do you want to place your "+ player1 +"? i.e 2,3:\n")
		p1_move = list(map(int, p1_move.split()))
		board.add_move(player1, p1_move[0], p1_move[1])
		board.draw()

		winner = check_board(board)
		if(winner == player1 or winner == player2):
			print(winner + " won!")
			break
		elif(winner == cnsts.DRAW):
			print('Draw!')
			break

		# Ask p2
		print("Player 2 plays...\n")
		score_res = minimax(board, board.pieces[1])
		p2_move = score_res[0]
		board.add_move(player2, p2_move[0], p2_move[1])
		# check board
		winner = check_board(board)
		if(winner == player1 or winner == player2):
			print(winner + " won!")
			break
		elif(winner == cnsts.DRAW):
			print('Draw!')
			break
		# end game or not
	board.draw()

if __name__ == "__main__":
	main()