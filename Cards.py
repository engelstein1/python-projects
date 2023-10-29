class Card:
    def __init__(self, rank, shape):
        self.shape = shape
        self.rank = rank

    def get_name(self):
        name = ''
        if self.rank == 11:
            name += 'jack'
        elif self.rank == 12:
            name += 'queen'
        elif self.rank == 13:
            name += 'king'
        elif self.rank == 14:
            name += 'ace'
        elif self.rank == 15:
            name += 'joker'
        else:
            name += f'{self.rank}'
        return name

    def __str__(self):
        return f'{self.get_name(), self.shape}'

    def __repr__(self):
        return self.__str__()

    def __gt__(self, other):
        return self.rank > other.rank

    def __lt__(self, other):
        return self.rank < other.rank

    def __eq__(self, other):
        return self.rank == other.rank
