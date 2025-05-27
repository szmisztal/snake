import pygame
from classes.snake_obj import SnakeObject
from config import screen_resolution


class GameLogic:
    def __init__(self, screen_resolution):
        self.running = True
        self.snake = SnakeObject(screen_resolution)
        self.clock = pygame.time.Clock()

    def collision_with_screen_edge(self, screen_resolution):
        if self.snake.snake_parts_position[0][0] < 0 or self.snake.snake_parts_position[0][0] >= screen_resolution[0]:
            self.running = False
        if self.snake.snake_parts_position[0][1] < 0 or self.snake.snake_parts_position[0][1] >= screen_resolution[1]:
            self.running = False

    def game_loop(self, screen):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and self.snake.movement_direction != "DOWN":
                        self.snake.movement_direction = "UP"
                    elif event.key == pygame.K_DOWN and self.snake.movement_direction != "UP":
                        self.snake.movement_direction = "DOWN"
                    elif event.key == pygame.K_LEFT and self.snake.movement_direction != "RIGHT":
                        self.snake.movement_direction = "LEFT"
                    elif event.key == pygame.K_RIGHT and self.snake.movement_direction != "LEFT":
                        self.snake.movement_direction = "RIGHT"
            screen.screen_draw(self.snake)
            self.snake.snake_movement()
            self.collision_with_screen_edge(screen_resolution)
            pygame.display.flip()
            self.clock.tick(10)

