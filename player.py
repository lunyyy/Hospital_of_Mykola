from sprites.sprite import Sprite
import pygame as pg
import paths
import animations
import time
import window.settings as window_settings

class Player(Sprite):
    def __init__(self, speed, **kwargs):
        super().__init__(**kwargs)
        self.DIRECTION = 'R'
        self.CAPS = 0
        self.IN_FIRE_EXIT = False

        self.CAN_CLICK = True

        self.DIG_ANIM_COUNT = 0
        self.DIG_ANIM_CHANGE_SPEED = 25
        self.CUR_DIG_SPRITE = 0
        self.IS_DIGING = False
        self.DIRECTION = 'L'
        
        self.TIME = 0

        # self.START_DIG = False

        self.IS_TIME_GET = False
        self.PRESSED_E = False

        self.LIVES = "3"
        self.FONT = pg.font.SysFont('Ariel', 100)

    def inner_move(self, condition_left, condition_right):
        keys = pg.key.get_pressed()

        if keys[pg.K_a] and condition_left:
            self.DIRECTION = 'R'
            self.X -= self.WALK_SPEED
            self.RECT.x -= self.WALK_SPEED
            self.walk_animation()
            self.direction()
    
        if keys[pg.K_d] and condition_right:
            self.DIRECTION = 'L'
            self.X += self.WALK_SPEED
            self.RECT.x += self.WALK_SPEED
            self.walk_animation()
            self.direction()

        if (not keys[pg.K_a] and not keys[pg.K_d]) or all( (keys[pg.K_a], keys[pg.K_d]) ):
            self.stand_animation()

    def move(self):
        if not self.IN_FIRE_EXIT:
            self.inner_move(condition_left=self.X >= 15,
                            condition_right=self.X + self.WIDTH <= 1185)
            # self.dig_animation()
        if self.IN_FIRE_EXIT:
            self.inner_move(condition_left=self.RECT.x > 450 and self.X > 450,
                            condition_right=False)
            self.dig_animation()
            
          
    def stand_animation(self):
        self.IMAGE = self.ANIMATIONS['STAND'][1]
        self.IMAGE = pg.transform.scale(self.IMAGE, (self.WIDTH, self.HEIGHT))
        self.direction()
    
    def dig_animation(self):
        keys = pg.key.get_pressed()
        
        if not self.IS_TIME_GET and keys[pg.K_t] and self.X <= 450:
            self.TIME = time.time()
            self.IS_TIME_GET = True

        if keys[pg.K_t] and self.X <= 450:
            if time.time() > self.TIME + 3:
                window_settings.blit_level_3 = False
                window_settings.can_show_comics2 = True
        else:
            self.IS_TIME_GET = False

        if keys[pg.K_t] and self.X <= 450:
            self.DIG_ANIM_COUNT += 1

            if self.DIG_ANIM_COUNT % self.DIG_ANIM_CHANGE_SPEED == 0:
                self.CUR_DIG_SPRITE += 1

            if self.CUR_DIG_SPRITE == len(self.ANIMATIONS['DIG']):
                self.CUR_DIG_SPRITE = 0

            self.IMAGE = self.ANIMATIONS['DIG'][self.CUR_DIG_SPRITE]
            self.IMAGE = pg.transform.scale(self.IMAGE, (self.WIDTH, self.HEIGHT))
            # else:
                # window_settings.can_show_comics2 = True
    
    def blit_lives(self, win):
        win.blit(self.TEXT_LIVES, (0,0))
        
    def render_text(self):
        self.TEXT_LIVES = self.FONT.render(self.LIVES, True, (255, 0, 0))
    

player = Player(speed=5,
                x=490,
                y=70,
                width=80,
                height=170,
                color=((0,0,0)),
                image_path=paths.idle1_path,
                animations=animations.player)