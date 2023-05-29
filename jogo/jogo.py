# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
import random
from config import WIDTH, HEIGHT, INIT, GAME, QUIT, GAME_OVER
from init_screen import init_screen
from game_screen import game_screen
from tela_final import tela_final

pygame.init()
pygame.mixer.init()

# ----- Gera tela principal
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Nome')

state = INIT
while state != QUIT:
    if state == INIT:
        state = init_screen(window)
    elif state == GAME:
        state = game_screen(window)
    elif state == GAME_OVER:
        state = tela_final(window)


