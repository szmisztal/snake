import pygame
from config import screen_resolution, running, green_color, blue_color, red_color, white_color
from objects.snake_obj import SnakeObject


pygame.init()
screen = pygame.display.set_mode(screen_resolution)
clock = pygame.time.Clock()
snake = SnakeObject(screen_resolution[0]/2, screen_resolution[1]/2, 10, 10)

while running:
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.draw.rect(screen, blue_color, pygame.Rect(snake.x_pos, snake.y_pos, snake.width, snake.height))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
