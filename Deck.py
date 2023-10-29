import random
from Cards import Card

class Deck:
    def __init__(self):
        self.__deck = []
        self.__hand = []
        self.create()
        self.shuffle_deck()

    def create(self):
        shape = ['diamonds', 'hearts', 'spades', 'clubs']
        for i in range(2,15):
            for j in shape:
                self.__deck.append(Card(i, j))
        self.__deck.append(Card(15, 'color'))
        self.__deck.append(Card(15, 'black'))

    def shuffle_deck(self):
        random.shuffle(self.__deck)

    def sort_deck_by_rank(self):
        new_list = []
        for i in sorted(self.__deck, key=lambda x: x.rank):
            new_list.append(i)
        self.__deck = new_list

    def sort_deck_by_shape(self):
        new_list = []
        for i in sorted(self.__deck, key=lambda x: x.shape):
            new_list.append(i)
        self.__deck = new_list

    def deal_hand(self, num):
        self.__hand = []
        for i in range(num):
            self.__hand.append(self.draw())
        return self.__hand

    def draw(self):
        return self.__deck.pop()

    def count_cards(self):
        count_list = []
        for i in range(2, 16):
            count = 0
            for j in self.__deck:
                if i == j.rank:
                    count += 1
            count_list.append((i, count))
        return count_list

    def get_hand(self):
        return self.__hand

    def __len__(self):
        return len(self.__deck)

    def __str__(self):
        return f'{self.__deck}'

    def __getitem__(self, item):
        return self.__deck[item]

