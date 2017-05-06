# !/usr/local/bin/python3

import sys
from board import check_board

def minimax(board, player):
	player1 = board.pieces[0]
	player2 = board.pieces[1]
	best_move = -1
	best_score = sys.maxsize if (player == player1) else -sys.maxsize
	winner = check_board(board)
	if(winner):
		if(winner == player1):
			return (best_move, 10)
		elif(winner == player2):
			return (best_move, -10)
		elif(len(empty_positions) == 0):
			return (best_move, 0)
	else:
		empty_positions = board.empty_spots()
		number_empty = len(empty_positions)
		grid = board.grid
		for i in range(0, number_empty):
			current = empty_positions[i]
			x_coord = current[0]
			y_coord = current[1]
			grid[x_coord][y_coord] = player
			if(player == player1):
				score = minimax(board, player2)[1]
				if(best_score > score):
					best_score = score
					best_move = current
			else:
				score = minimax(board, player1)[1]
				if(best_score < score):
					best_score = score
					best_move = current

			grid[x_coord][y_coord] = board.terminal

		return (best_move, best_score)