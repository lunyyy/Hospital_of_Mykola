import pygame as pg
pg.init()
import time

import os

# Импорт модулей
from menu.background import bg
from button.buttons import (
    play,
    helpp,
    exitt,
    down,
    down2,
    down3,
    up,
    up2,
    up3,
    three,
    two,
    one
)
# buttons, actions

from paths.comics import the_end, robbery

from button.actions import(
    play_game,
    continue_game,
    help_game,
    authors_game,
    exit_game,
    up_stairs,
    down_stairs,
    down2_stairs,
    down3_stairs,
    up_stairs,
    up2_stairs,
    up3_stairs
)

from tasks import (
    task1, 
    task2, 
    task2_1, 
    task3, 
    task3_1,
    task4,
    can_use_ladder,
    can_use_canteen,
    can_use_basement,
    show_basement_full,
    wires_cut,
    can_see_bum,
    can_go_outside
    # can_show_comics1
)

from levels.level_1 import bg_hospital, bg_dark
from window.screen import win
import window.settings as window_settings
from menu.background import help_bg
from player import player
from sprites.room import Room
import screen
# from button.buttons import dig
from nps import first_psycho, second_psycho, third_psycho, guard

from paths.get_path import get_full_path

from sprites.objects import (

    canteen,
    fire_exit,
    meat,
    storeroom,
    basement,
    key_from_basement,
    key_from_escape,
    rope,
    scissors,
    object1,
    object2,
    object3,
    object4,
    shovel,
    shield,
    block1,
    block2,
    block3,
    block4,
    block5,
    block6,
    dig,
    dialog1,
    dialog2,
    dialog2_1,
    dialog3,
    dialog3_1,
    dialog4,
    exclamation_mark1,
    exclamation_mark2,
    exclamation_mark3,
    arrow_down2,
    arrow_down3,
    basement_cut
)

from label import caps_label,caps_text_help



from sprites.phrases_bum1 import (mc_bum_phrases, bum_1_phrases, mc_sym, bum_sym, sys_press_e,
                             sys_press_r,
                             sys_exit_e,
                             sys_exit_esc,
                             sys_take_all_form_storeroom,
                             sys_take_meat,
                             sys_g,
                             sys_h,
                             sys_j,
                             sys_y,
                             sys_press_c,
                             sys_press_x,
                             sys_exit_esc_b,
                             sys_dig_t)

from sprites.phrases_meat import (
    mcp, mp, meat_sym, mcp2, meatp1_2
)

from sprites.phrases_spy import (
    mcps,
    spy_sym,
    sp,
    spl2,
    mcl2
)

from sprites.phrases_bum2 import (
    buml,
    mcpl
)



