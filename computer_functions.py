from card_functions import *
from deck_functions import *
from go_fish_functions import report_hands_pairs

def computer_choose_card(comp_hand):
    card = choice(comp_hand)
    return card

def computer_request(pick, value, deck, player_hand, comp_hand, player_pairs, comp_pairs):
    check = False
    player_response = input(f"\nDo you have a {value}?(y/n): ")
    if player_response == 'y':
        for card in player_hand:
            if get_value(card) == value:
                comp_pairs.append(pick)
                comp_pairs.append(card)
                comp_hand.remove(pick)
                player_hand.remove(card)
                print(f"\nYour opponent has taken your {card}. It's their turn again.")
                report_hands_pairs(player_hand, comp_hand, player_pairs, comp_pairs)
                computer_match(player_hand, comp_hand, player_pairs, comp_pairs, deck)
                check = True
                break
        if check == False:
            print("\nAre you sure?")
            computer_request(pick, value, deck, player_hand, comp_hand, player_pairs, comp_pairs)
    elif player_response == 'n':
        for card in player_hand:
            if get_value(card) == value:
                print("Are you sure?")
                computer_request(pick, value, deck, player_hand, comp_hand, player_pairs, comp_pairs)
                check == True
                break
        if pick not in comp_pairs:
            print("\nYour opponent has to deal a card from the deck.")
            computer_deal_card(pick, player_hand, comp_hand, player_pairs, comp_pairs, deck)
    else:
        print("That is not a valid response, please enter y/n.")
        computer_request(pick, value, deck, player_hand, comp_hand, player_pairs, comp_pairs)

def computer_match(player_hand, comp_hand, player_pairs, comp_pairs, deck):
    if len(comp_hand) > 0 and len(player_hand) > 0:
        pick = computer_choose_card(comp_hand)
        value = get_value(pick)
        computer_request(pick, value, deck, player_hand, comp_hand, player_pairs, comp_pairs)

def computer_deal_card(pick, player_hand, comp_hand, player_pairs, comp_pairs, deck):
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
                computer_match(player_hand, comp_hand, player_pairs, comp_pairs, deck)
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