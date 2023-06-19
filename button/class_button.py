import pygame as pg
import window.settings as window_settings

class Button:
    def __init__(self, x, y, width, height, image_path=None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = None
        self.clicked = False
        
        if image_path:
            self.image = pg.image.load(image_path)
            self.image = pg.transform.scale(self.image, (self.width, self.height))
        self.rect = pg.Rect(self.x, self.y, self.width, self.height)
        
    def show(self, win):
        win.blit(self.image, (self.rect.x, self.rect.y))
        

    def action(self, function):
        mouse_pos = pg.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            if pg.mouse.get_pressed()[0] == 1:
                if not self.clicked:
                    self.clicked = True
                    function()
    
        if pg.mouse.get_pressed()[0] == 0:
            self.clicked = False