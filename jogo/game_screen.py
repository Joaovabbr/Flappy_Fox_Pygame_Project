import pygame
import random
from config import load_img, LARGURA_RAPOSA, WIDTH, HEIGHT, ALTURA_RAPOSA, LARGURA_TUBO, ALTURA_TUBO #remove import config 
from assets import load_assets
from tela_final import tela_final
from sprites import Raposa, Tubo
#importar class raposa e tubo 





def game_screen(screen): 
    LARGURA = WIDTH
    ALTURA = HEIGHT
    VELOCIDADE_TUBOS = 10 
    
    relogio = pygame.time.Clock()
    FPS = 40


    pontos = 0
    pass_tubo = False
    font = pygame.font.SysFont('Bauhaus 93', 60)


    amarelo = (255, 255, 0)
    jogando = True

    tela = pygame.display.set_mode((LARGURA, ALTURA))
    pygame.display.set_caption('Flappy Fox')

    img_raposa = load_img('assets/imgs/img_rap.png', LARGURA_RAPOSA,ALTURA_RAPOSA)
    img_fundo = load_img('assets/imgs/wallpaper.webp', LARGURA, ALTURA)

    def texto_pontos(text, font, cor_texto, x, y):
        img = font.render(text, font, cor_texto)
        tela.blit(img,(x,y))

    
    todos_sprites = pygame.sprite.Group()
    raposa_jogo = Raposa(img_raposa)
    todos_sprites.add(raposa_jogo)
    tubos = pygame.sprite.Group() 
    #Criar variavel quantidade de tubos ou metodo 

    def criar_tubos(xpos):
        tamanho = random.randint(50, 250)
        ESPACO_ENTRE_TUBOS = random.randrange(200, 285)
        tubo_inferior = Tubo(False, xpos, tamanho)
        tubo_superior = Tubo(True, xpos, tamanho + ESPACO_ENTRE_TUBOS)
        return (tubo_inferior, tubo_superior)

    for i in range(2):
        tubo = criar_tubos(LARGURA * i + 800)
        tubos.add(tubo[0])
        tubos.add(tubo[1])

    while jogando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                jogando = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    assets = load_assets()
                    assets['som_pulo'].play()
                    raposa_jogo.speed_y = -10

        tela.blit(img_fundo, (0, 0))

        if len(tubos) > 0:
            if todos_sprites.sprites()[0].rect.left > tubos.sprites()[0].rect.left\
                and todos_sprites.sprites()[0].rect.right < tubos.sprites()[0].rect.right\
                and pass_tubo == False:
                pass_tubo = True
            if pass_tubo == True:
                if todos_sprites.sprites()[0].rect.left > tubos.sprites()[0].rect.right:
                    pontos = pontos + 1
                    pass_tubo = False
                    VELOCIDADE_TUBOS = VELOCIDADE_TUBOS + 0.5

        texto_pontos(str(pontos), font, amarelo, 450,0)
        
        if pygame.sprite.spritecollide(raposa_jogo, tubos, False, pygame.sprite.collide_mask):
            jogando = False

        # Cria novos tubos
        if len(tubos) < 3:
            tubo = criar_tubos(LARGURA + LARGURA_TUBO)
            tubos.add(tubo[0])
            tubos.add(tubo[1])

        todos_sprites.update()
        tubos.update()

        for tubo in tubos.copy():
            if tubo.rect.right < 0:
                tubos.remove(tubo)
                todos_sprites.remove(tubo)

        todos_sprites.draw(tela)
        tubos.draw(tela)

        relogio.tick(FPS)
        pygame.display.update()

    with open('pontuacoes.txt', 'a') as arquivo:
        lista_pont_fps = []
        lista_pont_fps.append(str(pontos))
        print(lista_pont_fps)
        pontuacao_da_rodada = lista_pont_fps[-1] 
        arquivo.write(pontuacao_da_rodada) 
        arquivo.write('\n')  
        
    state = tela_final(screen)

    
          
    return state