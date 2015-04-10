import pygame
import GameHandler

# Constants
screen_size = (500, 500)
screen_flags = 0
screen_depth = 0

# Color constants
screen_clear_color = (0, 0, 0)

# Variables
is_game_running = True

# Initialize PyGame
pygame.init()
pygame.font.init()

# Setup the program window
pygame.display.set_caption("Snake Game")

# Initialize the screen
game_screen = pygame.display.set_mode(screen_size, screen_flags, screen_depth)
game_handler = GameHandler.GameHandler(game_screen)

# Create the game clock
game_clock = pygame.time.Clock()

# Main game loop
while is_game_running:
    # Process events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_game_running = False
        if event.type == pygame.KEYDOWN:
            game_handler.process_event(event)

    # Do game logic
    game_handler.game_logic()

    # Clear the screen
    game_screen.fill(screen_clear_color)

    # Draw game objects
    game_handler.draw_game_objects()

    # Draw the screen
    pygame.display.flip()

    # Frame-rate
    game_clock.tick(60)