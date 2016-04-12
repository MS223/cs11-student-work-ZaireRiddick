raw_input ("Today you'll be playing a card game called War")
player1 = raw_input("Player 1, Type Your Name")
player2 = raw_input("Player 2, Type Your Name")
import random

def shuffled_deck():
    basic_deck = range (2, 15) * 4
    random.shuffle(basic_deck)
    return basic_deck

def player_turn(player_name):
    card = deck.pop()
    print player_name, 'drew card', card
    return str(card)

#def basic_deck():

#player_turn(player1,  ):
#print player1 drew  card x

#def compare_scores('compare player1 to player2')
