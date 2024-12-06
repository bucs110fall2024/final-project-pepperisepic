import pygame
from laser import Laser
import pygame

class Spaceship(pygame.sprite.Sprite):
    """
    spaceship class that controls the player's spaceship.
    
    args:
        x (int): Starting X position of the spaceship.
        y (int): Starting Y position of the spaceship.
    """
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("assets/spaceshipright.png")  # default image
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.velocity = 5  # movement speed

    def move_left(self):
        """
        moves the spaceship to the left and updates its image to 'spaceship_left'.
        
        return: none
        """
        self.rect.x -= self.velocity
        self.image = pygame.image.load("assets/spaceshipleft.png")

    def move_right(self):
        """
        moves the spaceship to the right and updates its image to 'spaceship_right'.
        
        return: none
        """
        self.rect.x += self.velocity
        self.image = pygame.image.load("assets/spaceship_right.png")

    def shoot(self):
        """
        creates and returns a laser object shot from the spaceship's position.
        
        return: Laser object
        """
        laser = Laser(self.rect.centerx, self.rect.top, self.image)
        return laser