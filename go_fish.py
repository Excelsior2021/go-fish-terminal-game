'''A simulation of an adaptation of the card game Go Fish.'''

from card_functions import *
from deck_functions import *
from go_fish_functions import *

comp1_pairs = []
comp_pairs = []

#Deck is created and shuffled. Hands are dealt to players.
deck = create_deck()
shuffled = shuffle_deck(deck)
comp1_cards = deal_hand(shuffled, 7)
comp2_cards = deal_hand(shuffled, 7)

#Original cards dealt to players.
print(f'Comp1 original hand: {comp1_cards}\n')
print(f'Comp2 original hand: {comp2_cards}\n')

#Inital pairs before players start.
comp1_pairs = pairs(comp1_cards)
comp2_pairs = pairs(comp2_cards)

#Loop of game. Players taking turns based on rules.
while len(deck) > 0:
    comp1_ask = ask_value(comp1_cards, comp2_cards, comp1_pairs)
    comp1_dealed = deal_card(comp1_cards, comp2_cards, comp1_pairs, deck)
    comp2_ask = ask_value(comp2_cards, comp1_cards, comp2_pairs)
    comp2_dealed = deal_card(comp2_cards, comp1_cards, comp2_pairs, deck)

print(f'Comp1 pairs: {comp1_pairs}\n')
print(f'Comp2 pairs: {comp2_pairs}\n')

print(f'Comp1 cards left: {comp1_cards}\n')
print(f'Comp2 cards left: {comp2_cards}\n')

print(f'Deck remaining: {len(deck)}\n')

# if len(comp1_pairs) > len(comp2_pairs):
#     print(f'{player_name} you win! Well done!')
# else:
#     print(f'The computer wins! Better luck next time!')