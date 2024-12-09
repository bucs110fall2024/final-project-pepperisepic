import pygame
class View:
    """
    View class that handles displaying the GUI (menu, game screen, and game over screen).
    """
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont("Arial", 36)  # Load font once

    def draw_menu(self):
        """Draws the menu screen with a play button."""
        self.screen.fill((0, 0, 0))  # Clear screen (black)
        self.screen.blit(pygame.image.load("assets/menuscreen.jpg"), (0, 0))
        pygame.draw.rect(self.screen, (0, 255, 0), pygame.Rect(300, 200, 200, 50))  # Play button
        text = self.font.render("Play", True, (255, 255, 255))
        self.screen.blit(text, (350, 210))
        pygame.display.update()

    def draw_game(self, spaceship, asteroids, lasers, score):
        """Draws the game screen with the spaceship, asteroids, and score."""
        self.screen.fill((0, 0, 0))  # Clear screen (black)
        self.screen.blit(pygame.image.load("assets/gamescreen.jpg"), (0, 0))
        spaceship_group = pygame.sprite.Group()
        spaceship_group.add(spaceship)
        spaceship_group.draw(self.screen)
        asteroids_group = pygame.sprite.Group()
        asteroids_group.add(*asteroids)
        asteroids_group.draw(self.screen)
        score_text = self.font.render(f"Score: {score}", True, (255, 255, 255))
        self.screen.blit(score_text, (10, 10))
        pygame.display.update()

    def draw_game_over(self, score, high_score):
        """Draws the game over screen with the score and a try again button."""
        self.screen.fill((0, 0, 0))  # Clear screen (black)
        self.screen.blit(pygame.image.load("assets/gameoverscreen.jpg"), (0, 0))
        text = pygame.font.SysFont("Arial", 48).render(f"Score: {score}", True, (255, 0, 0))
        self.screen.blit(text, (250, 200))
        high_score_text = pygame.font.SysFont("Arial", 36).render(f"High Score: {high_score}", True, (255, 255, 255))
        self.screen.blit(high_score_text, (250, 250))
        pygame.draw.rect(self.screen, (0, 255, 0), pygame.Rect(300, 300, 200, 50))  # Try Again button
        pygame.display.update()
