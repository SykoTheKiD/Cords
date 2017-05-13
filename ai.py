# !/usr/local/bin/python3

import sys
import cnsts

from board import check_board

def minimax(board, player):
	""" Uses the minimax algorithm to get the next best move
        Args:
            param1 (Board): the board in play
            param2 (player): the player a move must be generated for
			
		Returns:
			Returns a tuple of the form (best move, best score)
			If best move is -1 then the board is complete and no move is possible
	"""
	player1, player2 = board.pieces
	points = {player1: 10, player2: -10, cnsts.DRAW: 0}
	best_move = -1
	best_score = -sys.maxsize if (player == player1) else sys.maxsize
	winner = check_board(board)
	if(winner == player1):
		return (best_move, points[player1])
	elif(winner == player2):
		return (best_move, points[player2]) 
	elif(winner == cnsts.DRAW):
		return (best_move, points[cnsts.DRAW])
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

def alphabeta(board, player, alpha, beta):
	""" Uses alpha beta pruning algorithm to get the next best move
        Args:
            param1 (Board): the board in play
            param2 (player): the player a move must be generated for
			
		Returns:
			Returns a tuple of the form (best move, best score)
			If best move is -1 then the board is complete and no move is possible
	"""
	player1, player2 = board.pieces
	points = {player1: 10, player2: -10, cnsts.DRAW: 0}
	best_move = -1
	best_score = -sys.maxsize if (player == player1) else sys.maxsize
	winner = check_board(board)
	if(winner == player1):
		return (best_move, points[player1])
	elif(winner == player2):
		return (best_move, points[player2]) 
	elif(winner == cnsts.DRAW):
		return (best_move, points[cnsts.DRAW])
	else:
		empty_positions = board.empty_spots()
		number_empty = len(empty_positions)
		if(player == player1):
			for i in range(0, number_empty):
				current = empty_positions[i]
				x_coord, y_coord = current
				board.add_move(player, x_coord, y_coord)
				new_move, new_score = alphabeta(board, player2, alpha, beta)
				if(new_score > alpha):
					alpha = new_score
				if(alpha >= beta):
					break
			return alpha
				board.reset_position(x_coord, y_coord)