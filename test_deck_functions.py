import unittest
import json
from deck_functions import *
from card_functions import *

class DeckFunctionsTest(unittest.TestCase):
    """Tests for deck functions."""

    def test_deck_is_52(self):
        '''Does the deck have 52 cards?'''
        deck = len(create_deck())
        self.assertEqual(deck, 52)

    def test_four_cards_for_each_value(self):
        '''Does each value in the deck have 4 cards?'''
        deck = create_deck()
        check = []
        for x in range(2,11):
            values = []
            for card in deck:
                if str(x) in card:
                    values.append(True)
            if len(values) == 4:
                check.append(True)
        for x in non_num_cards:
            values = []
            for card in deck:
                if x.title() in card:
                    values.append(True)
            if len(values) == 4:
                check.append(True)
        
        self.assertEqual(len(check), 13)

    def test_decks_are_equal(self):
        """Checks if two decks are equal."""
        filename = "deck.json"
        deck1 = create_deck()
        with open (filename, 'w') as f:
            json.dump(deck1, f)
        deck2 =create_deck()
        with open(filename) as f:
            deck1 = json.load(f)

        self.assertEqual(deck1, deck2)

    def deck_size(self):
        """Check the size of the deck when cards have been dealt."""

    def test_deck_functionality(self, deal_x=5):
        """Check if dealt cards have been dealt and remain number of cards in deck is correct."""
        deck = create_deck()
        dealt = []
        x = 0
        while x < deal_x:
            card = deal_top_card(deck)
            dealt.append(card)
            x+=1
        
        self.assertEqual(len(dealt), deal_x)
        self.assertEqual(len(deck), 52-deal_x)

if __name__== '__main__':
    unittest.main()