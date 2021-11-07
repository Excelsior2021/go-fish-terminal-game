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
# print(f'Player original hand: {player_hand}\n')
# print(f'Computer original hand: {comp_hand}\n')

#Inital pairs before players start.
player_pairs = initial_pairs(player_hand)
comp_pairs = initial_pairs(comp_hand)

report_hands_pairs(player_hand, comp_hand, player_pairs, comp_pairs)

while len(deck) > 0:
    #player turn
    player_pick = player_match(player_hand, comp_hand, player_pairs, comp_pairs)
    player_deal_card(player_pick, player_hand, comp_hand, player_pairs, comp_pairs, deck)

    #computer turn
    comp_pick = computer_match(player_hand, comp_hand, player_pairs, comp_pairs, deck)
    computer_deal_card(comp_pick, player_hand, comp_hand, player_pairs, comp_pairs, deck)



# #Player cards at the end of the game.
# print(f'Player1 cards left: {player1_hand}\n')
# print(f'Computer cards left: {comp_hand}\n')

# #Cards remaining in deck.
# print(f'Deck remaining: {len(deck)}\n')

# #Outcome of the game.
# if len(player1_pairs) > len(comp_pairs):
#     print(f'Player1 wins!')
# elif len(comp_pairs) > len(player1_pairs):
#     print(f'Computer wins!')
# else:
#     print(f"It's a draw!")

# print(f'Total Card Count: {len(player1_hand + comp_hand + player1_pairs + comp_pairs + deck)}')