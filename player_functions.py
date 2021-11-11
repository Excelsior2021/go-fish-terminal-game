from card_functions import *
from deck_functions import *
from go_fish_functions import report_hands_pairs

def player_choose_card(player_hand):
    '''Player chooses a card from their hand with a value that they want to match in their opponent's hand.'''
    card = input(f"\nChoose a card from your hand: " + "\n")
    if card in player_hand:
        return card
    else:
        print("You don't have that card in your deck. Try again.")

def player_match(player_hand, comp_hand, player_pairs, comp_pairs, deck, comp_asked):
    if len(player_hand) > 0 and len(comp_hand) > 0:
        pick = player_choose_card(player_hand)
        while not pick:
            pick = player_choose_card(player_hand)
        for card in comp_hand:
            if get_value(card) == get_value(pick):
                player_pairs.append(pick)
                player_pairs.append(card)
                player_hand.remove(pick)
                comp_hand.remove(card)
                if len(player_hand) == 0:
                    pass
                else:
                    print("\nYou've matched! It's your turn again!")
                    report_hands_pairs(player_hand, comp_hand, player_pairs, comp_pairs)
                    pick = player_match(player_hand, comp_hand, player_pairs, comp_pairs, deck, comp_asked)
                    break
        if card not in player_pairs:
            player_deal_card(pick, player_hand, comp_hand, player_pairs, comp_pairs, deck, comp_asked)
        return pick
      
def player_deal_card(pick, player_hand, comp_hand, player_pairs, comp_pairs, deck, comp_asked):
    '''Deals top card from the deck and compares value with player ask or with another value in player hand. 
        If no matches, card added to player hand.'''
    comp_asked = comp_asked
    if len(deck) > 0:
        print("\nGo Fish! Deal a card from the deck.\n")
        card = deal_top_card(deck)
        value = get_value(card)
        print(f"Dealt card: {card}")
        if len(player_hand) > 0:
            if value == get_value(pick):
                player_pairs.append(card)
                player_pairs.append(pick)
                player_hand.remove(pick)
                print("The value you chose matches the card you dealt from the deck! Both cards will be added to your pairs. It's your turn again!")
                report_hands_pairs(player_hand, comp_hand, player_pairs, comp_pairs)  
                player_match(player_hand, comp_hand, player_pairs, comp_pairs, deck, comp_asked)
            elif value != get_value(pick):
                for card_1 in player_hand:
                    if value == get_value(card_1):
                        player_pairs.append(card)
                        player_pairs.append(card_1)
                        player_hand.remove(card_1)
                        print("The value you chose didn't match the dealt card but you had a match in your hand, the two cards will be added to your pairs. It's your opponent's turn.")
                        report_hands_pairs(player_hand, comp_hand, player_pairs, comp_pairs) 
                        break
                if card not in player_pairs:
                    player_hand.append(card)
                    comp_asked.clear()
                    print("No matches, the dealt card has been added to your hand. It's your opponent's turn.")
                    report_hands_pairs(player_hand, comp_hand, player_pairs, comp_pairs)
                    return comp_asked  