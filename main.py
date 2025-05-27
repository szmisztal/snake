import pygame
from config import screen_resolution
from classes import drawing, logic


pygame.init()
game_drawing = drawing.GameDrawing(screen_resolution)
game = logic.GameLogic(screen_resolution)
game.game_loop(game_drawing)
pygame.quit()
