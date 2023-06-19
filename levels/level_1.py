from paths import bg_lvl_1_path 
from screen import width, height
import pygame as pg
from paths.get_path import get_full_path


bg_hospital = pg.image.load(bg_lvl_1_path)
bg_hospital = pg.transform.scale(bg_hospital, (width, height))

bg_dark = get_full_path(path="resources/images/level_1/bg2.jpg")
bg_dark = pg.image.load(bg_dark)
bg_dark = pg.transform.scale(bg_dark, (width, height))
