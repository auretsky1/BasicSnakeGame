import pygame
import SnakePortion

class GameHandler(object):

    def __init__(self, game_screen):
        self.game_screen = game_screen
        self.all_game_sprites = pygame.sprite.Group()
        self.snake_sprites = pygame.sprite.Group()
        self.grid = []
        unit_width = game_screen.get_width()/50
        unit_height = game_screen.get_height()/50

        # creates game grid
        # for unit_width in range(game_screen.get_width()):
        #     self.grid.append([])
        #     for unit_height in range(game_screen.get_height()):
        #         self.grid[unit_width].append(0)
        # # sets center to index 0
        # self.grid[50][50] = 0
        # initializes player
        self.snake_head = SnakePortion.SnakePortion(game_screen, unit_width, unit_height, 5, 5)

        self.all_game_sprites.add(self.snake_head)
        self.snake_sprites.add(self.snake_head)

    def game_logic(self):
        self.all_game_sprites.update()

    def draw_game_objects(self):
        self.all_game_sprites.draw(self.game_screen)

    def process_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.snake_head.change_direction(0)
            if event.key == pygame.K_DOWN:
                self.snake_head.change_direction(2)
            if event.key == pygame.K_LEFT:
                self.snake_head.change_direction(3)
            if event.key == pygame.K_RIGHT:
                self.snake_head.change_direction(1)


