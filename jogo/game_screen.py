import pygame
from config import FPS, WIDTH, HEIGHT, GREEN, WHITE
from assets import load_assets





def game_screen(window):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    assets = load_assets()

    DONE = 0
    PLAYING = 1
    state = PLAYING

    # ===== Loop principal =====
    while state != DONE:
        clock.tick(FPS)

        # ----- Trata eventos
        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                state = DONE

        # ----- Gera saídas
        window.fill(GREEN)  # Preenche com a cor branca


        tela_texto = assets['font_media'].render("Tela com o seu jogo", True, WHITE)
        text_rect = tela_texto.get_rect()
        text_rect.centerx = WIDTH / 2
        text_rect.centery = 200
        window.blit(tela_texto, text_rect)

        pygame.display.update()  # Mostra o novo frame para o jogador

    return state
