"""
Unlike the strategy pattern, which separates common and specific functionalities of a feature
implementation via composition, the template method achieves this through inheritance.
"""
from abc import ABC, abstractmethod


class Game(ABC):

    def __init__(self, num_players):
        self.num_players = num_players
        self.curr_player = 0

    def run(self):
        """
        A template method that uses other methods defined by the interface,
        which then can be overriden via inheritance.
        """
        self.start()
        while not self.has_winner:
            self.take_turn()
        print(f'Player {self.winning_player} wins!')

    def start(self): pass

    @property
    @abstractmethod
    def has_winner(self): pass

    @abstractmethod
    def take_turn(self): pass

    @property
    @abstractmethod
    def winning_player(self): pass


class Chess(Game):

    def __init__(self):
        super().__init__(num_players=2)
        self.max_turns = 10
        self.curr_turn = 1

    def start(self):
        print('Starting a game of chess.')

    @property
    def has_winner(self):
        return self.curr_turn == self.max_turns

    def take_turn(self):
        print(f'Turn {self.curr_turn} taken by player {self.curr_player}')
        self.curr_turn += 1
        self.curr_player = 1 - self.curr_player

    @property
    def winning_player(self):
        return self.curr_player


if __name__ == '__main__':
    chess = Chess()
    chess.run()
