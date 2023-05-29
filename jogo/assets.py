import pygame
import os
from config import IMG_DIR, SND_DIR, FNT_DIR


def load_assets():
    assets = {}
    assets['btn'] = pygame.image.load(os.path.join(IMG_DIR, 'btn1.png')).convert_alpha()
    
    #mudando tamanho das imagens
    largura = assets['btn'].get_rect().width * .25
    altura = assets['btn'].get_rect().height * .25
    assets['btn'] = pygame.transform.scale(assets['btn'], (300, 200))

    assets['btn_hover'] = pygame.image.load(os.path.join(IMG_DIR, 'btn1_hover.png')).convert_alpha()
    assets['btn_hover'] = pygame.transform.scale(assets['btn_hover'], (300, 200))
    assets['titulo'] = pygame.image.load(os.path.join(IMG_DIR, 'titulo.png')).convert_alpha()
    assets['titulo'] = pygame.transform.scale(assets['titulo'], (600, 400 ))

    #carregando Fonte
    assets['font'] = pygame.font.Font(os.path.join(FNT_DIR, 'PressStart2P.ttf'), 22)
    assets['font_media'] = pygame.font.Font(os.path.join(FNT_DIR, 'PressStart2P.ttf'), 30)
    assets['font_pixel'] = pygame.font.Font(os.path.join(FNT_DIR, 'Pixelmania.ttf'), 22)

    return assets
