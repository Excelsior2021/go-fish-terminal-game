'''A simulation of an adaptation of the card game Go Fish.'''
from go_fish_functions import *
from player_functions import *
from computer_functions import *

#Deck is created and shuffled. Hands are dealt to players.
deck = create_deck()
shuffle_deck(deck)
player_hand = deal_hand(deck, 7)
comp_hand = deal_hand(deck, 7)

#Original cards dealt to players.
print(f'Player original hand: {player_hand}')

#Inital pairs before players start.
player_pairs = initial_pairs(player_hand)
comp_pairs = initial_pairs(comp_hand)

report_hands_pairs(player_hand, comp_hand, player_pairs, comp_pairs)

comp_asked = []
comp_hand_copy = comp_hand[:]

while len(deck) > 0 and len(player_hand) > 0 and len(comp_hand) > 0:
    #player turn
    player_pick = player_match(player_hand, comp_hand, player_pairs, comp_pairs, deck, comp_asked)

    #computer turn
    comp_pick = computer_match(player_hand, comp_hand, player_pairs, comp_pairs, deck, comp_asked)

"""End of Game"""
print("\n________________________________________________________________")
print("\nGAME OVER!")

#Outcome of the game.
if len(player_pairs) > len(comp_pairs):
    print(f'\nYou win!'.upper())
elif len(comp_pairs) > len(player_pairs):
    print(f'\nYour opponent wins!'.upper())
else:
    print(f"\nIt's a draw!".upper())

#Player cards at the end of the game.
print(f"\nPlayer pairs: {player_pairs}\n")
print(f"Computer pairs: {comp_pairs}\n")
print(f'\nPlayer1 cards left: {player_hand}\n')
print(f'Computer cards left: {comp_hand}\n')

#Cards remaining in deck.
print(f'Deck remaining: {len(deck)}\n')

# print(f'Total Card Count: {len(player_hand + comp_hand + player_pairs + comp_pairs + deck)}')