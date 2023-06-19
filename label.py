from sprites.sprite import Sprite
from paths import font_path
import pygame as pg


class Label(Sprite):
    def __init__(self, font_name, font_size, **kwargs):
        super().__init__(**kwargs)
        
        self.FONT = pg.font.Font(font_path+font_name, font_size)
        self.LABEL = self.FONT.render("Всего крышек: ", 1, "white")
    def change_text(self, caps_count):
        self.LABEL = self.FONT.render(f"Всего крышек: {caps_count}", 1, "white")
    
    def blit(self, win):
        
        win.blit(self.LABEL, (self.X, self.Y))
    
    def change_text_help(self):
        self.LABEL = self.FONT.render("Hi bro",1, "black")

        
            
caps_label = Label(x=30, y=30, font_name="Arial.ttf", font_size=25)
caps_text_help = Label(x=310, y=260, font_name="Arial.ttf", font_size=25)