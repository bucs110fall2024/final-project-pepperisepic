import random
import json
import pygame
from spaceship import Spaceship
from laser import Laser
from asteroid import Asteroid
from view import View


class Controller:
    """
    Controller class responsible for managing game states, handling events,
    and controlling the game data (spaceship, asteroids, lasers, score).
    """
    def __init__(self, screen):
        self.view = View(screen)
        self.game_state = "menu"
        self.score = 0
        self.spaceship = Spaceship(400, 300)  # create spaceship object
        self.lasers = pygame.sprite.Group()  # group to hold lasers
        self.asteroids = pygame.sprite.Group()  # group to hold asteroids
        self.create_asteroids()  # initialize asteroids
        self.high_score = self.load_high_score()  # load the high score from the file

    def create_asteroids(self):
        """ Creates initial asteroids and adds them to the asteroid group. """
        for _ in range(3):  # create 3 asteroids initially
            x = pygame.display.get_surface().get_width()  # edge of screen
            y = random.randint(0, 600)
            asteroid = Asteroid(x, y)
            self.asteroids.add(asteroid)

    def mainloop(self):
        """
        Main loop for handling game events, updating models, and redrawing the screen.
        This handles the game menu, game screen, and game over screen.
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
        Handles events during the menu screen (e.g., play button click).
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
        Handles events during the game screen (e.g., player movement, shooting).
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
            self.view.draw_game_over(self.score, self.high_score)  # pass high_score to display it

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
        self.check_high_score()  # check and save high score if needed

    def check_high_score(self):
        """
        Checks if the current score is higher than the high score, and updates the high score if necessary.
        """
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_high_score()  # save new high score to file

    def save_high_score(self):
        """
        Saves the high score to a JSON file.
        """
        with open("highscores.json", "w") as file:
            json.dump({"high_score": self.high_score}, file)

    def load_high_score(self):
        """
        Loads the high score from a JSON file.
        """
        try:
            with open("highscores.json", "r") as file:
                data = json.load(file)
                return data.get("high_score", 0)
        except FileNotFoundError:
            return 0  # default high score if file doesn't exist

    def is_play_button_clicked(self, pos):
        """
        Checks if the play button is clicked on the menu screen.
        """
        play_button_rect = pygame.Rect(300, 200, 200, 50)  # define play button area
        return play_button_rect.collidepoint(pos)

    def is_try_again_button_clicked(self, pos):
        """
        Checks if the try again button is clicked on the game over screen.
        """
        try_again_button_rect = pygame.Rect(300, 300, 200, 50)  # define try again button area
        return try_again_button_rect.collidepoint(pos)