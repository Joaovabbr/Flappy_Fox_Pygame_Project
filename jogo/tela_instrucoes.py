import pygame
import random
from os import path
from sprites import Botao
from config import IMG_DIR, GREEN, FPS, GAME, QUIT, WIDTH, HEIGHT, BLACK
from assets import load_assets


def tela_instrucoes(screen):
    clock = pygame.time.Clock()
    assets = load_assets()

    
    running = True
    while running:

        # Ajusta a velocidade do jogo.
        clock.tick(FPS)

        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                state = QUIT
                running = False

            if event.type == pygame.KEYDOWN:
                state = GAME
                running = False

            

        # A cada loop, redesenha o fundo e os sprites
        screen.fill(GREEN)

        screen.blit(assets['instrucoes'], (110, 30))
        

        pygame.display.flip()

    return state
