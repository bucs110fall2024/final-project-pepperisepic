import pygame
class Laser(pygame.sprite.Sprite):
    """
    laser class for controlling laser projectiles fired from the spaceship.
    
    args:
        x (int): Starting X position of the laser.
        y (int): Starting Y position of the laser.
        direction (str): The direction in which the laser travels ("left" or "right").
    """
    def __init__(self, x, y, direction):
        super().__init__()
        self.image = pygame.Surface((5, 20))
        self.image.fill((255, 0, 0))  # red color
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.direction = direction  # left or right

    def update(self):
        """
        moves the laser in the specified direction and removes it when it leaves the screen.
        
        return: None
        """
        if self.direction == "left":
            self.rect.x -= 10
        else:
            self.rect.x += 10
        
        if self.rect.right < 0 or self.rect.left > 800:  # if it goes off screen
            self.kill()  # remove laser
            