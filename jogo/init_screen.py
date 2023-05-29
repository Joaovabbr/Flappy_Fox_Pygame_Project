import pygame
import random
from os import path
from sprites import Botao
from config import IMG_DIR, GREEN, FPS, GAME, QUIT, WIDTH, HEIGHT, BLACK
from assets import load_assets


def init_screen(screen):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()
    assets = load_assets()
    # Criando botoes
    all_buttons = pygame.sprite.Group()

    # Calculando espaçamento entre os botões
    # Criando um botão apenas para pegar as medidas de um botão para realizar o calculo
    medidas_botao = Botao(assets, '')
    # O espaçamento é feito através da largura da janela menos o 
    # espaço necessário para posicionar 4 botões
    # depois é calculado o tamanho para 5 espaços vazios
    espacamento = (WIDTH - (medidas_botao.rect.width * 2))/ 3
    x = espacamento
    y = HEIGHT /2

    # Criando primeira fileira com 4 botões

    jogo = Botao(assets, "Jogar")

    # jogo = Botao(assets, 'Instruções')

    jogo.rect.x = x
    jogo.rect.centery = y + 90
    all_buttons.add(jogo)
    
    jogo1 = Botao(assets, "Instruções")
    jogo1.rect.x = x + 400
    jogo1.rect.centery = y + 90 
    all_buttons.add(jogo1)

    # Criando segunda fileira de Botões
    
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

            if event.type == pygame.KEYUP:
                state = GAME
                running = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                state = GAME
                running = False

            if event.type == pygame.MOUSEMOTION:
                #Alterando cor do botão
                for btn in all_buttons:
                    if btn.rect.collidepoint(event.pos):
                        btn.mouse_over(True)
                    else:
                        btn.mouse_over(False)
            

        # A cada loop, redesenha o fundo e os sprites
        screen.fill(GREEN)

        all_buttons.draw(screen)

        # Escrevendo texto dos botões
        for btn in all_buttons:
            btn_texto = assets['font'].render(f"{btn.nome_do_jogo}", True, BLACK)
            text_rect = btn_texto.get_rect()
            text_rect.centerx = btn.rect.centerx
            text_rect.centery = btn.rect.centery
            screen.blit(btn_texto, text_rect)

        tela_texto = assets['font_pixel'].render("F", False, BLACK)

        text_rect = tela_texto.get_rect()
        text_rect.centerx = WIDTH / 2
        text_rect.centery = 200
        screen.blit(assets['titulo'], (140, 90))
        
        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

    return state
