from paths import background_path, help_path
from screen import width, height
import pygame as pg


bg = pg.image.load(background_path)
bg = pg.transform.scale(bg, (width, height))

help_bg = pg.image.load(help_path)
help_bg = pg.transform.scale(help_bg, (1000, 800))
author_bg = pg.image.load(help_path)
author_bg = pg.transform.scale(author_bg, (1000, 800))