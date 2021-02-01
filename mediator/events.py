class Event(list):

    def __call__(self, *args, **kwargs):
        for item in self:
            item(*args, **kwargs)


class Game:
    """
    An Event-Based Mediator
    """

    def __init__(self):
        self.events = Event()

    def update(self, args):
        self.events(args)


class ScoreInfo:

    def __init__(self, player, score):
        self.player = player
        self.score = score


class Player:

    def __init__(self, name, game):
        self.name = name
        self.game = game
        self.score = 0

    def update_score(self, increment):
        self.score += increment
        args = ScoreInfo(self, self.score)
        self.game.update(args)


class Coach:

    def __init__(self, game):
        game.events.append(self.celebrate)

    def celebrate(self, args):
        if isinstance(args, ScoreInfo) and args.score < 3:
            print(f'Coach praises {args.player.name}')


if __name__ == '__main__':
    game = Game()
    player = Player('John', game)
    coach = Coach(game)

    player.update_score(1)
    player.update_score(1)
    player.update_score(1)
