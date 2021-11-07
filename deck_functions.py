'''Deck Functions for Deck of Cards'''
from random import shuffle, choice

non_num_cards = ['ace', 'jack', 'queen', 'king']
suits = ['clubs', 'diamonds', 'hearts', 'spades']

def create_deck():
    '''Creates a full deck of cards.'''
    deck = []
    i = 0
    for x in range(2, 11):
        for y in suits:
            deck.append(f'{x} of {y.title()}')
    for x in non_num_cards:
        if x != 'ace':
            for y in suits:
                deck.append(f'{x.title()} of {y.title()}')
    for x in suits:
        deck.insert(i, f'{non_num_cards[0].title()} of {x.title()}')
        i= i+1
    return deck

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
        card = deal_top_card(deck)
        hand.append(card)
    return hand

def deal_hands(deck, hand_size, num_hands=1):
    '''Returns sets of cards from a deck based on hand size.'''
    hands = []
    i = 0
    while i < num_hands:
        hands.append(deal_hand(deck, hand_size))
        i += 1
    return hands