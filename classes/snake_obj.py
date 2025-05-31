import random


class SnakeObject:
    def __init__(self, screen_resolution):
        self.parts_position = [[screen_resolution[0] / 2, screen_resolution[1] / 2]]
        self.movement_direction = random.choice(["UP", "DOWN", "RIGHT", "LEFT"])
        self.grow = False

    def snake_movement(self):
        self.parts_position.insert(1, [self.parts_position[0][0], self.parts_position[0][1]])
        if self.movement_direction == "UP":
            self.parts_position[0][1] -= 10
        elif self.movement_direction == "DOWN":
            self.parts_position[0][1] += 10
        elif self.movement_direction == "LEFT":
            self.parts_position[0][0] -= 10
        else:
            self.parts_position[0][0] += 10
        self.check_snake_grow()

    def check_snake_grow(self):
        if not self.grow:
            self.parts_position.pop()
        else:
            self.grow = False