def run_game():
    pg.mixer.music.load(get_full_path(path="resources/sounds/bg_music.wav"))
    pg.mixer.music.set_volume(0.1)
    pg.mixer.music.play(loops=-1, fade_ms=1000)

    running = True
    while running:
        global task1
        global task2
        global task3
        global task2_1
        global task3_1
        global task4
        global can_use_ladder
        global can_use_canteen
        global can_use_basement
        global show_basement_full
        global wires_cut
        global can_see_bum
        global can_go_outside
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        if window_settings.show_menu:
            # Отображение фона меню
            screen.win.blit(bg, (0, 0))

            play.show(win=win)
            exitt.show(win=win)

            # Действие кнопок по нажатию
            play.action(function=play_game)
            exitt.action(function=exit_game)
            task1 = True
            task2 = False
            task2_1 = False
            task3 = False
            task3_1 = False
            task4 = False
            
            can_use_ladder = False
            can_use_canteen = False
            can_use_basement = False
            can_go_outside = False

            show_basement_full = True

            wires_cut = False

            can_see_bum = True
            
            shovel.SHOVEL_TAKEN = False
            scissors.SCISSORS_TAKEN = False
            rope.ROPE_TAKEN = False
            meat.MEAT_TAKEN = False
            key_from_basement.KEY_FROM_BASEMENT_TAKEN = False
            key_from_escape.KEY_FROM_ESCAPE_TAKEN = False
            
            dialog1.COUNTER_DIALOGS = 0
            dialog2.COUNTER_DIALOGS = 0
            dialog2_1.COUNTER_DIALOGS = 0
            dialog3.COUNTER_DIALOGS = 0
            dialog3_1.COUNTER_DIALOGS = 0
            dialog4.COUNTER_DIALOGS = 0
            
            basement_cut.CAN_SHOW = False
            
            dialog2_1.SYS_ALERT = False
            dialog3_1.SYS_ALERT = False
            
            guard.BREAK = False
            guard.SHOW = True

            guard.X, guard.RECT.x = 100, 100
            guard.Y, guard.RECT.y = 600, 600
            
            shovel.BLITING = True
            scissors.BLITING = True
            rope.BLITING = True
            meat.BLITING = True
            key_from_basement.BLITING = True
            key_from_escape.BLITING = True
            
            object1.BLITING = True
            object2.BLITING = True
            object3.BLITING = True
            object4.BLITING = True
            shield.BLITING = True
            
            
            player.DIRECTION = 'R'
            player.CAPS = 0
            player.IN_FIRE_EXIT = False

            player.CAN_CLICK = True

            player.DIG_ANIM_COUNT = 0
            player.DIG_ANIM_CHANGE_SPEED = 25
            player.CUR_DIG_SPRITE = 0
            player.IS_DIGING = False
            player.DIRECTION = 'L'
            
            player.RECT.x = 350
            player.X = 350
            player.RECT.y = 70
            player.Y = 70

            player.TIME = 0

            player.IS_TIME_GET = False
            player.PRESSED_E = False
            # window_settings.can_show_comics1 = True
            window_settings.blit_level_3 = False
            # window_settings.blit_level_1 = False
            window_settings.blit_level_2 = False
            fire_exit.CAN_SHOW = False

                
            
        
                                                                                                                                                                                                                                                                                                                                                                                                                                                        
        if not window_settings.show_menu and not window_settings.can_show_comics1:
            if window_settings.blit_level_1:
                if not wires_cut and not basement.CAN_SHOW:
                    win.blit(bg_hospital,(0,0))
                elif wires_cut and not basement.CAN_SHOW:
                    win.blit(bg_dark, (0,0))

                if int(player.LIVES) == 0:
                    window_settings.show_menu = True
                    window_settings.blit_level_1 = False
                    window_settings.blit_level_2 = False
                    window_settings.blit_level_3 = False
                if not wires_cut:
                    first_psycho.show_image(win=win)
                if not wires_cut:
                    second_psycho.show_image(win=win)
                if can_see_bum:
                    third_psycho.show_image(win=win)
                    
                if guard.SHOW:
                    guard.show_image(win=win)
                    guard.move()
                    guard.catch_player(player=player)
                
                player.render_text()
                player.blit_lives(win=win)
                if not wires_cut:
                    down.show(win=bg_hospital)
                    down2.show(win=bg_hospital)
                    down3.show(win=bg_hospital)
                    up.show(win=bg_hospital)
                    up2.show(win=bg_hospital)
                    up3.show(win=bg_hospital)
                
                if can_use_ladder and not wires_cut:
                    down.action(function=down_stairs)
                    down2.action(function=down2_stairs)
                    down3.action(function=down3_stairs)
                    up.action(function=up_stairs)
                    up2.action(function=up2_stairs)
                    up3.action(function=up3_stairs)        
                
                if not meat.MEAT_TAKEN:
                    canteen.click_on_room(player_rect=player)
                    
                if can_use_basement and not wires_cut:
                    basement.click_on_room(player_rect=player)

                if can_go_outside:
                    fire_exit.click_on_room(player_rect=player, fire_exit=True)
                
                if task3_1:
                    if not rope.ROPE_TAKEN or not shovel.SHOVEL_TAKEN or not scissors.SCISSORS_TAKEN or not key_from_basement.KEY_FROM_BASEMENT_TAKEN or not key_from_escape.KEY_FROM_ESCAPE_TAKEN:
                        storeroom.click_on_room(player_rect=player)

            if canteen.CAN_SHOW:
                window_settings.blit_level_1 = False
                canteen.show(win=win)
                sys_exit_esc.blit_text(win=win)
                canteen.wait_exit(player)
                meat.show_image(win=win)
                meat.on_click()
            

            if fire_exit.CAN_SHOW:
                player.IN_FIRE_EXIT = True
                window_settings.blit_level_1 = False
                window_settings.blit_level_3 = True
                fire_exit.show(win=win)
                sys_dig_t.blit_text(win=win)
                fire_exit.wait_exit(player=player, fire_exit=True)
                    
            
            if basement.CAN_SHOW:
                window_settings.blit_level_1 = False
                window_settings.blit_level_2 = True

                if show_basement_full:
                    basement.show(win=win)
                 
                if object1.BLITING or object2.BLITING or object3.BLITING or object4.BLITING:
                    shield.show_image(win=win)
                        
                if object1.BLITING:
                    object1.show_image(win=win)
                    sys_y.blit_text(win=win)
                    if pg.key.get_pressed()[pg.K_y] == 1:
                        object1.BLITING = False

                if object2.BLITING:
                    object2.show_image(win=win)
                    sys_g.blit_text(win=win)
                    if pg.key.get_pressed()[pg.K_g] == 1:
                        object2.BLITING = False

                if object3.BLITING:
                    object3.show_image(win=win)
                    sys_h.blit_text(win=win)
                    if pg.key.get_pressed()[pg.K_h] == 1:
                        object3.BLITING = False

                if object4.BLITING:
                    object4.show_image(win=win)
                    sys_j.blit_text(win=win)
                    if pg.key.get_pressed()[pg.K_j] == 1:
                        object4.BLITING = False
                    
                if not object1.BLITING and not object2.BLITING and not object3.BLITING and not object4.BLITING:
                    if not wires_cut:
                        sys_press_x.blit_text(win=win)
                    if pg.key.get_pressed()[pg.K_x] == 1:
                        show_basement_full = False
                        basement_cut.show(win=win)
                        sys_exit_esc_b.blit_text(win=win)
                        basement_cut.CAN_SHOW = True
                        wires_cut = True
                            
                if basement_cut.CAN_SHOW:
                    basement.wait_exit(player=player)
                    can_go_outside = True
                    

            if storeroom.CAN_SHOW:
                window_settings.blit_level_1 = False
                # scroll.SHOW_SMALL_SCROLL = False
                # scroll.SHOW_FULL_SCROLL = False
                storeroom.show(win=win)
                storeroom.wait_exit(player=player)
                sys_exit_esc.blit_text(win=win)
                if scissors.BLITING:
                    scissors.show_image(win=win)
                    scissors.on_click()
                if rope.BLITING:
                    rope.show_image(win=win)
                    rope.on_click()
                if key_from_basement.BLITING:
                    key_from_basement.show_image(win=win)
                    key_from_basement.on_click()
                if key_from_escape.BLITING:
                    key_from_escape.show_image(win=win)
                    key_from_escape.on_click()
                if shovel.BLITING:
                    shovel.show_image(win=win)
                    shovel.on_click()
            # if not window_settings.show_button_menu:
            #     win.blit(bg, (0, 0))
            #     win.blit(help_bg,(0,0))
            #     caps_text_help.blit(win=win)
            #     caps_text_help.change_text_help()
            #     if pg.key.get_pressed()[pg.K_ESCAPE] == 1:
            #         window_settings.show_menu = True
            #         window_settings.show_button_menu = True
              
            #   or window_settings.blit_level_2
        if window_settings.blit_level_1 or window_settings.blit_level_3:
            player.show_image(win=win)
            if not dialog1.CAN_SHOW and not dialog2.CAN_SHOW and not dialog2_1.CAN_SHOW and not dialog3.CAN_SHOW and not dialog3_1.CAN_SHOW and not dialog4.CAN_SHOW:
                player.move()
                    
            if task1:
                exclamation_mark1.show_image(win=win)
                dialog1.click_on_npc(player_rect=player.RECT, player_stand=player)
            if dialog1.CAN_SHOW:
                # player.stand_animation()
                window_settings.blit_level_1 = True
                dialog1.show(win=win)
                if dialog1.COUNTER_DIALOGS == 0:
                    mc_sym.blit_text(win=win)
                    mc_bum_phrases[0].blit_text(win=win)
                    sys_press_e.blit_text(win=win)
                    if pg.key.get_pressed()[pg.K_e] == 1:
                        dialog1.COUNTER_DIALOGS += 1
                if dialog1.COUNTER_DIALOGS == 1:
                    bum_sym.blit_text(win=win)
                    sys_press_r.blit_text(win=win)
                    bum_1_phrases[0].blit_text(win=win)
                    if pg.key.get_pressed()[pg.K_r] == 1:
                        dialog1.COUNTER_DIALOGS += 1
                if dialog1.COUNTER_DIALOGS == 2:
                    mc_sym.blit_text(win=win)
                    sys_press_e.blit_text(win=win)
                    mc_bum_phrases[1].blit_text(win=win)
                    if pg.key.get_pressed()[pg.K_e] == 1:
                        dialog1.COUNTER_DIALOGS += 1
                if dialog1.COUNTER_DIALOGS == 3:
                    bum_sym.blit_text(win=win)
                    bum_1_phrases[1].blit_text(win=win)
                    sys_press_r.blit_text(win=win)
                    if pg.key.get_pressed()[pg.K_r] == 1:
                        dialog1.COUNTER_DIALOGS += 1
                if dialog1.COUNTER_DIALOGS == 4:
                    mc_sym.blit_text(win=win)
                    mc_bum_phrases[2].blit_text(win=win)
                    sys_press_e.blit_text(win=win)
                    if pg.key.get_pressed()[pg.K_e] == 1:
                        dialog1.COUNTER_DIALOGS += 1
                if dialog1.COUNTER_DIALOGS == 5:
                    bum_sym.blit_text(win=win)
                    bum_1_phrases[2].blit_text(win=win)
                    sys_press_r.blit_text(win=win)
                    if pg.key.get_pressed()[pg.K_r] == 1:
                        dialog1.COUNTER_DIALOGS += 1
                if dialog1.COUNTER_DIALOGS == 6:
                    bum_sym.blit_text(win=win)
                    bum_1_phrases[3].blit_text(win=win)
                    sys_press_e.blit_text(win=win)
                    if pg.key.get_pressed()[pg.K_e] == 1:
                        dialog1.COUNTER_DIALOGS += 1
                if dialog1.COUNTER_DIALOGS == 7:
                    bum_sym.blit_text(win=win)
                    bum_1_phrases[4].blit_text(win=win)
                    sys_press_r.blit_text(win=win)
                    if pg.key.get_pressed()[pg.K_r] == 1:
                        dialog1.COUNTER_DIALOGS += 1
                if dialog1.COUNTER_DIALOGS == 8:
                    bum_sym.blit_text(win=win)
                    bum_1_phrases[5].blit_text(win=win)
                    bum_1_phrases[6].blit_text(win=win)
                    sys_press_e.blit_text(win=win)
                    if pg.key.get_pressed()[pg.K_e] == 1:
                        dialog1.COUNTER_DIALOGS += 1
                if dialog1.COUNTER_DIALOGS == 9:
                    bum_sym.blit_text(win=win)
                    bum_1_phrases[7].blit_text(win=win)
                    bum_1_phrases[8].blit_text(win=win)
                    sys_press_r.blit_text(win=win)
                    if pg.key.get_pressed()[pg.K_r] == 1:
                        dialog1.COUNTER_DIALOGS += 1
                if dialog1.COUNTER_DIALOGS == 10:
                    bum_sym.blit_text(win=win)
                    bum_1_phrases[9].blit_text(win=win)
                    bum_1_phrases[10].blit_text(win=win)
                    sys_press_e.blit_text(win=win)
                    if pg.key.get_pressed()[pg.K_e] == 1:
                        dialog1.COUNTER_DIALOGS += 1
                if dialog1.COUNTER_DIALOGS == 11:
                    bum_sym.blit_text(win=win)
                    bum_1_phrases[11].blit_text(win=win)
                    bum_1_phrases[12].blit_text(win=win)
                    sys_press_r.blit_text(win=win)
                    if pg.key.get_pressed()[pg.K_r] == 1:
                        dialog1.COUNTER_DIALOGS += 1
                if dialog1.COUNTER_DIALOGS == 12:
                    bum_sym.blit_text(win=win)
                    bum_1_phrases[13].blit_text(win=win)
                    sys_exit_e.blit_text(win=win)
                    if pg.key.get_pressed()[pg.K_e] == 1:
                        dialog1.CAN_SHOW = False
                        task1 = False
                        task2 = True
                        dialog1.COUNTER_DIALOGS = 0

                        
            if task2:
                exclamation_mark2.show_image(win=win)
                dialog2.click_on_npc(player_rect=player.RECT, player_stand=player)
            if dialog2.CAN_SHOW:
                window_settings.blit_level_1 = True
                dialog2.show(win=win)
                if dialog2.COUNTER_DIALOGS == 0:
                    mc_sym.blit_text(win=win)
                    mcp[0].blit_text(win=win)
                    sys_press_e.blit_text(win=win)
                    if pg.key.get_pressed()[pg.K_e] == 1:
                        dialog2.COUNTER_DIALOGS += 1
                if dialog2.COUNTER_DIALOGS == 1:
                    meat_sym.blit_text(win=win)
                    mp[0].blit_text(win=win)
                    sys_press_r.blit_text(win=win)
                    if pg.key.get_pressed()[pg.K_r] == 1:
                        dialog2.COUNTER_DIALOGS += 1
                if dialog2.COUNTER_DIALOGS == 2:
                    mc_sym.blit_text(win=win)
                    mcp[1].blit_text(win=win)
                    sys_press_e.blit_text(win=win)
                    if pg.key.get_pressed()[pg.K_e] == 1:
                        dialog2.COUNTER_DIALOGS += 1
                if dialog2.COUNTER_DIALOGS == 3:
                    meat_sym.blit_text(win=win)
                    mp[1].blit_text(win=win)
                    sys_press_r.blit_text(win=win)
                    if pg.key.get_pressed()[pg.K_r] == 1:
                        dialog2.COUNTER_DIALOGS += 1
                if dialog2.COUNTER_DIALOGS == 4:
                    mc_sym.blit_text(win=win)
                    mcp[2].blit_text(win=win)
                    sys_exit_e.blit_text(win=win)
                    if pg.key.get_pressed()[pg.K_e] == 1:
                        dialog2.CAN_SHOW = False
                        task2 = False
                        task2_1 = True
                        can_use_ladder = True
                        can_use_canteen = True
                        dialog2.COUNTER_DIALOGS = 0
                        
            if task2_1:
                arrow_down2.show_image(win=win)
                dialog2_1.sys_alert(player_rect=player.RECT)
                if dialog2_1.SYS_ALERT:
                    if not meat.MEAT_TAKEN:
                        sys_take_meat.blit_text(win=win)
                if meat.MEAT_TAKEN:
                    dialog2_1.click_on_npc(player_rect=player.RECT, player_stand=player)
            if dialog2_1.CAN_SHOW:
                window_settings.blit_level_1 = True
                dialog2_1.show(win=win)
                if dialog2_1.COUNTER_DIALOGS == 0:
                    mc_sym.blit_text(win=win)
                    mcp2[0].blit_text(win=win)
                    sys_press_e.blit_text(win=win)
                    if pg.key.get_pressed()[pg.K_e] == 1:
                        dialog2_1.COUNTER_DIALOGS += 1
                if dialog2_1.COUNTER_DIALOGS == 1:
                    mc_sym.blit_text(win=win)
                    meatp1_2.blit_text(win=win)
                    sys_press_r.blit_text(win=win)
                    if pg.key.get_pressed()[pg.K_r] == 1:
                        dialog2_1.COUNTER_DIALOGS += 1
                if dialog2_1.COUNTER_DIALOGS == 2:
                    mc_sym.blit_text(win=win)
                    mcp2[1].blit_text(win=win)
                    sys_exit_e.blit_text(win=win)
                    if pg.key.get_pressed()[pg.K_e] == 1:
                        dialog2_1.CAN_SHOW = False
                        task2_1 = False 
                        task3 = True 
                        dialog2_1.COUNTER_DIALOGS = 0          
            
            if task3:
                exclamation_mark3.show_image(win=win)
                dialog3.click_on_npc(player_rect=player.RECT, player_stand=player)
            if dialog3.CAN_SHOW:
                window_settings.blit_level_1 = True
                dialog3.show(win=win)
                if dialog3.COUNTER_DIALOGS == 0:
                    mc_sym.blit_text(win=win)
                    mcps[0].blit_text(win=win)
                    sys_press_e.blit_text(win=win)
                    if pg.key.get_pressed()[pg.K_e] == 1:
                        dialog3.COUNTER_DIALOGS += 1
                if dialog3.COUNTER_DIALOGS == 1:
                    spy_sym.blit_text(win=win)
                    sp[0].blit_text(win=win)
                    sys_press_r.blit_text(win=win)
                    if pg.key.get_pressed()[pg.K_r] == 1:
                        dialog3.COUNTER_DIALOGS += 1
                if dialog3.COUNTER_DIALOGS == 2:
                    mc_sym.blit_text(win=win)
                    mcps[1].blit_text(win=win)
                    sys_press_e.blit_text(win=win)
                    if pg.key.get_pressed()[pg.K_e] == 1:
                        dialog3.COUNTER_DIALOGS += 1
                if dialog3.COUNTER_DIALOGS == 3:
                    spy_sym.blit_text(win=win)
                    sp[1].blit_text(win=win)
                    sys_press_r.blit_text(win=win)
                    if pg.key.get_pressed()[pg.K_r] == 1:
                        dialog3.COUNTER_DIALOGS += 1
                if dialog3.COUNTER_DIALOGS == 4:
                    spy_sym.blit_text(win=win)
                    sp[2].blit_text(win=win)
                    sys_press_e.blit_text(win=win)
                    if pg.key.get_pressed()[pg.K_e] == 1:
                        dialog3.COUNTER_DIALOGS += 1
                if dialog3.COUNTER_DIALOGS == 5:
                    mc_sym.blit_text(win=win)
                    mcps[2].blit_text(win=win)
                    sys_press_r.blit_text(win=win)
                    if pg.key.get_pressed()[pg.K_r] == 1:
                        dialog3.COUNTER_DIALOGS += 1
                if dialog3.COUNTER_DIALOGS == 6:
                    spy_sym.blit_text(win=win)
                    sp[3].blit_text(win=win)
                    sys_press_e.blit_text(win=win)
                    if pg.key.get_pressed()[pg.K_e] == 1:
                        dialog3.COUNTER_DIALOGS += 1
                if dialog3.COUNTER_DIALOGS == 7:
                    spy_sym.blit_text(win=win)
                    sp[4].blit_text(win=win)
                    sys_press_r.blit_text(win=win)
                    if pg.key.get_pressed()[pg.K_r] == 1:
                        dialog3.COUNTER_DIALOGS += 1  
                if dialog3.COUNTER_DIALOGS == 8:
                    spy_sym.blit_text(win=win)
                    sp[5].blit_text(win=win)
                    sys_press_e.blit_text(win=win)
                    if pg.key.get_pressed()[pg.K_e] == 1:
                        dialog3.COUNTER_DIALOGS += 1
                if dialog3.COUNTER_DIALOGS == 9:
                    spy_sym.blit_text(win=win)
                    sp[6].blit_text(win=win)
                    sys_press_r.blit_text(win=win)
                    if pg.key.get_pressed()[pg.K_r] == 1:
                        dialog3.COUNTER_DIALOGS += 1  
                if dialog3.COUNTER_DIALOGS == 10:
                    spy_sym.blit_text(win=win)
                    sp[7].blit_text(win=win)
                    sys_press_e.blit_text(win=win)
                    if pg.key.get_pressed()[pg.K_e] == 1:
                        dialog3.COUNTER_DIALOGS += 1          
                if dialog3.COUNTER_DIALOGS == 11:
                    spy_sym.blit_text(win=win)
                    sp[8].blit_text(win=win)
                    sys_press_r.blit_text(win=win)
                    if pg.key.get_pressed()[pg.K_r] == 1:
                        dialog3.COUNTER_DIALOGS += 1  
                if dialog3.COUNTER_DIALOGS == 12:
                    mc_sym.blit_text(win=win)
                    mcps[-1].blit_text(win=win)
                    sys_exit_e.blit_text(win=win)
                    if pg.key.get_pressed()[pg.K_e] == 1:
                        dialog3.CAN_SHOW = False
                        task3 = False
                        task3_1 = True
                        dialog3.COUNTER_DIALOGS = 0
                        
            if task3_1:
                arrow_down3.show_image(win=win)
                dialog3_1.sys_alert(player_rect=player.RECT)
                if dialog3_1.SYS_ALERT:
                    if not rope.ROPE_TAKEN or not shovel.SHOVEL_TAKEN or not scissors.SCISSORS_TAKEN or not key_from_basement.KEY_FROM_BASEMENT_TAKEN or not key_from_escape.KEY_FROM_ESCAPE_TAKEN:
                        sys_take_all_form_storeroom.blit_text(win=win)
                if rope.ROPE_TAKEN and shovel.SHOVEL_TAKEN and scissors.SCISSORS_TAKEN and key_from_basement.KEY_FROM_BASEMENT_TAKEN and key_from_escape.KEY_FROM_ESCAPE_TAKEN:
                    dialog3_1.click_on_npc(player_rect=player.RECT, player_stand=player)
            if dialog3_1.CAN_SHOW:
                window_settings.blit_level_1 = True
                dialog3_1.show(win=win)
                if dialog3_1.COUNTER_DIALOGS == 0:
                    mc_sym.blit_text(win=win)
                    mcl2[0].blit_text(win=win)
                    sys_press_e.blit_text(win=win)
                    if pg.key.get_pressed()[pg.K_e] == 1:
                        dialog3_1.COUNTER_DIALOGS += 1
                if dialog3_1.COUNTER_DIALOGS == 1:
                    spy_sym.blit_text(win=win)
                    spl2[0].blit_text(win=win)
                    sys_press_r.blit_text(win=win)
                    if pg.key.get_pressed()[pg.K_r] == 1:
                        dialog3_1.COUNTER_DIALOGS += 1
                if dialog3_1.COUNTER_DIALOGS == 2:
                    spy_sym.blit_text(win=win)
                    spl2[1].blit_text(win=win)
                    sys_press_e.blit_text(win=win)
                    if pg.key.get_pressed()[pg.K_e] == 1:
                        dialog3_1.COUNTER_DIALOGS += 1
                if dialog3_1.COUNTER_DIALOGS == 3:
                    spy_sym.blit_text(win=win)
                    spl2[2].blit_text(win=win)
                    sys_press_r.blit_text(win=win)
                    if pg.key.get_pressed()[pg.K_r] == 1:
                        dialog3_1.COUNTER_DIALOGS += 1
                if dialog3_1.COUNTER_DIALOGS == 4:
                    spy_sym.blit_text(win=win)
                    spl2[3].blit_text(win=win)
                    sys_press_e.blit_text(win=win)
                    if pg.key.get_pressed()[pg.K_e] == 1:
                        dialog3_1.COUNTER_DIALOGS += 1
                if dialog3_1.COUNTER_DIALOGS == 5:
                    spy_sym.blit_text(win=win)
                    spl2[4].blit_text(win=win)
                    sys_press_r.blit_text(win=win)
                    if pg.key.get_pressed()[pg.K_r] == 1:
                        dialog3_1.COUNTER_DIALOGS += 1
                if dialog3_1.COUNTER_DIALOGS == 6:
                    mc_sym.blit_text(win=win)
                    mcl2[1].blit_text(win=win)
                    sys_exit_e.blit_text(win=win)
                    if pg.key.get_pressed()[pg.K_e] == 1:
                        dialog3_1.CAN_SHOW = False
                        task3_1 = False
                        task4 = True
                        dialog3_1.COUNTER_DIALOGS = 0
                        guard.BREAK = True
                        
                
            if task4:
                exclamation_mark1.show_image(win=win)
                dialog4.click_on_npc(player_rect=player.RECT, player_stand=player)
            if dialog4.CAN_SHOW:
                window_settings.blit_level_1 = True
                dialog4.show(win=win)
                if dialog4.COUNTER_DIALOGS == 0:
                    mc_sym.blit_text(win=win)
                    mcpl[0].blit_text(win=win)
                    sys_press_e.blit_text(win=win)
                    if pg.key.get_pressed()[pg.K_e] == 1:
                        dialog4.COUNTER_DIALOGS += 1
                if dialog4.COUNTER_DIALOGS == 1:
                    bum_sym.blit_text(win=win)
                    buml[0].blit_text(win=win)
                    sys_press_r.blit_text(win=win)
                    if pg.key.get_pressed()[pg.K_r] == 1:
                        dialog4.COUNTER_DIALOGS += 1
                if dialog4.COUNTER_DIALOGS == 2:
                    mc_sym.blit_text(win=win)
                    mcpl[1].blit_text(win=win)
                    sys_press_e.blit_text(win=win)
                    if pg.key.get_pressed()[pg.K_e] == 1:
                        dialog4.COUNTER_DIALOGS += 1
                if dialog4.COUNTER_DIALOGS == 3:
                    bum_sym.blit_text(win=win)
                    buml[1].blit_text(win=win)
                    sys_press_r.blit_text(win=win)
                    if pg.key.get_pressed()[pg.K_r] == 1:
                        dialog4.COUNTER_DIALOGS += 1
                if dialog4.COUNTER_DIALOGS == 4:
                    mc_sym.blit_text(win=win)
                    mcpl[2].blit_text(win=win)
                    sys_press_e.blit_text(win=win)
                    if pg.key.get_pressed()[pg.K_e] == 1:
                        dialog4.COUNTER_DIALOGS += 1
                if dialog4.COUNTER_DIALOGS == 5:
                    bum_sym.blit_text(win=win)
                    buml[2].blit_text(win=win)
                    sys_press_r.blit_text(win=win)
                    if pg.key.get_pressed()[pg.K_r] == 1:
                        dialog4.COUNTER_DIALOGS += 1
                if dialog4.COUNTER_DIALOGS == 6:
                    mc_sym.blit_text(win=win)
                    mcpl[3].blit_text(win=win)
                    sys_press_e.blit_text(win=win)
                    if pg.key.get_pressed()[pg.K_e] == 1:
                        dialog4.COUNTER_DIALOGS += 1
                if dialog4.COUNTER_DIALOGS == 7:
                    bum_sym.blit_text(win=win)
                    buml[3].blit_text(win=win)
                    sys_press_r.blit_text(win=win)
                    if pg.key.get_pressed()[pg.K_r] == 1:
                        dialog4.COUNTER_DIALOGS += 1
                if dialog4.COUNTER_DIALOGS == 8:
                    mc_sym.blit_text(win=win)
                    mcpl[4].blit_text(win=win)
                    sys_exit_e.blit_text(win=win)
                    if pg.key.get_pressed()[pg.K_e] == 1:
                        task4 = False
                        dialog4.CAN_SHOW = False
                        dialog4.COUNTER_DIALOGS = 0
                        can_use_basement = True
                        can_see_bum = False

        if window_settings.can_show_comics1:
            win.blit(robbery, (0,0))
            sys_press_c.blit_text(win=win)
            
            if pg.key.get_pressed()[pg.K_c] == 1:
                window_settings.can_show_comics1 = False
                window_settings.blit_level_1 = True

        if window_settings.can_show_comics2:
            window_settings.blit_level_3 = False
            window_settings.blit_level_1 = False
            window_settings.blit_level_2 = False
            win.blit(the_end, (0, 0))
            sys_press_c.blit_text(win=win)
        
            if pg.key.get_pressed()[pg.K_c] == 1:
                window_settings.can_show_comics2 = False
                window_settings.show_menu = True

        pg.display.flip()
        screen.clock.tick(screen.fps)
        pg.display.set_caption(screen.caption)
        
run_game()