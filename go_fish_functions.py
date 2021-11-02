from card_functions import *
from deck_functions import *

from random import choice

# deck = ['Queen of Hearts', 'Jack of Spades', '2 of Clubs', '2 of Hearts', 'Queen of Diamonds', '5 of Hearts', '2 of Diamonds']

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
    card = choice(asker_cards)
    value = get_value(card)
    for card_1 in askee_cards:
        if value == get_value(card_1):
            pairs.append(card)
            pairs.append(card_1)
            asker_cards.remove(card)
            askee_cards.remove(card_1)
            ask_value(asker_cards, askee_cards, pairs)
        continue
        

def deal_card(asker_cards, askee_cards, pairs, deck):
    '''deals top card from the deck.'''
    card = deal_top_card(deck)
    value = get_value(card)
    for card_1 in asker_cards:
        if value == get_value(card_1):
            pairs.append(card)
            pairs.append(card_1)
            asker_cards.remove(card)
            askee_cards.remove(card_1)
            break
        else:
            asker_cards.append(card)
            break

# print(pairs(deck))
# print(deck)