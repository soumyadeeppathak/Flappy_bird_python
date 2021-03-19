import pygame

class Bird:
    """a class to manage the bird"""

    def __init__(self, fb_game):
        """initialize the bird and set its starting settings"""

        self.screen = fb_game.screen
        self.screen_rect = fb_game.screen.get_rect()
        self.setting = fb_game.setting

        #load bird image and get its rect
        self.image = pygame.image.load('images/dove.bmp')
        self.rect = self.image.get_rect()

        #start the new game with bird at left center
        self.rect.midleft = self.screen_rect.midleft

        #movement flags
        self.moving_up = False
        self.moving_down = True

        #storing the position in decimal format
        self.y = float(self.rect.y)

    def blitme(self):
        """draw the ship at its current loation"""
        self.screen.blit(self.image, self.rect)
    
    def update(self):
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.y -= self.setting.bird_speed 
        elif self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.setting.bird_speed
        
        #update the rect object using the self.y
        self.rect.y = self.y
