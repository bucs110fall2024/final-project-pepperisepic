import pygame
from laser import Laser

class Spaceship(pygame.sprite.Sprite):
    """
    spaceship class that controls the player's spaceship.
   
    args:
        x (int): Starting X position of the spaceship.
        y (int): Starting Y position of the spaceship.
    """
    def __init__(self, x, y):
        super().__init__()
        self.image_right = pygame.image.load("assets/spaceshipright.png")  # right image
        self.image_left = pygame.image.load("assets/spaceshipleft.png")  # left image
        self.image = self.image_right  # default image
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.velocity = 5  # movement speed

    def move_left(self):
        """
        moves the spaceship to the left and updates its image to 'spaceship_left'.
        """
        self.rect.x -= self.velocity
        self.image = self.image_left

    def move_right(self):
        """
        moves the spaceship to the right and updates its image to 'spaceship_right'.
        """
        self.rect.x += self.velocity
        self.image = self.image_right

    def shoot(self):
        """
        Creates and returns a laser object shot from spaceship's position.
        """
        direction = "left" if self.image == self.image_left else "right"
        laser = Laser(self.rect.centerx, self.rect.top, direction)
        return laser