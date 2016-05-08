#class cardGame
#main()
#// Declarations
import random
x = 0
y = 0
limit = 0
index = 0
playerCard = 0
playerCardNum = 0
computerCard = 0
computerCardNum = 0
playerWin = 0
computerWin = 0
tie = 0
playerCardSuit = ""
computerCardSuit = ""
LENGTH = 52
GROUPS = 4
ROUNDS = 26
cardBounds  =  [0, 13, 26, 39]
cards  =  [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52]

SUITS  =  ["Clubs","Diamonds","Hearts","Spades"]
limit = LENGTH
y = 0

while (y < ROUNDS):		
	#// input the player’s card
	print "loop ",y
	index = random.randint(0,51)
	playerCard = cards[index]
	x = GROUPS - 1
	
	while (playerCard < cardBounds[x]) :
		x -= 1
	 
	playerCardNum = playerCard - cardBounds[x]
	
	playerCardSuit = SUITS[x]

	#move the cards up (take out player card)
	x = index
	while (x < (limit - 1)) :
		 
		
		cards[x] = cards[x + 1]
		x = x + 1
	 	limit = limit - 1

	#// input the computer’s card
	index = random.randint(0,51)
	computerCard = cards[index]
	x = GROUPS-1
	
	while (computerCard < cardBounds[x]):
		x -= 1
	 
	computerCardNum = computerCard - cardBounds[x]
	computerCardSuit = SUITS[x]

	#// move the cards up (take out computer’s card)
	x = index
	while (x < (limit - 1)):
		cards[x]= cards[x + 1]
		x = x + 1
		limit = limit - 1

	print "Player's card: ", playerCardNum, " of ", playerCardSuit
	
	print "Computer's card: ", computerCardNum, " of ", computerCardSuit
	
	if playerCardNum > computerCardNum :
		print "Player wins hand!"
		playerWin = playerWin + 1
	else :
		if computerCardNum > playerCardNum :
			print "Computer wins hand!"
			computerWin = computerWin + 1
		else :
			print "Tie!"
			tie = tie + 1
 
	y = y + 1
print "the end"
#endClass			

