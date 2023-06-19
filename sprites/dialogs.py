from sprites.room import Room
import pygame as pg
import window.settings
from window.screen import win
from sprites.phrases_bum1 import mc_bum_phrases, bum_1_phrases, mc_sym, bum_sym

class Dialogs(Room):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.IMAGE = pg.transform.scale(self.IMAGE, (1200, 300))
        # self.CLOSE_DIALOG = False
        self.COUNTER_DIALOGS = 0
        self.SYS_ALERT = False
        
    def click_on_npc(self, player_rect, player_stand=None):
        if self.RECT.collidepoint(player_rect.x + player_rect.w // 2, player_rect.y):
            mouse_pos = pg.mouse.get_pos()
            if self.RECT.collidepoint(mouse_pos):
                if pg.mouse.get_pressed()[0] == 1:
                    if not self.CAN_SHOW:
                        self.CAN_SHOW = True
                        self.CLICKED = True
                        if player_stand:
                            player_stand.stand_animation()
        
        if pg.mouse.get_pressed()[0] == 0:
            self.CLICKED = False
            
    def sys_alert(self, player_rect):
        if self.RECT.collidepoint(player_rect.x + player_rect.w // 2, player_rect.y):
            mouse_pos = pg.mouse.get_pos()
            if self.RECT.collidepoint(mouse_pos):
                if pg.mouse.get_pressed()[0] == 1:
                    if not self.CAN_SHOW:
                        self.CLICKED = True
                        self.SYS_ALERT = True
                        
                            
        if pg.mouse.get_pressed()[0] == 0:
            self.CLICKED = False
        
    def wait_exit(self, player):
        if pg.key.get_pressed()[pg.K_ESCAPE] == 1:
            self.CAN_SHOW = False
            window.settings.blit_level_1 = True
            
    def show(self, win):
        win.blit(self.IMAGE, (0, 215))
    