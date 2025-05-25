import pygame
from config import screen_resolution, running, green_color, blue_color, red_color, white_color
from objects.snake_obj import SnakeObject


pygame.init()
screen = pygame.display.set_mode(screen_resolution)
clock = pygame.time.Clock()
snake = SnakeObject(screen_resolution[0]/2, screen_resolution[1]/2, 1)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.y_pos -= 10
            elif event.key == pygame.K_DOWN:
                snake.y_pos += 10
            elif event.key == pygame.K_LEFT:
                snake.x_pos -= 10
            elif event.key == pygame.K_RIGHT:
                snake.x_pos += 10

    if snake.x_pos < 0 or snake.x_pos >= screen_resolution[0]:
        running = False
    if snake.y_pos < 0 or snake.y_pos >= screen_resolution[1]:
        running = False

    screen.fill(green_color)
    pygame.draw.rect(screen, blue_color, pygame.Rect(snake.x_pos, snake.y_pos, 10, 10))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
