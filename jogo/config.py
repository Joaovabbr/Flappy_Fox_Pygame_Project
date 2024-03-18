from os import path
import pygame

# Estabelece a pasta que contem as figuras e sons.
IMG_DIR = path.join(path.dirname(__file__), 'assets', 'imgs')
SND_DIR = path.join(path.dirname(__file__), 'assets', 'snd')
FNT_DIR = path.join(path.dirname(__file__), 'assets', 'fonts')

# Dados gerais do jogo.
WIDTH = 900 # Largura da tela
HEIGHT = 500 # Altura da tela
FPS = 60 # Frames por segundo

# Dados da raposa
LARGURA_RAPOSA = 125
ALTURA_RAPOSA = 115
ACELERACAO = 1

# Dados dos tubos
LARGURA_TUBO = 400
ALTURA_TUBO = 800
VELOCIDADE_TUBOS = 10

# Define algumas variáveis com as cores básicas
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 153, 51)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Estados para controle do fluxo da aplicação
INIT = 0
GAME = 1
INSTRUCOES = 2
QUIT = 3
GAME_OVER = 4

def load_img(str_img, largura, altura):
    img = pygame.image.load(str_img).convert_alpha()
    img = pygame.transform.scale(img, (largura, altura))
    return img 