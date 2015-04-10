import pygame


class GameText(object):
    def __init__(self, game_screen, x_position, y_position, text):
        self.game_screen = game_screen
        self.x_position = x_position
        self.y_position = y_position
        self.text = text

    def game_object_draw(self):
        font = pygame.font.SysFont("Callisto", 25)
        game_text = font.render(str(self.text), True, (255, 255, 255))
        self.game_screen.blit(game_text, (self.x_position, self.y_position))

