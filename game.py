from classes.deck import Deck


"""
Group project!
Anthony
Andrew
Omar
Jessica
Zach
"""

deck = Deck()
house = Player("House", 1000000000)
player = Player("Player", 1000)

player_hand = []
dealer_hand = []
def add_cards_to_hand(arr):
    card_sum = 0
    for i in arr:
        card_sum += i.point_val
    return card_sum

# give player and dealer 2 cards to start
def play():
    player_hand = []
    dealer_hand = []
    player_hand.append(giveRandomCard())
    dealer_hand.append(giveRandomCard())
    player_hand.append(giveRandomCard())
    dealer_hand.append(giveRandomCard())
    player_sum = add_cards_to_hand(player_hand)
    dealer_sum = add_cards_to_hand(dealer_hand)
    print(f'Player is showing a {player_sum}')
    print(f'Dealer is showing a {dealer_sum}')
    if player_sum < 21 :
        choose_move = input('Hit or stay? h or s: ')
        if choose_move == 'h':
            while choose_move == 'h':
                print('player recieves another card')
                player_hand.append(giveRandomCard())
                new_total = add_cards_to_hand(player_hand)
                print(new_total)
                if new_total > 21:
                    print('you busted')
                    break
                else:
                    choose_move = input('Hit or stay? h or s: ')
        else:
            print('Player chooses to stay.')
    elif player_sum == 21:
        print('You`ve won!')
    else:
        print('You lose')
    # dealerAmount = add_cards_to_hand(dealer_hand)
    # while dealerAmount < 17:
    #     newCard = giveRandomCard()
    #     dealer_hand.append(newCard)
    #     dealerAmount = add_cards_to_hand(dealer_hand)
        
    #     print(f"Dealer has {dealerAmount}")

    # if dealerAmount >= player_sum:
    #     print("Dealer wins!")
    # else:
    #     print("Player wins!")



def reshuffle():
    deck = Deck()

def giveRandomCard():
    randomNumber = random.randint(0, len(deck.cards))
    print(f'the deck has: {len(deck.cards)}')
    newCard = deck.cards.pop(randomNumber)
    return newCard


# start game
# play game while both players have money
while player.balance > 10 and house.balance > 10:
    begin_game = input('Do you want to play? yes or no: ')
    if begin_game == 'yes' :
        reshuffle()
        play()
    else: 
        print('Keep walking through casino')
        break


    # print 1 card of house
    # print both cards of player

    # give choice to player to HIT or STAY
