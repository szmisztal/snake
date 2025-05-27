import random


class SnakeObject:
    def __init__(self, screen_resolution):
        self.snake_parts_position = [[screen_resolution[0]/2, screen_resolution[1]/2]]
        self.movement_direction = random.choice(["UP", "DOWN", "RIGHT", "LEFT"])
    def snake_movement(self):
        if self.movement_direction == "UP":
            self.snake_parts_position[0][1] -= 10
        elif self.movement_direction == "DOWN":
            self.snake_parts_position[0][1] += 10
        elif self.movement_direction == "LEFT":
            self.snake_parts_position[0][0] -= 10
        else:
            self.snake_parts_position[0][0] += 10
