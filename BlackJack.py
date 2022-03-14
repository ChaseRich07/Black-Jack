import random

#TUPLE OF CARD SUITS
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
#TUPLE OF CARD RANKS
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
#DICTIONARY OF CARD VALUES
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':11}
playing = True
class Card:

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit


class Deck:

    def __init__(self):
        
        self.deck = []
        for suit in suits:
            for rank in ranks:
               self.deck.append(Card(suit,rank))

    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n'+ card.__str__()
        return "The deck has: "+deck_comp

    def shuffle(self):
        
        random.shuffle(self.deck)

    def deal_one(self):
        single_card = self.deck.pop()
        return single_card


class Hand:

    def __init__(self):

        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self,card):
        
        self.cards.append(card)
        self.value += values[card.rank]

    def adjust_for_ace(self):

        while self.value > 21 and self.aces:
            self.value -=10
            seld.aces -= 1
class Chips:

    def __init__(self):
        self.total = 100
        self.bet = 0

    def win_bet(self):
        self.total = self.total + self.bet



    def lose_bet(self):
        self.total = self.total - self.bet



def take_bet(chips):
    while True:
        try:
            chips.bet = int(input("Enter the amount of chips you would like to bet: "))
        except ValueError:
            print ("That is not an integer")
        else:
            if chips.bet > chips.total:
                 print(f"Insufficient chips for such a bet. you have",chips.total)
            else:
                break


#DEFINE WHICH DECK IS BEING DRAWN FROM AND WHICH PLAYER THE HIT IS BEING GIVEN TO
def hit(deck,hand):
        hand.add_card(deck.deal_one())
        hand.adjust_for_ace()
        

def hit_or_stand(deck,hand):
    global playing

    while True:
        x = input("""Would you like to hit or stand?
'h' for hit
's' for stand""")

        if x[0].lower() == 'h':
            hit(deck,hand)
        elif x[0].lower() == 's':
            print ("Player chooses to stand. Dealer is playing.")
            playing = False

        else:
            print("Sorry please try again.")
            continue
        break







    
def player_busts(player,dealer,chips):
        #END GAME HERE!!!
    print ("HUMAN SUCKS")
    chips.lose_bet()

def player_wins(player,dealer,chips):
        #END GAME HERE!!!
    print ("HUMAN WINS")
    chips.win_bet()

def dealer_busts(player,dealer,chips):
        #END GAME HERE!!!
    print ("DEALER SUCKS")
    chips.lose_bet()
    
    
def dealer_wins(player,dealer,chips):
        #END GAME HERE!!!
    print ("DEALER WINS")
    chips.win_bet()
    
def push(player,dealer):
    print ("TIE!!! IT IS A PUSH!")

def show_some(player,dealer):
    print ("--DEALER CARDS--")
    print ("<card hidden>")
    print (dealer.cards[0])
    print ("--PLAYER CARDS--")
    print (*player.cards, sep=
           '\n ')
    print("Player's Hand =",player.value)


def show_all(player,dealer):
    print ("--DEALER CARDS--")
    print (*dealer.cards, sep= '\n ')
    print("Dealer's Hand =",dealer.value)
    print ("--PLAYER CARDS--")
    print (*player.cards, sep= '\n ')
    print("Player's Hand =",player.value)

while True:
    rules =  input("Let's play a game of blackjack! Do you know how to play? 'Y' = yes 'N' = no: ")
    if rules.lower() == 'y':
        pass
    elif rules.lower() == 'n':
        print ( '-Get as close to 21 as you can without going over!\n\
-Dealer hits until she reaches 17. Aces count as 1 or 11.')
        rules[0].lower == 'Y'

    #GAME BEGINNING
    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal_one())
    player_hand.add_card(deck.deal_one())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal_one())
    dealer_hand.add_card(deck.deal_one())

    player_chips = Chips()

    take_bet(player_chips)

    show_some(player_hand,dealer_hand)
    
    while playing:
        hit_or_stand(deck,player_hand)
        show_some(player_hand,dealer_hand)

        if player_hand.value > 21:
            player_busts(player_hand,dealer_hand,player_chips)
            break

    if player_hand.value < 17:

        while dealer_hand.value < 17:
            hit(deck,dealer_hand)

        show_all(player_hand,dealer_hand)

        if dealer_hand.value > 21:
            dealer_busts(player_hand,dealer_hand,player_chips)

        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)

        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)

        else:
            push(player_hand,dealer_hand)
    print ()
    print ("Player's winnings stand at",player_chips.total)
    new_game = input("Would you like to play again? Enter 'y' or 'n': ")

    if new_game[0].lower() == 'y':
        playing = True
        continue
    else:
        print("Thank you for playing!")
        break
    
    






































    




















                

































