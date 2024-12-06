import pygame
from spaceship import Spaceship
from laser import Laser
from asteroid import Asteroid
from view import View

class Controller:
    """
    controller class responsible for managing game states, handling events,
    and controlling the game data (spaceship, asteroids, lasers, score).
    """
    def __init__(self, view):
        """
        initializes the Controller with the provided view object.

        args:
            view (View): the View object responsible for displaying the game.
        """
        self.view = view
        self.game_state = "menu" 
        self.score = 0
        self.spaceship = Spaceship()  # create spaceship object
        self.lasers = pygame.sprite.Group()  # group to hold lasers
        self.asteroids = pygame.sprite.Group()  # group to hold asteroids
        self.create_asteroids()  # initialize asteroids
    
    def create_asteroids(self):
        """ Creates initial asteroids and adds them to the asteroid group. """
        for _ in range(3):  # create 3 asteroids initially
            asteroid = Asteroid()
            self.asteroids.add(asteroid)
    
    def mainloop(self):
        """
        main loop for handling game events, updating models, and redrawing the screen.
        this handles the game menu, game screen, and game over screen.
        """
        running = True
        while running:
            if self.game_state == "menu":
                self.handle_menu_events()
            elif self.game_state == "game":
                self.handle_game_events()
            elif self.game_state == "game_over":
                self.handle_game_over_events()

            # update models (spaceship, lasers, asteroids)
            self.update_models()

            # detect collisions
            self.detect_collisions()

            # redraw the screen based on the current state
            self.update_view()

            # update display
            pygame.display.flip()

    def handle_menu_events(self):
        """
        handles events during the menu screen (e.g., play button click).
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.is_play_button_clicked(event.pos):
                    self.start_game()

    def handle_game_events(self):
        """
        handles events during the game screen (e.g., player movement, shooting).
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    self.spaceship.move_left()
                elif event.key == pygame.K_d:
                    self.spaceship.move_right()
                elif event.key == pygame.K_SPACE:
                    laser = self.spaceship.shoot()
                    self.lasers.add(laser)

    def handle_game_over_events(self):
        """
        Handles events during the game over screen (e.g., try again button click).
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.is_try_again_button_clicked(event.pos):
                    self.reset_game()

    def update_models(self):
        """
        Updates the positions and states of all game models (spaceship, lasers, asteroids).
        """
        self.spaceship.update()
        for laser in self.lasers:
            laser.update()
        for asteroid in self.asteroids:
            asteroid.update()

    def detect_collisions(self):
        """
        Detects and handles collisions between lasers, asteroids, and the spaceship.
        """
        # laser colliding with asteroid
        for laser in self.lasers:
            if pygame.sprite.spritecollide(laser, self.asteroids, True):  # laser hits asteroid
                self.score += 1  # increase score
                laser.kill()  # remove laser after collision

        # spaceship colliding with asteroid
        if pygame.sprite.spritecollide(self.spaceship, self.asteroids, False):  # spaceship hits asteroid
            self.game_over()

    def update_view(self):
        """
        Updates the view based on the current game state (menu, game, game over).
        """
        if self.game_state == "menu":
            self.view.draw_menu()
        elif self.game_state == "game":
            self.view.draw_game(self.spaceship, self.asteroids, self.lasers, self.score)
        elif self.game_state == "game_over":
            self.view.draw_game_over(self.score)

    def start_game(self):
        """
        Starts the game by transitioning to the game state and resetting the score.
        """
        self.game_state = "game"
        self.score = 0
        self.lasers.empty()
        self.create_asteroids()  # create new asteroids

    def reset_game(self):
        """
        Resets the game when the "Try Again" button is clicked.
        """
        self.game_state = "game"
        self.score = 0
        self.lasers.empty()
        self.create_asteroids()

    def game_over(self):
        """
        Ends the game when the spaceship collides with an asteroid.
        Transitions to the game over state.
        """
        self.game_state = "game_over"

    def is_play_button_clicked(self, pos):
        """
        Checks if the play button is clicked on the menu screen.

        args:
            pos (tuple): The mouse position (x, y).

        return: bool: True if the play button was clicked, False otherwise.
        """
        play_button_rect = pygame.Rect(300, 200, 200, 50)  # define play button area
        return play_button_rect.collidepoint(pos)

    def is_try_again_button_clicked(self, pos):
        """
        Checks if the try again button is clicked on the game over screen.

        args:
        pos (tuple): The mouse position (x, y).

        return: bool: True if the try again button was clicked, False otherwise.
        """
        try_again_button_rect = pygame.Rect(300, 300, 200, 50)  # define try again button area
        return try_again_button_rect.collidepoint(pos)