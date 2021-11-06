'''A simulation of an adaptation of the card game Go Fish.'''
from go_fish_functions import *

#Deck is created and shuffled. Hands are dealt to players.
deck = create_deck()
shuffle_deck(deck)
player1_cards = deal_hand(deck, 7)
player2_cards = deal_hand(deck, 7)

#Original cards dealt to players.
print(f'Player1 original hand: {player1_cards}\n')
print(f'Player2 original hand: {player2_cards}\n')

#Inital pairs before players start.
player1_pairs = initial_pairs(player1_cards)
player2_pairs = initial_pairs(player2_cards)

#Loop of game. Players taking turns based on rules.
while len(deck) > 0 and len(player1_cards) > 0 or len(player2_cards) > 0:
    #player1 turn.
    player1_turn = turn(player1_cards, player2_cards, player1_pairs, deck)

    #player2 turn.
    player2_turn = turn(player2_cards, player1_cards, player2_pairs, deck)

#Players pairs.
print(f'Player1 pairs: {player1_pairs}\n')
print(f'Player2 pairs: {player2_pairs}\n')

#Player cards at the end of the game.
print(f'Player1 cards left: {player1_cards}\n')
print(f'Player2 cards left: {player2_cards}\n')

#Cards remaining in deck.
print(f'Deck remaining: {len(deck)}\n')

#Outcome of the game.
if len(player1_pairs) > len(player2_pairs):
    print(f'Player1 wins!')
elif len(player2_pairs) > len(player1_pairs):
    print(f'Player2 wins!')
else:
    print(f"It's a draw!")

print(f'Total Card Count: {len(player1_cards + player2_cards + player1_pairs + player2_pairs + deck)}')