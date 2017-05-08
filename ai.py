# !/usr/local/bin/python3

import sys
from board import check_board

def minimax(board, player):
	player1 = board.pieces[0]
	player2 = board.pieces[1]
	best_move = -1
	best_score = sys.maxsize if (player == player1) else -sys.maxsize
	winner = check_board(board)
	points = {
		player1: 10,
		player2: -10,
		'draw': 0
	}
	if(winner):
		if(winner == player1):
			return (best_move, points[player1])
		elif(winner == player2):
			return (best_move, points[player2])
		elif(len(empty_positions) == 0):
			return (best_move, points['draw'])
	else:
		empty_positions = board.empty_spots()
		number_empty = len(empty_positions)
		for i in range(0, number_empty):
			current = empty_positions[i]
			x_coord, y_coord = current[0], current[1]
			board.grid[x_coord][y_coord] = player

			board.grid[x_coord][y_coord] = board.terminal