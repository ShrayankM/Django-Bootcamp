#SUITS ARE NOT IMPORTANT
#Game Description at link below
#https://en.wikipedia.org/wiki/War_(card_game)

import random
from random import shuffle
faces = ['A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2']
priority = {'A':13, 'K':12, 'Q':11, 'J':10, '10':9, '9':8, '8':7, '7':6, '6':5, '5':4, '4':3, '3':2, '2':1}

def get_priority(face):
    return priority[face]

class Deck:
    def __init__(self):
        self.d = []

    def create_deck(self):
        for i in range(0, 4):
            for f in faces:
                self.d.append(f)
        random.shuffle(self.d)

    def partition(self):
        L = int(len(self.d)/2)
        d1 = self.d[:L]
        d2 = self.d[L:]
        return d1, d2

class Player:
    def __init__(self, hand):
        self.hand = hand
        self.current = ""
        self.bet = []

    def check_hand(self):
        return len(self.hand)

    def get_top(self):
        return self.hand.pop(0)

    def add_to_hand(self, list):
        for i in list:
            self.hand.append(i)

    def add_to_bet(self, i, n):
        self.bet.append(i)
        if self.check_hand() >= n:
            for j in range(n):
                self.bet.append(self.hand.pop(0))
        else:
            while self.check_hand() > 0:
                self.bet.append(self.hand.pop(0))

    def clear_bet(self):
        self.bet = []

def Game(p1, p2):
    war = False
    while p1.check_hand() != 0 and p2.check_hand() != 0:
        p1.current = p1.get_top()
        p2.current = p2.get_top()

        if get_priority(p1.current) > get_priority(p2.current):
            war = False
            p1.hand.append(p1.current)
            p1.hand.append(p2.current)
            p1.add_to_hand(p2.bet)
            p1.add_to_hand(p1.bet)
            p1.clear_bet()
            p2.clear_bet()
        elif get_priority(p1.current) < get_priority(p2.current):
            war = False
            p2.hand.append(p2.current)
            p2.hand.append(p1.current)
            p2.add_to_hand(p1.bet)
            p2.add_to_hand(p2.bet)
            p1.clear_bet()
            p2.clear_bet()
        else:
            print(f"DECK1: {p1.check_hand()}, DECK2: {p2.check_hand()}")
            if war == False:
                p1.add_to_bet(p1.current, 2)
                p2.add_to_bet(p2.current, 2)
                war = True
            else:
                p1.add_to_bet(p1.current, 0)
                p2.add_to_bet(p2.current, 0)

    if p1.check_hand() == 0:
        print("Player 2 has won")
    else:
        print("Player 1 has won")

if __name__ == "__main__":
    deck = Deck()
    deck.create_deck()
    d1, d2 = deck.partition()
    p1 = Player(d1)
    p2 = Player(d2)

    print(f"DECK1: {p1.check_hand()}, DECK2: {p2.check_hand()}")
    Game(p1, p2)
