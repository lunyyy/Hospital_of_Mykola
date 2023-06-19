from sprites.sprite import Sprite
import paths
import animations

class Npc(Sprite):              
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.DIRECTION = 'L'
        self.ANIM_CHANGE_SPEED = 20
        self.CATCHED = False
        self.BREAK = False
        self.SHOW = True
        
    def move(self):   
        self.X += self.WALK_SPEED
        self.RECT.x += self.WALK_SPEED
        self.walk_animation()
        self.direction()
        
        if self.X <= 15:
            self.DIRECTION = 'L'
            self.WALK_SPEED *= -1

            
        if self.X + self.WIDTH >= 505 and not self.BREAK:
            self.DIRECTION = 'R'
            self.WALK_SPEED *= -1
        
        if self.X + self.WIDTH >= 950 and self.BREAK:
            self.SHOW = False
            
    
    # def catch_player(self, player_rect, function=None):
    #     if self.RECT.colliderect(player_rect) and not self.CATCHED:
    #         self.CATCHED = True
    #         if function:
    #             function()
                
                
    def catch_player(self, player):
        if self.RECT.colliderect(player.RECT):
            player.RECT.x = 350
            player.X = 350
            player.RECT.y = 70
            player.Y = 70
            player.LIVES = int(player.LIVES) - 1
            player.LIVES = str(player.LIVES)



first_psycho = Npc(x=790,
                y=338,
                width=90,
                height=150,
                image_path=paths.girl1_path)


second_psycho = Npc(x=1035,
                y=60,
                width=80,
                height=170,
                image_path=paths.girl2_path)

third_psycho = Npc(x=785,
                y=60,
                width=80,
                height=170,
                image_path=paths.homeless_path)

guard = Npc(x=100,
            y=600,
            width=80,
            height=170,
            image_path=paths.guard3_path,
            animations=animations.guard,
            speed=2)

cleaner = Npc(x=500,
            y=338,
            width=95,
            height=170,
            image_path=paths.cleaner1_path,
            animations=animations.cleaner,
            speed=1)
