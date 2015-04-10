import pygame
import SnakePortion
import SnakeFood
import SnakeHandler
import GameText


class GameHandler(object):
    # Constructor
    def __init__(self, game_screen):
        # Instance variables for this singleton
        self.game_screen = game_screen
        self.all_game_sprites = pygame.sprite.Group()
        self.snake_sprites = pygame.sprite.Group()
        self.game_text = []
        self.speed = 10
        self.speed_countdown = self.speed
        unit_count = 50
        unit_width = game_screen.get_width() / unit_count
        unit_height = game_screen.get_height() / unit_count
        unit_dimensions = (unit_width, unit_height)
        center_width = game_screen.get_width() / 2
        center_height = game_screen.get_height() / 2

        # Setup the initial condition of the snake (just the head)
        self.snake_head = SnakePortion.SnakePortion(game_screen, unit_width, unit_height, 5, 5, 0)
        self.snake_sprites.add(self.snake_head)

        # Create the snake handler object which will handle many of the snake requirements (growth, direction changes)
        self.snake_handler = SnakeHandler.SnakeHandler(self.snake_head, self.snake_head, self.snake_sprites)

        # Create a sprite that will contain the food object
        self.food = SnakeFood.SnakeFood(game_screen, unit_dimensions, 20, 20, unit_count, self.snake_sprites, self.snake_handler)

        # Add all created sprites to the master list
        self.all_game_sprites.add(self.snake_head)
        self.all_game_sprites.add(self.food)

        # initializes Game Over Text
        self.game_over = GameText.GameText(game_screen, center_width - 160, center_height-50, "GAME OVER: Press Space to"
                                                                                              " Try Again")
        self.game_text.append(self.game_over)

    def game_logic(self):
        # Update the speed countdown
        self.speed_countdown -= 1

        # Update all the snake sprites sprites
        self.snake_sprites.update(self.food, self.speed_countdown)

        # Add new snake sprites to the master group of sprites
        self.all_game_sprites.add(self.snake_sprites)

        # Update the SnakeHandler object for direction propagation
        self.snake_handler.update(self.speed_countdown)

        # Reset the speed countdown if it's at 0
        if self.speed_countdown == 0:
            self.speed_countdown = self.speed

    def draw_game_objects(self):
        self.all_game_sprites.draw(self.game_screen)
        if self.snake_head.reset == 1:
            self.game_text[0].game_object_draw()

    def process_event(self, event):
        # For all 4 directions, move the snake then propagate a direction change with the SnakeHandler
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                #self.snake_head.change_direction(0)
                self.snake_handler.propagate_direction_change(0)
            if event.key == pygame.K_DOWN:
                #self.snake_head.change_direction(2)
                self.snake_handler.propagate_direction_change(2)
            if event.key == pygame.K_LEFT:
                #self.snake_head.change_direction(3)
                self.snake_handler.propagate_direction_change(3)
            if event.key == pygame.K_RIGHT:
                self.snake_handler.propagate_direction_change(1)
                #self.snake_head.change_direction(1)
            if self.snake_head.reset == 1:
                if event.key == pygame.K_SPACE:
                    self.snake_head.reset_game()


