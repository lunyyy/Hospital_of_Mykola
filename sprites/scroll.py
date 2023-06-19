from sprites.sprite import Sprite
import pygame as pg
pg.init()



class Scroll(Sprite):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.SHOW_FULL_SCROLL = False
        self.SHOW_SMALL_SCROLL = True
        
    def scroll_clicked(self):
        mouse_pos = pg.mouse.get_pos()
        if self.RECT.collidepoint(mouse_pos):
            if pg.mouse.get_pressed()[0] == 1:
                if not self.CLICKED:
                    self.CLICKED = True
                    self.SHOW_FULL_SCROLL = True

        if pg.mouse.get_pressed()[0] == 0:
            self.CLICKED = False