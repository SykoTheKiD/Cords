from board import Board, check_board

def main():
	board = Board(3)
	game_in_progress = True
	print("TIC TAC TOE P1 is 'X' \nP2 is 'O'")
	while(game_in_progress):
		board.draw()
		# Ask p1
		p1_move = input("Where do you want to place your X? ")
		# Ask p2
		# check board
		# end game or not
		game_in_progress = False 
	board.add_move('X', 0, 0)
	board.add_move('X', 0, 1)
	board.add_move('X', 0, 2)
	board.draw()

	print(check_board(board))

if __name__ == "__main__":
	main()