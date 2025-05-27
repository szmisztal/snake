import random


class SnakeObject:
    def __init__(self, screen_resolution):
        self.snake_parts_position = [[screen_resolution[0]/2, screen_resolution[1]/2]]
        self.movement_direction = random.choice(["UP", "DOWN", "RIGHT", "LEFT"])


