import pygame
from classes import drawing, logic, snake_obj, apple_obj
from config import screen_resolution, fps, running


pygame.init()
clock = pygame.time.Clock()

screen = drawing.GameDrawing(screen_resolution)
game_logic = logic.GameLogic()
snake = snake_obj.SnakeObject(screen_resolution)
apple = apple_obj.AppleObject(screen_resolution)

while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake.movement_direction != "DOWN":
                snake.movement_direction = "UP"
            elif event.key == pygame.K_DOWN and snake.movement_direction != "UP":
                snake.movement_direction = "DOWN"
            elif event.key == pygame.K_LEFT and snake.movement_direction != "RIGHT":
                snake.movement_direction = "LEFT"
            elif event.key == pygame.K_RIGHT and snake.movement_direction != "LEFT":
                snake.movement_direction = "RIGHT"
    game_logic.eating_an_apple(screen_resolution, snake, apple)
    snake.snake_movement()
    screen.screen_draw(snake, apple)
    # if game_logic.collision_with_screen_edge(screen_resolution, snake) == False or \
    #         game_logic.collision_snake_with_his_tail(snake) == False:
    #     running = False
    pygame.display.flip()
    clock.tick(fps)

pygame.quit()
