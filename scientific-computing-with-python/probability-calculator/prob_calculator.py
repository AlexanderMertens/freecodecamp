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
    success_count = 0
    for _ in range(num_experiments):
        drawn = hat.draw_without_remove(num_balls_drawn)
        success = True
        for name, amount in expected_balls.items():
            if drawn.count(name) < amount:
                success = False
        if success:
            success_count += 1
    return success_count / num_experiments
