import random

class Hat:
    def __init__(self, **balls):
        self.contents = []
        for ball_name, amount in balls.items():
            self.add_balls(ball_name, amount)

    def add_balls(self, name, amount):
        self.contents += [name] * amount

    def draw(self, amount):
        drawn = self.draw_without_remove(amount)
        for ball in drawn:
            self.contents.remove(ball)
        return drawn

    def draw_without_remove(self, amount):
        if amount > len(self.contents):
            return self.contents[:]
        return random.sample(self.contents, k=amount)


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
