'''A simulation of an adaptation of the card game Go Fish.'''
from go_fish_functions import *
from player_functions import *
from computer_functions import *
from stats import record
import json

#Initialise record file. To be used if no record file exists already. I will be updated after game is played.
first_record = {"Wins": 0, "Loses": 0, "Draws": 0}

#Print current stats
try:
    filename = 'record.json'
    with open(filename) as f:
        current_record = json.load(f)
except FileNotFoundError:
    pass
else:
    print(f"Current Record: {current_record}\n")

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
    first_record["Wins"] = 1
elif len(comp_pairs) > len(player_pairs):
    print(f'\nYour opponent wins!'.upper())
    first_record["Loses"] = 1
else:
    print(f"\nIt's a draw!".upper())
    first_record["Draws"] = 1

#Player cards at the end of the game.
print(f"\nPlayer pairs: {player_pairs}\n")
print(f"Computer pairs: {comp_pairs}\n")
print(f'\nPlayer1 cards left: {player_hand}\n')
print(f'Computer cards left: {comp_hand}\n')

#Cards remaining in deck.
print(f'Deck remaining: {len(deck)}\n')

# print(f'Total Card Count: {len(player_hand + comp_hand + player_pairs + comp_pairs + deck)}')

#Stats function
record(player_pairs, comp_pairs, first_record)

#New Stats
filename = 'record.json'
with open(filename) as f:
    new_record = json.load(f)

print(f"New Record: {new_record}")