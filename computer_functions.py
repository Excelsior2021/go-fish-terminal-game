from card_functions import *
from deck_functions import *
from go_fish_functions import report_hands_pairs

def computer_choose_card(comp_hand, comp_asked):
    '''Computer chooses card from hand.'''
    copy = computer_asked(comp_hand, comp_asked)
    card = choice(copy)
    return card

def computer_asked(comp_hand, comp_asked):
    '''Checks if computer has asked player for value already if player has not added card from deck.'''
    comp_hand_copy = comp_hand[:]
    if len(comp_hand) > 1:
        for card in comp_hand_copy:
            if card in comp_asked:
                comp_hand_copy.remove(card)
        return comp_hand_copy
    else:
        return comp_hand_copy

def computer_request(pick, value, deck, player_hand, comp_hand, player_pairs, comp_pairs, comp_asked):
    '''Computer asks if player has value. Function verifies players response. 
    If response if valid, if 'yes', computer matches with card from player hand. If 'no' computer deals from deck.'''
    check = False
    player_response = input(f"\nDo you have a {value}?(y/n): ")
    if player_response == 'y':
        for card in player_hand:
            if get_value(card) == value:
                comp_pairs.append(pick)
                comp_pairs.append(card)
                comp_hand.remove(pick)
                player_hand.remove(card)
                if len(comp_hand) == 0:
                    check = True
                    pass
                else:
                    print(f"\nYour opponent has taken your {card}. It's their turn again.")
                    report_hands_pairs(player_hand, comp_hand, player_pairs, comp_pairs)
                    computer_match(player_hand, comp_hand, player_pairs, comp_pairs, deck, comp_asked)
                    check = True
                    break
        if check == False:
            print("\nAre you sure?")
            computer_request(pick, value, deck, player_hand, comp_hand, player_pairs, comp_pairs, comp_asked)
    elif player_response == 'n':
        for card in player_hand:
            if get_value(card) == value:
                print("Are you sure?")
                computer_request(pick, value, deck, player_hand, comp_hand, player_pairs, comp_pairs, comp_asked)
                check == True
                break
        if pick not in comp_pairs:
            print("\nYour opponent has to deal a card from the deck.")
            comp_asked.append(pick)
            computer_deal_card(pick, player_hand, comp_hand, player_pairs, comp_pairs, deck, comp_asked)
            return comp_asked
    else:
        print("That is not a valid response, please enter y/n.")
        computer_request(pick, value, deck, player_hand, comp_hand, player_pairs, comp_pairs, comp_asked)

def computer_match(player_hand, comp_hand, player_pairs, comp_pairs, deck, comp_asked):
    '''Computer chooses card from hand and calls function to query player.'''
    if len(comp_hand) > 0 and len(player_hand) > 0:
        pick = computer_choose_card(comp_hand, comp_asked)
        value = get_value(pick)
        computer_request(pick, value, deck, player_hand, comp_hand, player_pairs, comp_pairs, comp_asked)

def computer_deal_card(pick, player_hand, comp_hand, player_pairs, comp_pairs, deck, comp_asked):
    '''Deals top card from the deck and compares value with value that computer chose initially or with another value in computer's hand. 
    If no matches, card added to computer's hand.'''
    if len(deck) > 0:
        card = deal_top_card(deck)
        value = get_value(card)
        if len(comp_hand) > 0:
            if value == get_value(pick):
                comp_pairs.append(card)
                comp_pairs.append(pick)
                comp_hand.remove(pick)
                print("Your opponent matched with the dealt card. Both cards have been added to their pairs. It's your opponent's turn again.")
                report_hands_pairs(player_hand, comp_hand, player_pairs, comp_pairs)
                computer_match(player_hand, comp_hand, player_pairs, comp_pairs, deck, comp_asked)
            elif value != get_value(pick):
                for card_1 in comp_hand:
                    if value == get_value(card_1):
                        comp_pairs.append(card)
                        comp_pairs.append(card_1)
                        comp_hand.remove(card_1)
                        print("Your opponent didn't match the orginal choice with the dealt card, but another card in their deck matched. Both cards will be added to their pairs. It's your turn.")
                        report_hands_pairs(player_hand, comp_hand, player_pairs, comp_pairs)
                        break
                if card not in comp_pairs:
                    comp_hand.append(card)
                    print("Your opponent didn't match. The dealt card has been added to their hand. It's your turn.")
                    report_hands_pairs(player_hand, comp_hand, player_pairs, comp_pairs)