from card_functions import *
from deck_functions import *

from random import choice

def initial_pairs(hand):
    '''Returns a list of pairs of values.'''
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

def ask_value(asker_hand, askee_hand, asker_pairs):
    '''Player asks for a value of a card they have in their hand.'''
    if len(asker_hand) > 0 and len(askee_hand) > 0:
        card = choice(asker_hand)
        value = get_value(card)
        for card_1 in askee_hand:
            if value == get_value(card_1):
                asker_pairs.append(card)
                asker_pairs.append(card_1)
                asker_hand.remove(card)
                askee_hand.remove(card_1)
                return True

def deal_card(asker_hand, askee_hand, asker_pairs, deck):
    '''Deals top card from the deck and compares value with player ask or with another value in player hand. 
        If no matches, card added to player hand.'''
    if len(deck) > 0:
        card = deal_top_card(deck)
        value = get_value(card)
        if len(asker_hand) > 0:
            player_ask = choice(asker_hand)
            if value == get_value(player_ask):
                asker_pairs.append(card)
                asker_pairs.append(player_ask)
                asker_hand.remove(player_ask)
                return True
            elif value != get_value(player_ask):
                for card_1 in asker_hand:
                    if value == get_value(card_1):
                        asker_pairs.append(card)
                        asker_pairs.append(card_1)
                        asker_hand.remove(card_1)
                        break
                    else:
                        asker_hand.append(card)
                        break
        else:
            asker_hand.append(card)

def again(asker_hand, askee_hand, asker_pairs):
    '''Calls ask_value if player is to play again.'''
    if ask_value or deal_card:
        ask_value(asker_hand, askee_hand, asker_pairs)