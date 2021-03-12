import sys

import pygame

from settings import Settings

class FlappyBird:
    """overall class to manage the game and its mechanics"""
    
    def __init__(self):
        """initializes the game and creates its resources"""
        pygame.init()

        self.setting = Settings()

        self.screen = pygame.display.set_mode((self.setting.screen_width,self.setting.screen_height ))
        pygame.display.set_caption("Flappy Bird")


    def run_game(self):
        """start the main loop of the game"""
        while True:
            #watch for keybord and mouse movements
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            #redraw the screen through each run of the loop
            self.screen.fill(self.setting.bg_color)
            #make the most recently drawn screen visible
            pygame.display.flip()

if __name__ == '__main__':
    #make a game instance and run the game
    fb = FlappyBird()
    fb.run_game()