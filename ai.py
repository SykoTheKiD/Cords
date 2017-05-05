# !/usr/local/bin/python3

import sys

def score(board):
	if (board.winner == board.pieces[0]):
		return 10
	elif (board.winner == board.pieces[1]):
		return -10
	else:
		return 0

def minimax(board, depth, player):
	depth += 1
	empty_positions = board.empty_spots()

	winner = board.check_board()

	if(winner == board.pieces[0]):
		return 10
	elif(winner == board.pieces[1]):
		return -10
	elif(len(empty_positions) == 0):
		return 0

	states = []
	for i in range(0, len(empty_positions)):
		current = empty_positions[i]
		board[current[0]][current[1]] = player
		state = {}
		if(player == board.pieces[0]):
			score = minimax(board, depth, board.pieces[1])
		else:
			score = minimax(board, depth, board.pieces[0])

		state[current] = score
		board[current[0]][current[1]] = board.terminal

		states.append(state)

	best_position = None
	if(player == board.pieces[0]):
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