import unittest
from computer_functions import computer_match
from go_fish_functions import *
from player_functions import *

class GoFishFunctionsTest(unittest.TestCase):
    """Tests for Go Fish."""

    def test_guess_in_deck(self):
        """Test if player/computer guesses are processed correctly"""
        deck = create_deck()

        #Players hands
        player_hand = deal_hand(deck, 7)
        computer_hand = deal_hand(deck, 7)
        player_pairs = []
        computer_pairs = []
        comp_asked = []

        print(f"Player hand: {player_hand}")
        print(f"Computer hand: {computer_hand}")

        #Player Guess
        player_match(player_hand, computer_hand, player_pairs, computer_pairs, deck, comp_asked)

        #Computer Guess
        computer_match(player_hand, computer_hand, player_pairs, computer_pairs, deck, comp_asked)

if __name__== '__main__':
    unittest.main()