import pygame
import SnakePortion


# This class handles all the pieces of the snake including growing it and propagating direction changes
class SnakeHandler(object):
    # Constructor
    def __init__(self, snake_head, snake_tail, snake_sprites):
        # Set instance variables
        self.snake_head = snake_head
        self.snake_tail = snake_tail
        self.snake_sprites = snake_sprites

        # List that holds direction changes to be propagated
        self.direction_changes = []

    # Grow the snake by one unit positioning it behind the tail opposite to it's moving direction
    def grow(self, speed_countdown, food):
        # First determine the direction from the tail where the piece should be added
        add_direction = self.snake_tail.direction + 2  # Slide two direction to get the opposite direction
        if add_direction > 3:  # Required for down and left which would be 4/5 respectively
            add_direction = ((add_direction % 3) - 1)  # Use clock arithmetic to get real values

        # Next determine the actual positions by the direction calculated above
        if add_direction == 0:  # Should appear one above the tail
            x_position = self.snake_tail.x_position
            y_position = self.snake_tail.y_position - 1
        elif add_direction == 1:  # Should appear to the right of the tail
            x_position = self.snake_tail.x_position + 1
            y_position = self.snake_tail.y_position
        elif add_direction == 2:  # Should appear below the tail
            x_position = self.snake_tail.x_position
            y_position = self.snake_tail.y_position + 1
        elif add_direction == 3:  # Should appear to the left of the tail
            x_position = self.snake_tail.x_position - 1
            y_position = self.snake_tail.y_position

        # Create the new SnakePortion object using the above calculated positions
        new_portion_of_snake = SnakePortion.SnakePortion(self.snake_head.game_screen,
                                                         self.snake_head.segment_width,
                                                         self.snake_head.segment_height,
                                                         x_position, y_position, 0)

        # Set the direction of the new portion to follow the snake
        new_portion_of_snake.change_direction(self.snake_tail.direction)

        # Add the new portion to the snake sprites
        self.snake_sprites.add(new_portion_of_snake)

        # Perform a force invoke if the head does not equal the tail
        if self.snake_head != self.snake_tail:
            # Force invoke the update for the new sprite
            new_portion_of_snake.update(food, speed_countdown)

        # Make the tail point to the new tail
        self.snake_tail.next_portion = new_portion_of_snake

        # Make the new portion of snake the new tail
        self.snake_tail = new_portion_of_snake

    # Update method called each frame, processes direction changes
    def update(self, *args):
        if self.direction_changes:  # Do this if the direction_changes list is not empty
            for direction_change in self.direction_changes:  # Process each direction change independently
                # First set the current_piece to the piece pointed to be direction_change
                current_snake_piece = direction_change[1]  # The sprite object to have it's direction changed

                # Now process the direction change for that piece
                if current_snake_piece is None:  # The direction change has been fully propagated
                    self.direction_changes.remove(direction_change)  # Remove it from the list
                # This is the first time current piece has moved, wait for the next time to propagate change
                # elif args[0] == 1 and direction_change[2] is False:
                #     direction_change[2] = True
                # Ready to move a second time, propagate the change
                elif args[0] == 1 and direction_change[2] is False:
                    # Perform the change on the current piece
                    current_snake_piece.change_direction(direction_change[0])

                    # Now make the direction change point to the next piece of the snake
                    direction_change[1] = current_snake_piece.next_portion

    # Called to add a direction propagation to the internal list
    def propagate_direction_change(self, direction):
        self.direction_changes.append([direction, self.snake_head, False])