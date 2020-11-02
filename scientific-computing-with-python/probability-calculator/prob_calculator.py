import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **balls):
        self.contents = []
        for ball_name, amount in balls.items():
            self.add_balls(ball_name, amount)

    def add_balls(self, name, amount):
        self.contents += [name] * amount

    def draw(self, amount):
        drawn = random.sample(self.contents, k=amount)
        for ball in drawn:
            self.contents.remove(ball)
        return drawn


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
