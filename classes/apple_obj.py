import random


class AppleObject:
    def __init__(self, screen_resolution):
        self.coordinates = self.establish_coordinates(screen_resolution)

    def establish_coordinates(self, screen_resolution):
        x = round(random.randint(5, screen_resolution[0]), -1)
        y = round(random.randint(5, screen_resolution[1]), -1)
        return (x - 5, y - 5)

    def new_coordinates(self, screen_resolution):
        self.coordinates = self.establish_coordinates(screen_resolution)
