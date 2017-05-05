# !/usr/local/bin/python3

import sys

def minimax(board, player):
	player1 = board.pieces[0]
	player2 = board.pieces[1]
	empty_positions = board.empty_spots()

	winner = board.check_board()

	if(winner == player1):
		return 10
	elif(winner == player2):
		return -10
	elif(len(empty_positions) == 0):
		return 0

	states = []
	for i in range(0, len(empty_positions)):
		current = empty_positions[i]
		x_coord = current[0]
		y_coord = current[1]
		board[x_coord][y_coord] = player
		state = {}
		if(player == player1):
			score = minimax(board, player2)
		else:
			score = minimax(board, player1)

		state[current] = score
		board[x_coord][y_coord] = board.terminal

		states.append(state)

	best_position = None
	if(player == player1):
		best_score = sys.maxsize
		for key in states:
			if(states[key] < best_score):
				best_position = key
	else:
		best_score = -sys.maxsize
		for key in states:
			if(states[key] >= best_score):
				best_position = key

	return best_position