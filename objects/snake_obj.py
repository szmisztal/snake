import pygame

class SnakeObject:
    def __init__(self, x_pos , y_pos, height, width):
        self._x_pos = x_pos
        self._y_pos = y_pos
        self._height = height
        self._width = width

    @property
    def x_pos(self):
        return self._x_pos

    @x_pos.setter
    def x_pos(self, value):
        self.x_pos = value

    @property
    def y_pos(self):
        return self._y_pos

    @y_pos.setter
    def y_pos(self, value):
        self._y_pos = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

