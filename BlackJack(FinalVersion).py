from random import shuffle

suits = ("Diamonds", "Spades", "Hearts", "Clubs")
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': '4', 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}
playing = True

class Chips():

    def __init__(self, balance , accountowner):

        self.accountowner = accountowner
        self.balance = balance

    def __str__(self):

        return ("This is the balance of {}'s account: {}".format(self.accountowner, self.balance))

    def gainedchips(self, gainedvalue):

        self.balance = self.balance + gainedvalue

    def lostchips(self, lostvalue):

        self.balance = self.balance - lostvalue

    def bet(self):
        bet = int(input('What is your bet? '))
        if bet > self.balance:
            while bet > self.balance:
                print("You don't have all this money, buddy!")
                bet = int(input("what is your bet? "))
                if bet <= self.balance:
                    self.balance = self.balance - bet
                    break
        else:
            self.balance = self.balance - bet


class Hand():

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value = self.value + int(values[card.rank])
        if card.rank == 'Ace':
            self.aces = self.aces + 1

    def adjust_for_aces(self):
        while self.value > 21 and self.aces > 0:
            self.value = self.value - 10
            self.aces = self.aces - 1


class Card():

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return self.rank + ' of ' + self.suit


class Deck():

    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(rank, suit))

    def __str__(self):
        for card in self.deck:
            print(card.__str__())

    def shuffle(self):
        shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card


def busted(s):
    return s > 21


def hit_or_stand():

    return input("\nDo you want to hit a card or stand?").upper().startswith('H')
    #if hit_or_stand():
        #w = deck.pop()
        #players_hand.append(w)
    #else:
        #pass


def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.adjust_for_aces()


def show_some(hand1, hand2):
    print('\n')
    print("Player's Hand: \n", *hand1.cards, "\nValue: ", hand1.value, sep= '\n')
    print('\n')
    print("Dealer's Hand: \n", hand2.cards[0])
    print('\n')


def show_all(hand1, hand2):
    print('\n')
    print("Player's Hand: \n", *hand1.cards, "\nValue: ", hand1.value, sep= '\n')
    print('\n')
    print("Dealer's Hand: \n", *hand2.cards, "\nValue: ", hand2.value, sep= '\n')
    print('\n')


def hit_a_card_to_the_dealer(sumdealer):
    return sumdealer <= 17

def replay():
    return input("Do you want to make another bet? Yes or No? ").upper().startswith("Y")
#if replay():
#   playing = True
#else:
#   print("Thank you for play!!!")

while True:
    print("Welcome to BlackJack!!!")
    print('\n')
    name = input('What is your name? ')
    balance = int(input("How much do you want to add in your account? "))
    account = Chips(balance, name)
    while playing:
        deck = Deck()
        deck.shuffle()
        players_hand = Hand()
        dealers_hand = Hand()
        players_hand.add_card(deck.deal())
        dealers_hand.add_card(deck.deal())
        players_hand.add_card(deck.deal())
        dealers_hand.add_card(deck.deal())
        account.bet()
        bet = int(input("Please confirm your bet: "))
        show_some(players_hand, dealers_hand)
        while hit_or_stand():
            hit(deck, players_hand)
            show_some(players_hand, dealers_hand)
            if busted(players_hand.value):
                print("Player Busted, you lost the game!!")
                account.lostchips(0)
                print("Your balance is: ", account.balance)
                if replay():
                    break
                else:
                    print("You finished the game with {} in your account!".format(account.balance))
                    print("Thank you for play!!!")
                    exit()
            else:
                pass
        else:
            show_all(players_hand, dealers_hand)
            hit_a_card_to_the_dealer(dealers_hand.value)
            while hit_a_card_to_the_dealer(dealers_hand.value):
                hit(deck, dealers_hand)
                show_all(players_hand, dealers_hand)
                if busted(dealers_hand.value):
                    print("Dealer was busted! Player Win!")
                    account.gainedchips(bet*2)
                    print("Your balance is: ", account.balance)
                    if replay():
                        continue
                    else:
                        print("You finished the game with {} in your account!".format(account.balance))
                        print("Thank you for play!!!")
                        exit()

                else:
                    pass
            else:
                if players_hand.value > dealers_hand.value and players_hand.value <= 21 and dealers_hand.value <= 21:
                    print("Player Win!!!")
                    account.gainedchips(bet*2)
                    print("Your balance is: ", account.balance)
                    if replay():
                        continue
                    else:
                        print("You finished the game with {} in your account!".format(account.balance))
                        print("Thank you for play!!!")
                        exit()

                elif players_hand.value == dealers_hand.value:
                    print("The game is draw!!!")
                    account.gainedchips(bet)
                    print("Your balance is: ", account.balance)
                    if replay():
                        continue
                    else:
                        print("You finished the game with {} in your account!".format(account.balance))
                        print("Thank you for play!!!")
                        exit()

                else:
                    print("Dealer Win!")
                    account.lostchips(0)
                    print("Your balance is: ", account.balance)
                    if replay():
                        continue
                    else:
                        print("You finished the game with {} in your account!".format(account.balance))
                        print("Thank you for play!!!")
                        exit()