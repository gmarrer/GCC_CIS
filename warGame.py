#warGame.py
#look at the following non-OOP solution and provide comments to ALL lines of 
#code and all modules(functions).

import random

 
player1win = 0
player2win = 0 
ties = 0
 
def faceCardConvert(inCard):
	if inCard[1] == "j":
		return  11
	elif inCard[1] == "q":
		return 12
        elif inCard[1] == "k":
        	return 13
        elif inCard[1] == "a":
        	return 14
        else:
        	if len(inCard) == 3:
        		return inCard[1:3]
        	else: 
        		return inCard[1]
        
               
 
cards=[ "h2", "h3", "h4", "h5", "h6", "h7", "h8", "h9", "h10", "hj", "hq", "hk", "ha", "s2", "s3", "s4", "s5", "s6", "s7", "s8", "s9", "s10", "sj", "sq", "sk", "sa", "d2", "d3", "d4", "d5", "d6", "d7", "d8", "d9", "d10", "dj", "dq", "dk", "da", "c2", "c3", "c4", "c5", "c6", "c7", "c8", "c9", "c10", "cj", "cq", "ck", "ca"]
cnt  = 0              

#start of program

print " War Games"
print ""
print "The games assumes only two players and that ace is high"
print "ties.... No one wins"
print "=========================================================="

print "Dealing Cards"
random.shuffle(cards)

#hand1
print "Hand 1"
cnt = 0
hand1= []
while cnt < 26:
	hand1.append(cards[cnt])
	cnt = cnt + 1 

#hand2   
print "Hand 2"
cnt = 26
hand2= []
while cnt < 52:
	hand2.append(cards[cnt])
	cnt = cnt + 1 
	
cnt = 0   	
while cnt < 26:
	print "Hand ", cnt + 1
	player1card = hand1[cnt]
	player2card = hand2[cnt]
	print "Player 1 Card",  player1card.upper(), "  "  "Player 2 Card ",  player2card.upper()
	player1Val = faceCardConvert(player1card)
	player2Val = faceCardConvert(player2card)

	if  int(player1Val) != int(player2Val):

		if int(player1Val) > int(player2Val):

			print "Player One ", player1Val, "  Player Two", player2Val
			print "Player 1 Wins "
			player1win = player1win + 1 
		else:
			print "Player One ", player1Val, "  Player Two", player2Val
			print "Player 2 Wins "
			player2win = player2win + 1 
	else:
		ties = ties + 1 
	cnt = cnt + 1 
	#stp = raw_input("hit any key to continue")  #uncomment to look at each hand one at a time.
	
print "Player One has ", player1win, " points"
print "Player Two has ", player2win, " points"
print "Ties = ", ties,  