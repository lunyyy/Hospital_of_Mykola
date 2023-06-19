from sprites.sprite import Sprite
import pygame as pg
import window.settings

class Room(Sprite):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.CAN_SHOW = False
        self.IMAGE = pg.image.load(self.IMAGE_PATH)
        self.IMAGE = pg.transform.scale(self.IMAGE, (1200, 800))

    def click_on_room(self, player_rect, fire_exit=False):
        if self.RECT.collidepoint(player_rect.RECT.x + player_rect.RECT.w // 2, player_rect.RECT.y):
            mouse_pos = pg.mouse.get_pos()
            if self.RECT.collidepoint(mouse_pos):
                if pg.mouse.get_pressed()[0] == 1:
                    if not self.CAN_SHOW:
                        self.CLICKED = True
                        self.CAN_SHOW = True
                        if fire_exit:
                            player_rect.X, player_rect.RECT.x = (1100, 1100)
                            player_rect.Y, player_rect.RECT.y = (420, 420)
                        
        if pg.mouse.get_pressed()[0] == 0:
            self.CLICKED = False
                        

                    
    def wait_exit(self, player, fire_exit=False):
        if pg.key.get_pressed()[pg.K_ESCAPE] == 1 and not fire_exit:
            self.CAN_SHOW = False
            window.settings.blit_level_1 = True
            # player.RECT.x = self.X + 5
            # player.X = player.RECT.x

            

    def show(self, win):
        win.blit(self.IMAGE, (0, 0))
        

        