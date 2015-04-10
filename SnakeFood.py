import pygame
import random


# Class which extends sprite and acts as the "food" the snake eats to get bigger
class SnakeFood(pygame.sprite.Sprite):
    # Constructor
    def __init__(self, game_screen, segment_dimensions, x_position, y_position, grid_max, snake_sprites, snake_handler):
        # Call the parent constructor
        super().__init__()

        # Seed the random number generator
        random.seed()

        # Set instance variables
        self.segment_width = segment_dimensions[0]  # The width of a grid unit of which the sprite should take up 1
        self.segment_height = segment_dimensions[1]  # The height of the grid unit of which the sprite should take up 1
        self.x_max = grid_max  # The maximum amount of units on the X axis
        self.y_max = grid_max  # The maximum amount of units on the Y axis
        self.x_position = x_position  # The initial X position of the food on the grid
        self.y_position = y_position  # The initial Y position of the good on the grid
        self.snake_sprites = snake_sprites  # A group (from pygame.sprite) that holds all the snake pieces
        self.snake_handler = snake_handler  # A SnakeHandler object that handles the snake for this game

        # Initialize the elements of the sprite used for drawing (image/rect)
        self.image = pygame.Surface([self.segment_width, self.segment_height])
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = self.x_position * self.segment_width
        self.rect.y = self.y_position * self.segment_height

    # Called when the food is eaten and should be regenerated in a new random location
    def eaten(self, speed_countdown, food):
        # Randomize position until no collision occurs with snake pieces
        while pygame.sprite.spritecollide(self, self.snake_sprites, False):
            self.randomize_position()

        # Tell the snake_handler it is time to grow
        self.snake_handler.grow(speed_countdown, food)


    # Called to randomize the position of the food on the screen
    def randomize_position(self):
        self.x_position = random.randint(0, self.x_max - 1)
        self.y_position = random.randint(0, self.y_max - 1)
        self.rect.x = self.x_position * self.segment_width
        self.rect.y = self.y_position * self.segment_height