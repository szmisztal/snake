import pygame


class GameDrawing:
    def __init__(self, screen_resolution):
        self.screen = pygame.display.set_mode(screen_resolution)
        self.red_color = (255, 0, 0)
        self.blue_color = (0, 0, 255)
        self.green_color = (0, 255, 0)

    def screen_draw(self, snake):
        self.screen.fill(self.green_color)
        for part in snake.snake_parts_position:
            pygame.draw.rect(self.screen, self.blue_color, pygame.Rect(part[0], part[1], 10, 10))


