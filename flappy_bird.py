import sys

import pygame
from pygame.constants import K_DOWN, K_UP, K_q

from settings import Settings

from bird import Bird


class FlappyBird:
    """overall class to manage the game and its mechanics"""

    def __init__(self):
        """initializes the game and creates its resources"""
        pygame.init()

        self.setting = Settings()

        self.screen = pygame.display.set_mode(
            (0,0) , pygame.FULLSCREEN)
        self.setting.screen_width = self.screen.get_rect().width
        self.setting.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Flappy Bird")

        self.bird = Bird(self)

    def run_game(self):
        """start the main loop of the game"""
        while True:
            self._check_events()
            self.bird.update()
            self._update_screen()

    def _check_events(self):
        # watch for keybord and mouse movements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self. _check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self. _check_keyup_events(event)

    def _check_keydown_events(self, event):
        if event.key == K_UP:
            self.bird.moving_up = True
        elif event.key == K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        if event.key == K_UP:
            self.bird.moving_up = False

    def _update_screen(self):
        # redraw the screen through each run of the loop
        self.screen.fill(self.setting.bg_color)
        self.bird.blitme()
        # make the most recently drawn screen visible
        pygame.display.flip()


if __name__ == '__main__':
    # make a game instance and run the game
    fb = FlappyBird()
    fb.run_game()
