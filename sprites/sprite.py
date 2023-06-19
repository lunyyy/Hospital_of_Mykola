import pygame as pg

class Sprite:
    def __init__(self, x, y,
                 width=None, height=None,
                 color=None,
                 image_path=None,
                 animations=None,
                 speed=4
                 ):
        self.X = x
        self.Y = y
        self.WIDTH = width
        self.HEIGHT = height
        self.COLOR = color
        self.IMAGE_PATH = image_path
        self.IMAGE = None
        self.CLICKED = False
        self.BLITING = True
        self.SHOW_BUTTON = True
        self.SHOW_ITEMS_IN_HERO_ROOM = False
        if self.WIDTH and self.HEIGHT:
            self.RECT = pg.Rect(self.X, self.Y, self.WIDTH, self.HEIGHT)
        self.MEAT_TAKEN = False
        self.ROPE_TAKEN = False
        self.KEY_FROM_BASEMENT_TAKEN = False
        self.KEY_FROM_ESCAPE_TAKEN = False
        self.SCISSORS_TAKEN = False
        self.SHOVEL_TAKEN = False
        
        # Animations
        self.WALK_SPEED = speed
        self.ANIMATIONS = animations
        self.CUR_WALK_SPRITE = 0
        self.WALK_ANIM_COUNT = 0
        self.DIRECTION = 'R'
        self.ANIM_CHANGE_SPEED = 12
        
        if self.IMAGE_PATH:
            self.load_image()
    
    def load_image(self):
        self.IMAGE = pg.image.load(self.IMAGE_PATH)
        self.IMAGE = pg.transform.scale(self.IMAGE, (self.WIDTH, self.HEIGHT))

    def draw_rect(self,win):
        pg.draw.rect(win, (255,0,0), self.RECT)

    def show_image(self, win):
        if self.BLITING:
            win.blit(self.IMAGE, (self.X, self.Y))
    
    def walk_animation(self):
        self.WALK_ANIM_COUNT += 1

        if self.WALK_ANIM_COUNT % self.ANIM_CHANGE_SPEED == 0:
            self.CUR_WALK_SPRITE += 1

        if self.CUR_WALK_SPRITE == len(self.ANIMATIONS['RUN']):
            self.CUR_WALK_SPRITE = 0

        self.IMAGE = self.ANIMATIONS['RUN'][self.CUR_WALK_SPRITE]
        self.IMAGE = pg.transform.scale(self.IMAGE, (self.WIDTH, self.HEIGHT))

    def direction(self):
        if self.DIRECTION == 'L':
            self.IMAGE = pg.transform.flip(self.IMAGE, False, False)
        if self.DIRECTION == 'R':
            self.IMAGE = pg.transform.flip(self.IMAGE, True, False)


    def change_color(self):
        mouse_pos = pg.mouse.get_pos()
        if self.RECT.collidepoint(mouse_pos):
            if pg.mouse.get_pressed()[0] == 1:
                self.CLICKED = True
                self.COLOR = (0,255,0)
                self.SHOW_BUTTON = False
                self.SHOW_ITEMS_IN_HERO_ROOM = True
                
        if pg.mouse.get_pressed()[0] == 0:
            self.CLICKED = False

    def on_click(self):
        mouse_pos = pg.mouse.get_pos()
        if self.RECT.collidepoint(mouse_pos):
            if pg.mouse.get_pressed()[0] == 1:
                self.CLICKED = True
                self.BLITING = False
                self.MEAT_TAKEN = True
                self.ROPE_TAKEN = True
                self.KEY_FROM_BASEMENT_TAKEN = True
                self.KEY_FROM_ESCAPE_TAKEN = True
                self.SCISSORS_TAKEN = True
                self.SHOVEL_TAKEN = True
                
        if pg.mouse.get_pressed()[0] == 0:
            self.CLICKED = False
            
    def collideplayer(self,player):
        pass
            
