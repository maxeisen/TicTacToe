def stateUpdate(gameState, turnTaker, posChoice):
	gameState[posChoice - 1] = turnTaker
	return(gameState)


def printBoard(gameState):
	for i in range(9):
		if str(gameState[i]) in "123456789":
			gameState[i] = " "
	gameBoard = "\n   |   |   \n " + str(gameState[0]) + " | " + str(gameState[1]) + " | " + str(gameState[2]) + " \n___|___|___\n   |   |   \n " + str(gameState[3]) + " | " + str(gameState[4]) + " | " + str(gameState[5]) + " \n___|___|___\n   |   |   \n " + str(gameState[6]) + " | " + str(gameState[7]) + " | " + str(gameState[8]) + " \n   |   |   "
	print(gameBoard)


def turn(gameState, turnNum, turnTaker):
	if (turnNum > 9):
		checkState(gameState, turnNum)
		return(endGame())
	initState = gameState
	invalidChoice = True
	try:
		while invalidChoice == True:
			posChoice = eval(input("\nPlayer " + turnTaker + " - Choose your position (1-9) or leave blank to view board map: "))
			if ((gameState[posChoice - 1] != " ") and (gameState[posChoice - 1] != posChoice)):
				print("\nPosition filled. Try again.")
			else:
				return(stateUpdate(gameState, turnTaker, posChoice))
	except:
		gameState = initState
		print("\nPlease take note of the board map\n\n   |   |   \n 1 | 2 | 3 \n___|___|___\n   |   |   \n 4 | 5 | 6 \n___|___|___\n   |   |   \n 7 | 8 | 9 \n   |   |   ")
		return(turn(initState, turnNum, turnTaker))


def checkState(gameState, turnNum):
	topRow = str(gameState[0]) + str(gameState[1]) + str(gameState[2])
	midRow = str(gameState[3]) + str(gameState[4]) + str(gameState[5])
	botRow = str(gameState[6]) + str(gameState[7]) + str(gameState[8])
	leftCol = str(gameState[0]) + str(gameState[3]) + str(gameState[6])
	midCol = str(gameState[1]) + str(gameState[4]) + str(gameState[7])
	rightCol = str(gameState[2]) + str(gameState[5]) + str(gameState[8])
	diag1 = str(gameState[0]) + str(gameState[4]) + str(gameState[8])
	diag2 = str(gameState[2]) + str(gameState[4]) + str(gameState[6])
	lines = [topRow, midRow, botRow, leftCol, midCol, rightCol, diag1, diag2]
	if turnNum > 9:
		print("\nCat's game - Thanks for playing!")
		return(False)
	elif ("XXX" in lines):
		print("\nPlayer X wins! Thanks for playing!")
		return(endGame())
	elif ("OOO" in lines):
		print("\nPlayer O wins! Thanks for playing!")
		return(endGame())
	else:
		return(True)


def gameDriver():
	gameState = [1,2,3,4,5,6,7,8,9]
	turnNum = 1
	players = ["X", "O"]
	X = "X"
	O = "O"
	x = "X"
	o = "O"
	try:
		starter = None
		starterChoice = eval(input("\nWho's starting? (X or O): "))
	except:
		starterChoice = None
	if starterChoice == "X":
		starter = True
	elif starterChoice == "O":
		starter = False
	else:
		print("\nInvalid entry. Try again.")
		gameDriver()
	if starter:
		turnTaker = "X"
	else:
		turnTaker = "O"
	gameState = turn(gameState, turnNum, turnTaker)
	print("\nTurn #1")
	printBoard(gameState)
	gameOn = True
	while gameOn == True:
		starter = not starter
		if starter:
			turnTaker = "X"
		else:
			turnTaker = "O"
		turnNum += 1
		gameState = turn(gameState, turnNum, turnTaker)
		print(("\nTurn #" + str(turnNum)))
		printBoard(gameState)
		gameOn = checkState(gameState, turnNum)


def endGame():
	playAgain = False
	y = True
	Y = True
	try:
		playAgain = False
		playAgain = (eval(input("\nPlay again? (Y/N): ")))
	except:
		quit()
	if playAgain:
		gameDriver()
	else:
		quit()
		

def main():
	print("\nWelcome to TicTacToe Basic by Max Eisen\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\nPlease take note of the board map")
	print("\n   |   |   \n 1 | 2 | 3 \n___|___|___\n   |   |   \n 4 | 5 | 6 \n___|___|___\n   |   |   \n 7 | 8 | 9 \n   |   |   ")
	gameDriver()


if __name__ == '__main__':
    main()
