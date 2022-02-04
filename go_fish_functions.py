from card_functions import *
from deck_functions import *

def initial_pairs(hand):
    '''Returns a list of initial pairs of values.'''
    pairs = []
    for cardx in hand:
        for cardy in hand:
            if get_value(cardx) == get_value(cardy) and get_suit(cardx) != get_suit(cardy) and cardx not in pairs and cardy not in pairs:
                pairs.append(cardx)
                pairs.append(cardy)
    for card in pairs:
        hand.remove(card)
    return pairs

def pairs(hand, pairs):
    '''Returns a list of pairs of values.'''
    for cardx in hand:
        for cardy in hand:
            if get_value(cardx) == get_value(cardy) and get_suit(cardx) != get_suit(cardy) and cardx not in pairs and cardy not in pairs:
                pairs.append(cardx)
                pairs.append(cardy)
    for card in pairs:
        if card in hand:
            hand.remove(card)

def report_hands_pairs(player_hand, comp_hand, player_pairs, comp_pairs):
    '''Prints out lists of players cards in their current status.'''
    print(f"\nPlayer pairs: {player_pairs}\n")
    print(f"Computer pairs: {comp_pairs}\n")
    print(f"Player hand: {player_hand}\n")
    # print(f"Computer hand: {comp_hand}")