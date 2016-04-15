deck = []
score1 = 0
score2 = 0
print 'Today you will be playing a card game called War.'
player1 = raw_input("Player 1, Type Your Name.")
player2 = raw_input("Player 2, Type Your Name.")
import random

def shuffled_deck():
    basic_deck = range (2, 15) * 4
    random.shuffle(basic_deck)
    return basic_deck

def player_turn(player_name):
    card = deck.pop()
    print player_name + " drew a " + str(card)
    return str(card)
def compare_scores (card1, card2):
    if card1  > card2: 
        print
deck = shuffled_deck()

while deck:
    if player_turn(player1) == player_turn(player2):
        print 'The game is a tie!'
    else:
        player_turn(player1) != player_turn(player2)
        print ''
#def basic_deck():

#player_turn(player1,  ):
#print player1 drew  card x

