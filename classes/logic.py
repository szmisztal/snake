class GameLogic:
    def collision_with_screen_edge(self, screen_resolution, snake):
        if (snake.parts_position[0][0] < 0 or snake.parts_position[0][0] >= screen_resolution[0]) or \
                (snake.parts_position[0][1] < 0 or snake.parts_position[0][1] >= screen_resolution[1]):
            return False

    def collision_snake_with_his_tail(self, snake):
        if snake.parts_position[0] in snake.parts_position[2:]:
            return False

    def eating_an_apple(self, screen_resolution, snake, apple):
        if snake.parts_position[0][0] + 5 == apple.coordinates[0] and snake.parts_position[0][1] + 5 == apple.coordinates[1]:
            snake.parts_position.insert(1, [snake.parts_position[0][0], snake.parts_position[0][1]])
            apple.new_coordinates(screen_resolution)


