'''An adaptation of the card game Go Fish.'''

from card_functions import *
from deck_functions import *
from go_fish_functions import *

player_pairs = []
comp_pairs = []

#Deck is created and shuffled. Hands are dealt to players.
deck = create_deck()
shuffled = shuffle_deck(deck)
player_cards = deal_hand(shuffled, 7)
comp_cards = deal_hand(shuffled, 7)

#Original cards dealt to players.
print(f'Player original hand: {player_cards}')
print(f'Comp original hand: {comp_cards}')

#Inital pairs before players start.
player_pairs = pairs(player_cards)
comp_pairs = pairs(comp_cards)

player_ask = ask_value(player_cards, comp_cards, player_pairs)
print(player_ask)
deal_card(player_cards, comp_cards, player_pairs, deck, player_ask)
comp_ask = ask_value(comp_cards, player_cards, comp_pairs)
deal_card(comp_cards, player_cards, comp_pairs, deck, player_ask)

print(f'Player cards: {player_cards}')
print(f'Comp cards: {comp_cards}')

print(f'Player pairs: {player_pairs}')
print(f'Comp pairs: {comp_pairs}')

print(len(deck))