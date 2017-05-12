# !/usr/local/bin/python3

import sys
from board import check_board

DRAW = 'DRAW'
# move, score
def minimax(board, player):
	player1, player2 = board.pieces
	points = {
		player1: 10,
		player2: -10,
		DRAW: 0
	}
	best_move = -1
	best_score = -sys.maxsize if (player == player1) else sys.maxsize
	winner = check_board(board)
	if(winner == player1):
		return (best_move, points[player1])
	elif(winner == player2):
		return (best_move, points[player2]) 
	elif(winner == DRAW):
		return (best_move, points[DRAW])
	else:
		empty_positions = board.empty_spots()
		number_empty = len(empty_positions)
		for i in range(0, number_empty):
			current = empty_positions[i]
			x_coord, y_coord = current
			board.add_move(player, x_coord, y_coord)
			if(player == player1):
				new_move, new_score = minimax(board, player2)
				if(new_score > best_score):
					best_score = new_score
					best_move = current
			else:
				new_move, new_score = minimax(board, player1)
				if(new_score < best_score):
					best_score = new_score
					best_move = current

			board.reset_position(x_coord, y_coord)

		return best_move, best_score