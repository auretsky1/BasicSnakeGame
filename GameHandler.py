import pygame
import SnakePortion
import SnakeFood
import GameText


class GameHandler(object):
    # Constructor
    def __init__(self, game_screen):
        # Instance variables for this singleton
        self.game_screen = game_screen
        self.all_game_sprites = pygame.sprite.Group()
        self.snake_sprites = pygame.sprite.Group()
        self.game_text = []
        self.speed = 5
        self.speed_countdown = self.speed
        unit_count = 50
        self.unit_width = game_screen.get_width() / unit_count
        self.unit_height = game_screen.get_height() / unit_count
        unit_dimensions = (self.unit_width, self.unit_height)
        center_width = game_screen.get_width() / 2
        center_height = game_screen.get_height() / 2
        self.game_ended = 0  # Has the game ended?

        # Setup the initial condition of the snake (just the head w/ tail pointing to the head)
        self.snake_head = SnakePortion.SnakePortion(game_screen, self.unit_width, self.unit_height, 5, 5, 0)
        self.snake_tail = self.snake_head
        self.snake_sprites.add(self.snake_head)

        # Create a sprite that will contain the food object
        self.food = SnakeFood.SnakeFood(game_screen, unit_dimensions, 10, 10, unit_count, self.snake_sprites)

        # Add all created sprites to the master list
        self.all_game_sprites.add(self.snake_head)
        self.all_game_sprites.add(self.food)

        # initializes Game Over Text
        self.game_over = GameText.GameText(game_screen, center_width - 160, center_height-50, "GAME OVER: Press Space to"
                                                                                              " Try Again")
        self.game_text.append(self.game_over)

        # The current direction input by the user (does not get processed till speed_countdown is 0)
        self.user_input = None

        # List that holds direction changes to be passed down the snake chain
        # This list will contain lists that have a direction and the next snake piece to get changed
        # In the format: [[direction, snake_piece]]
        self.direction_changes = []

    def game_logic(self):
        # If the game has ended do not do normal processing
        if self.game_ended == 1:
            return

        # Update the speed countdown
        self.speed_countdown -= 1

        # Process the snake sprites if the countdown has reached 0
        if self.speed_countdown == 0:
            # Take the users most recent input into account if the game hasn't ended
            if self.user_input is not None:
                # Only process direction change is snake isn't already moving in that direction
                if self.snake_head.direction != self.user_input:
                    # Append the direction change
                    self.direction_changes.append([self.user_input, self.snake_head])

                # Either way set the users input back to None
                self.user_input = None

            # Propagate direction changes
            if self.direction_changes:  # There is at least one queued direction change
                for direction_change in self.direction_changes:
                    # Direction change should be in form of: [direction, snake_piece]
                    direction_change[1].change_direction(direction_change[0])

                    # Set the snake piece to be the next snake piece in the chain
                    direction_change[1] = direction_change[1].next_portion

                # Remove empty direction changes from the queue
                for direction_change in self.direction_changes:
                    if direction_change[1] is None:
                        self.direction_changes.remove(direction_change)

            # Update all the snake sprites
            self.snake_sprites.update()

            # Check if the snake has eaten the food and if so call eaten/grow
            if pygame.sprite.collide_rect(self.snake_head, self.food):
                new_snake_portion = self.snake_tail.grow()
                self.food.eaten()

                # Set the tail to be the new portion of the snake
                self.snake_tail = new_snake_portion

                # Add the snake portion to the snake_portion group and master group
                self.snake_sprites.add(new_snake_portion)
                self.all_game_sprites.add(new_snake_portion)

            # Check if the snake has collided with any of the walls and if so reset the game
            if self.snake_head.x_position < 0 or self.snake_head.x_position >= 50:
                self.game_ended = 1  # Set game over flag
                self.end_game()  # Call the game over routine
            elif self.snake_head.y_position < 0 or self.snake_head.y_position >= 50:
                self.game_ended = 1  # Set game over flag
                self.end_game()  # Call the game over routine
            elif 1 == 0:  # Add the check for collision against the snake body here
                pass

            # Reset the speed countdown if it's at 0
            self.speed_countdown = self.speed

    # The game has ended because the snake collided, change settings to reflect this
    def end_game(self):
        # First set the game_ended flag to be true
        self.game_ended = 1

        # Second remove all the snake sprites from the snake sprites/master sprites list
        self.all_game_sprites.remove(self.snake_sprites)  # Remove the snake sprites from the master list
        self.snake_sprites.empty()  # Remove the snake sprites from the snake list

        # Next clear the direction changes list
        self.direction_changes.clear()

    def reset_game(self):
        self.snake_head = SnakePortion.SnakePortion(self.game_screen, self.unit_width, self.unit_height, 5, 5, 0)
        self.snake_tail = self.snake_head
        self.snake_sprites.add(self.snake_head)
        self.all_game_sprites.add(self.snake_head)
        self.game_ended = 0

    def draw_game_objects(self):
        self.all_game_sprites.draw(self.game_screen)
        if self.game_ended == 1:
            self.game_text[0].game_object_draw()

    def process_event(self, event):
        # Move the snake head then propagate a direction change with the direction_changes list
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.user_input = 0
            if event.key == pygame.K_DOWN:
                self.user_input = 2
            if event.key == pygame.K_LEFT:
                self.user_input = 3
            if event.key == pygame.K_RIGHT:
                self.user_input = 1
            if event.key == pygame.K_SPACE and self.game_ended == 1:
                self.reset_game()


