from Deck import Deck


class Player:
    def __init__(self, name: str, hand):
        self.name = name
        self.hand = hand

    def __repr__(self):
        return self.name


class Game:
    def __init__(self, name1, name2, deck):
        self.player1 = Player(name1, deck.deal_hand(27))
        self.player2 = Player(name2, deck.deal_hand(27))
        self.score = {name1: 0, name2: 0}
        self.round_list1 = []
        self.round_list2 = []

    def add_round(self, n):
        while n > 0 and not self.check_end_game():
            self.round_list1.append(self.player1.hand.pop(0))
            self.round_list2.append(self.player2.hand.pop(0))
            n -= 1


    def check_end_game(self):
        return len(self.player1.hand) == 0 or len(self.player2.hand) == 0

    def who_won(self):
        if self.round_list1[-1] > self.round_list2[-1]:
            self.winner_round(self.player1)
        else:
            self.winner_round(self.player2)

    def winner_round(self, win):
        win.hand.extend(self.round_list1)
        win.hand.extend(self.round_list2)
        self.score[win.name] += 1
        self.round_list1.clear(), self.round_list2.clear()


    def round(self):
        self.add_round(1)
        while self.round_list1[-1] == self.round_list2[-1]:
            self.add_round(4)
        self.who_won()

    def show_winner(self):
        if len(self.player2.hand) == len(self.player1.hand):
            print("equal, no winner")
            return
        if len(self.player2.hand) > len(self.player1.hand):
            winner, loser = self.player2, self.player1
        else:
            winner, loser = self.player1, self.player2
        print(
            f"The winner of the war card game is {winner} has {len(winner.hand)} amount of cards and won {self.score[winner.name]},The big loser is {loser} ")

    def flow_round(self, rounds=float('inf')):
        while rounds > 0 and not self.check_end_game():
            self.round()
            rounds -= 1
        return self.show_winner()
a = Game("yitschak","elhanan",Deck())
a.flow_round(56)
