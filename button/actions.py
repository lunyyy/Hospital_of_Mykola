import pygame as pg
import button.buttons as buttons
import window.settings as window_settings
from player import player
from button.buttons import three,two,one
from sprites.objects import (
    scroll,
    canteen,
    dialog1,
    dialog2,
    dialog2_1,
    dialog3,
    dialog3_1,
    dialog4,
    shovel,
    rope,
    key_from_basement,
    key_from_escape,
    scissors,
    meat
)
from sys import exit as sys_exit
from tasks import task1



def play_game():
    global task1
    window_settings.show_menu = False
    # window_settings.blit_level_1 = True
    window_settings.can_show_comics1 = True
    player.LIVES = "3"
    task1 = True


    

def continue_game():
    pass

def help_game():
    window_settings.show_button_menu = False
    window_settings.show_menu = False  
    

def authors_game():

    window_settings.show_menu = False

def exit_game():
    pg.quit()
    sys_exit()

def up_stairs():
    if pg.mouse.get_pressed()[0] == 1:
        player.X = 605
        player.Y = 200

def down_stairs():
    if pg.mouse.get_pressed()[0] == 1:
        player.X = 605
        player.Y = 430


#
def down_stairs():
    if three.rect.collidepoint(player.RECT.center):
        if pg.mouse.get_pressed()[0] == 1:
            player.RECT.x = 600
            player.RECT.y = 330
            player.X = player.RECT.x 
            player.Y = player.RECT.y
                       
def down2_stairs():
    if two.rect.collidepoint(player.RECT.center):
        if pg.mouse.get_pressed()[0] == 1:
            player.RECT.x = 600
            player.RECT.y = 600
            player.X = player.RECT.x 
            player.Y = player.RECT.y

def down3_stairs():
    if three.rect.collidepoint(player.RECT.center):
        if pg.mouse.get_pressed()[0] == 1:
            player.RECT.x = 600
            player.RECT.y = 330
            player.X = player.RECT.x 
            player.Y = player.RECT.y
        
def up_stairs():
    if two.rect.collidepoint(player.RECT.center):
        if pg.mouse.get_pressed()[0] == 1:
            player.RECT.x = 600
            player.RECT.y = 60
            player.X = player.RECT.x 
            player.Y = player.RECT.y
        
def up2_stairs():
    if one.rect.collidepoint(player.RECT.center):
        if pg.mouse.get_pressed()[0] == 1:
            player.RECT.x = 600
            player.RECT.y = 330
            player.X = player.RECT.x 
            player.Y = player.RECT.y

def up3_stairs():
    if one.rect.collidepoint(player.RECT.center):
        if pg.mouse.get_pressed()[0] == 1:
            player.RECT.x = 600
            player.RECT.y = 330
            player.X = player.RECT.x 
            player.Y = player.RECT.y
# def dig_fire_exit():
    # if dig.rect.collidepoint(player.RECT.center):
        # if pg.mouse.get_pressed()[0] == 1:            
            # pass

def exit_from_scroll_lvl1():
   window_settings.blit_level_1 = False
   window_settings.blit_level_2 = False
   window_settings.blit_level_3 = False
   window_settings.show_menu = True
   scroll.SHOW_FULL_SCROLL = False

def exit_from_button_help_func():
    window_settings.show_menu = True           

def exit_from_full_scroll_func():
    scroll.SHOW_FULL_SCROLL = False
    
def exit_from_kitchen_func():
    window_settings.blit_level_1 = True
    canteen.CAN_SHOW = False
    