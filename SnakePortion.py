import pygame


class SnakePortion(pygame.sprite.Sprite):
    def __init__(self, game_screen, segment_width, segment_height, x_position, y_position):

        # snakeportion constructor
        self.x_position = x_position
        self.y_position = y_position
        self.segment_width = segment_width
        self.segment_height = segment_height
        self.speed = 60
        self.speed_countdown = self.speed
        self.direction = 1

        # calls upon Sprite constructor
        super().__init__()
        self.image = pygame.Surface([self.segment_width, self.segment_height])
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.x = x_position * segment_width
        self.rect.y = y_position * segment_height

    def update(self, *args):
        self.speed_countdown -= 1
        if self.speed_countdown == 0:
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
            self.speed_countdown = self.speed

    def change_direction(self, direction):
        self.direction = direction



    def game_object_draw(self):
        pass
