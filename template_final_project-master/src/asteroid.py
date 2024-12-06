import pygame
class Asteroid(pygame.sprite.Sprite):
    """
    asteroid class for controlling asteroid objects.
    
    args:
        x (int): starting X position of the asteroid.
        y (int): starting Y position of the asteroid.
    """
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("assets/asteroid.png")
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self):
        """
        moves the asteroid to the left and resets its position when it leaves the screen.
        
        return: none
        """
        self.rect.x -= 5  # move toward the left
        if self.rect.right < 0:  # if it goes off screen
            self.rect.left = 800  # reset position




            
        
            