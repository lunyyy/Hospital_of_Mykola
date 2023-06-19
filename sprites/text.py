from sprites.sprite import Sprite
import pygame


class Text(Sprite):
    def __init__(self, text, **kwargs):
        super().__init__(**kwargs)
        self.TEXT = text
        self.FONT = pygame.font.SysFont("Ariel", 30)
        self.render_text()
        # self.blit_text()
        
    def render_text(self):
        self.TEXT = self.FONT.render(self.TEXT, False, (0, 0, 0))
        
    def blit_text(self, win):
        win.blit(self.TEXT, (self.X,self.Y))