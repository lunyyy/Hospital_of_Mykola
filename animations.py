import paths
import pygame as pg




player = {
    'RUN': (pg.image.load(paths.run1_path),
            pg.image.load(paths.run2_path)),
    
    'STAND': (pg.image.load(paths.idle1_path),
              pg.image.load(paths.idle1_path)),
    
    'DIG': (pg.image.load(paths.diging1_path),
            pg.image.load(paths.diging2_path),
            pg.image.load(paths.diging3_path),
            pg.image.load(paths.diging4_path))
}

guard = {
    'RUN': (pg.image.load(paths.guard1_path),
            pg.image.load(paths.guard2_path))
}

cleaner = {
    'RUN': (pg.image.load(paths.cleaner1_path),
            pg.image.load(paths.cleaner2_path))
}