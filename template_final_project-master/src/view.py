import pygame

class View:
    """
    view class that handles displaying the GUI (menu, game screen, and game over screen).
    
    args:
        screen (pygame.Surface): The screen surface where the game will be displayed.
    """
    def __init__(self, screen):
        self.screen = screen

    def draw_menu(self):
        """
        draws the menu screen with a play button.
        
        return: none
        """
        self.screen.blit(pygame.image.load("assets/menuscreen.jpg"), (0, 0))
        # draw button 
        pygame.draw.rect(self.screen, (0, 255, 0), pygame.Rect(300, 200, 200, 50))  # play button
        pygame.display.update()

    def draw_game(self, spaceship, asteroids, score):
        """
        Draws the game screen with the spaceship, asteroids, and score.
        
        args:
            spaceship (pygame.sprite.Sprite): The player's spaceship.
            asteroids (pygame.sprite.Group): Group containing all active asteroids.
            score (int): The current player's score.
        
        return: None
        """
        self.screen.blit(pygame.image.load("assets/gamescreen.jpg"), (0, 0))
        spaceship_group = pygame.sprite.Group()
        spaceship_group.add(spaceship)
        spaceship_group.draw(self.screen)
        asteroids_group = pygame.sprite.Group()
        asteroids_group.add(*asteroids)
        asteroids_group.draw(self.screen)
        self.screen.blit(pygame.font.SysFont("Arial", 36).render(f"Score: {score}", True, (255, 255, 255)), (10, 10))
        pygame.display.update()

    def draw_game_over(self, score):
        """
        draws the game over screen with the score and a try again button.
        
        args:
            score (int): the score to display on the game over screen.
        
        return:  none
        """
        self.screen.blit(pygame.image.load("assets/gameoverscreen.jpg"), (0, 0))
        self.screen.blit(pygame.font.SysFont("Arial", 48).render(f"Score: {score}", True, (255, 0, 0)), (250, 200))
        pygame.draw.rect(self.screen, (0, 255, 0), pygame.Rect(300, 300, 200, 50))  # try Again button
        pygame.display.update()