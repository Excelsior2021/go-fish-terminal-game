'''Deck Functions for Deck of Cards'''
from random import shuffle, choice

def shuffle_deck(deck):
    '''Shuffles a deck of cards.'''
    shuffle(deck)
    return deck

def deal_top_card(deck):
    '''Deals the top card of a deck.'''
    card = deck[0]
    deck.remove(card)
    return card

def get_random_card(deck):
    '''Chooses a random card from the deck.'''
    card = choice(deck)
    deck.remove(card)
    return card

def deal_hand(deck, hand_size):
    '''Returns a set of cards from a deck. Amount based on hand size.'''
    hand = []
    while len(hand) < int(hand_size):
        pick = choice(shuffle_deck(deck))
        hand.append(pick)
        deck.remove(pick)
    return hand

def deal_hands(deck, hand_size, num_hands=1):
    '''Returns sets of cards from a deck based on hand size.'''
    hands = []
    i = 0
    while i < num_hands:
        hands.append(deal_hand(deck, hand_size))
        i += 1
    return hands