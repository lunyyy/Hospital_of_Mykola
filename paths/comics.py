import pygame
from paths.get_path import get_full_path

robbery = get_full_path(path="resources/images/comics/robbery.jpg")
robbery = pygame.image.load(robbery)
robbery = pygame.transform.scale(robbery, (1200, 800))


the_end = get_full_path(path="resources/images/comics/the_end.jpg")
the_end = pygame.image.load(the_end)
the_end = pygame.transform.scale(the_end, (1200, 800))