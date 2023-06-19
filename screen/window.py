import pygame as pg
import screen.settings as settings
# from paths import game_icon_path
from paths.get_path import get_full_path

win = pg.display.set_mode((settings.width, settings.height))
clock = pg.time.Clock()
pg.display.set_caption(settings.caption)
pg.display.set_icon(pg.image.load(get_full_path(path="resources/images/game.ico")))