'''A simulation of an adaptation of the card game Go Fish.'''
from go_fish_functions import *

#Deck is created and shuffled. Hands are dealt to players.
deck = create_deck()
shuffle_deck(deck)
player1_hand = deal_hand(deck, 7)
comp_hand = deal_hand(deck, 7)

#Original cards dealt to players.
print(f'Player1 original hand: {player1_hand}\n')
print(f'Computer original hand: {comp_hand}\n')

#Inital pairs before players start.
player1_pairs = initial_pairs(player1_hand)
comp_pairs = initial_pairs(comp_hand)

#Loop of game. Players taking turns based on rules.
while len(deck) > 0 and len(player1_hand) > 0 or len(comp_hand) > 0:
    #player1 turn.
    player1_turn = turn(player1_hand, comp_hand, player1_pairs, deck)

    #comp turn.
    comp_turn = turn(comp_hand, player1_hand, comp_pairs, deck)

#Players pairs.
print(f'Player1 pairs: {player1_pairs}\n')
print(f'Computer pairs: {comp_pairs}\n')

#Player cards at the end of the game.
print(f'Player1 cards left: {player1_hand}\n')
print(f'Computer cards left: {comp_hand}\n')

#Cards remaining in deck.
print(f'Deck remaining: {len(deck)}\n')

#Outcome of the game.
if len(player1_pairs) > len(comp_pairs):
    print(f'Player1 wins!')
elif len(comp_pairs) > len(player1_pairs):
    print(f'Computer wins!')
else:
    print(f"It's a draw!")

print(f'Total Card Count: {len(player1_hand + comp_hand + player1_pairs + comp_pairs + deck)}')