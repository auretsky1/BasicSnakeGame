import pygame
import GameHandler


class SnakePortion(pygame.sprite.Sprite):

    # Constructor
    def __init__(self, game_screen, segment_width, segment_height, x_position, y_position, reset):
        # Instance variables for this object
        self.game_screen = game_screen
        self.x_position = x_position
        self.y_position = y_position
        self.segment_width = segment_width
        self.segment_height = segment_height
        self.direction = 1

        # Call the parent class's constructor
        super().__init__()

        # Set variables pertaining to the Sprite class
        self.image = pygame.Surface([self.segment_width, self.segment_height])
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.x = x_position * segment_width
        self.rect.y = y_position * segment_height

        # Special variable that holds the next piece in the snake line
        self.next_portion = None  # Initialized to none as we assume new pieces always on tail

    # Update the snake portion object
    def update(self, *args):
        if self.direction == 0:
            self.y_position -= 1

        elif self.direction == 1:
            self.x_position += 1

        elif self.direction == 2:
            self.y_position += 1

        elif self.direction == 3:
            self.x_position -= 1

        self.rect.x = self.x_position * self.segment_width
        self.rect.y = self.y_position * self.segment_height

    # Simple setter method that changes the direction of this snake portion
    def change_direction(self, direction):
        self.direction = direction

    # Grow the snake by one unit positioning it behind the tail opposite to it's moving direction
    def grow(self):
        # First determine the direction from the tail where the piece should be added
        add_direction = self.direction + 2  # Slide two direction to get the opposite direction
        if add_direction > 3:  # Required for down and left which would be 4/5 respectively
            add_direction = ((add_direction % 3) - 1)  # Use clock arithmetic to get real values

        # Next determine the actual positions by the direction calculated above
        if add_direction == 0:  # Should appear one above the tail
            x_position = self.x_position
            y_position = self.y_position - 1
        elif add_direction == 1:  # Should appear to the right of the tail
            x_position = self.x_position + 1
            y_position = self.y_position
        elif add_direction == 2:  # Should appear below the tail
            x_position = self.x_position
            y_position = self.y_position + 1
        elif add_direction == 3:  # Should appear to the left of the tail
            x_position = self.x_position - 1
            y_position = self.y_position

        # Create the new SnakePortion object using the above calculated positions
        new_portion_of_snake = self.__class__(self.game_screen,
                                                         self.segment_width,
                                                         self.segment_height,
                                                         x_position, y_position, 0)

        # Set the initial direction of the new portion to follow the snake
        new_portion_of_snake.change_direction(self.direction)

        # Make the tail (self) point to the new tail
        self.next_portion = new_portion_of_snake

        # Return the new snake piece to the caller
        return new_portion_of_snake