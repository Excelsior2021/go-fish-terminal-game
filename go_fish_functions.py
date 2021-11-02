from card_functions import *
from deck_functions import *

from random import choice


def pairs(deck):
    '''Returns a list of pairs of values.'''
    pairs = []
    for cardx in deck:
        for cardy in deck:
            if get_value(cardx) == get_value(cardy) and get_suit(cardx) != get_suit(cardy) and cardx not in pairs and cardy not in pairs:
                pairs.append(cardx)
                pairs.append(cardy)
    for card in pairs:
        deck.remove(card)
    return pairs

def ask_value(asker_cards, askee_cards, pairs):
    '''Player asks for a value of a card they have in their hand.'''
    if len(asker_cards) > 0:
        card = choice(asker_cards)
        value = get_value(card)
        for card_1 in askee_cards:
            if value == get_value(card_1):
                pairs.append(card)
                pairs.append(card_1)
                asker_cards.remove(card)
                askee_cards.remove(card_1)
                if len(asker_cards) > 0:
                    ask_value(asker_cards, askee_cards, pairs)
            continue 

def deal_card(asker_cards, askee_cards, pairs, deck):
    '''Deals top card from the deck and compares value with player ask or with another value in player hand. 
        If no matches, card appended to player hand.'''
    if len(deck) > 0:
        card = deal_top_card(deck)
        value = get_value(card)
        if len(asker_cards) > 0:
            player_ask = choice(asker_cards)
            if value == get_value(player_ask):
                pairs.append(card)
                pairs.append(player_ask)
                asker_cards.remove(player_ask)
                ask_value(asker_cards, askee_cards, pairs)
            else:
                for card_1 in asker_cards:
                    if value == get_value(card_1):
                        pairs.append(card)
                        pairs.append(card_1)
                        asker_cards.remove(card_1)
                        break
                    else:
                        continue
                asker_cards.append(card)