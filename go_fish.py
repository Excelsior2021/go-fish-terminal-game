from card_functions import *
from deck_functions import *
from go_fish_functions import *

player_pairs = []
comp_pairs = []

deck = create_deck()
shuffled = shuffle_deck(deck)
player_cards = deal_hand(shuffled, 7)
comp_cards = deal_hand(shuffled, 7)

print(f'Player cards: {player_cards}')
print(f'Comp cards: {comp_cards}')

player_pairs = pairs(player_cards)
comp_pairs = pairs(comp_cards)

player_ask = ask_value(player_cards, comp_cards, player_pairs)
deal_card(player_cards, comp_cards, player_pairs, deck)
comp_ask = ask_value(comp_cards, player_cards, comp_pairs)
deal_card(comp_cards, player_cards, comp_pairs, deck)

print(f'Player cards: {player_cards}')
print(f'Comp cards: {comp_cards}')

print(f'Player pairs: {player_pairs}')
print(f'Comp pairs: {comp_pairs}')

print(len(deck))