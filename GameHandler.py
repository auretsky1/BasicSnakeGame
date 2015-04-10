import pygame
import SnakePortion
import GameText

class GameHandler(object):

    def __init__(self, game_screen):
        self.game_screen = game_screen
        self.all_game_sprites = pygame.sprite.Group()
        self.snake_sprites = pygame.sprite.Group()
        self.game_text = []
        self.grid = []
        self.unit_width = game_screen.get_width()/50
        self.unit_height = game_screen.get_height()/50
        center_width = game_screen.get_width()/2
        center_height = game_screen.get_height()/2

        # creates game grid
        # for unit_width in range(game_screen.get_width()):
        #     self.grid.append([])
        #     for unit_height in range(game_screen.get_height()):
        #         self.grid[unit_width].append(0)
        # # sets center to index 0
        # self.grid[50][50] = 0
        # initializes player
        self.snake_head = SnakePortion.SnakePortion(game_screen, self.unit_width, self.unit_height, 5, 5, 0)

        self.all_game_sprites.add(self.snake_head)
        self.snake_sprites.add(self.snake_head)

        # initializes Game Over Text
        self.game_over = GameText.GameText(game_screen, center_width - 160, center_height-50, "GAME OVER: Press Space to"
                                                                                              " Try Again")
        
        self.game_text.append(self.game_over)

    def game_logic(self):
        self.all_game_sprites.update(self.game_screen)

    def draw_game_objects(self):
        self.all_game_sprites.draw(self.game_screen)
        if self.snake_head.reset == 1:
            self.game_text[0].game_object_draw()


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
                if self.snake_head.reset == 1:
                    if event.key == pygame.K_SPACE:
                        self.snake_head.reset_game()




