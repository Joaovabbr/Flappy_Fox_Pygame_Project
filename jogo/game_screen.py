import pygame
import random
from config import FPS, WIDTH, HEIGHT, GREEN, WHITE
from assets import load_assets
from tela_final import tela_final





def game_screen(screen):
    LARGURA = 900
    ALTURA = 500  

    LARGURA_RAPOSA = 75
    ALTURA_RAPOSA = 65

    LARGURA_TUBO = 400
    ALTURA_TUBO = 800

    ACELERACAO = 1
    VELOCIDADE_TUBOS = 10 
    ESPACO_ENTRE_TUBOS = 250
    DESLIZAR = 4
    X = 0
    
    relogio = pygame.time.Clock()
    FPS = 40


    pontos = 0
    pass_tubo = False
    font = pygame.font.SysFont('Bauhaus 93', 60)


    amarelo = (255, 255, 0)
    jogando = True

    tela = pygame.display.set_mode((LARGURA, ALTURA))
    pygame.display.set_caption('Flappy Fox')

    img_raposa = pygame.image.load('assets/imgs/img_rap.png').convert_alpha()
    img_raposa = pygame.transform.scale(img_raposa, (LARGURA_RAPOSA, ALTURA_RAPOSA))
    img_fundo = pygame.image.load('assets/imgs/wallpaper.webp').convert()
    img_fundo = pygame.transform.scale(img_fundo, (LARGURA, ALTURA))
    img_tubo = pygame.image.load('assets/imgs/tubo.PNG').convert_alpha()
    img_tubo = pygame.transform.scale(img_tubo, (LARGURA_TUBO, ALTURA_TUBO)) 


    def texto_pontos(text, font, cor_texto, x, y):
        img = font.render(text, font, cor_texto)
        tela.blit(img,(x,y))

    class Raposa(pygame.sprite.Sprite):
        def __init__(self, img):
            pygame.sprite.Sprite.__init__(self)
            self.image = img
            self.rect = self.image.get_rect()
            self.rect.centerx = LARGURA / 2
            self.rect.bottom = ALTURA / 2
            self.speed_y = 0
            self.mask = pygame.mask.from_surface(self.image)

        def update(self): 
            self.speed_y += ACELERACAO
            self.rect.bottom += self.speed_y

            if self.rect.bottom > ALTURA:
                self.rect.bottom = ALTURA

    class Tubo(pygame.sprite.Sprite):
        def __init__(self, inverted, xpos, ypos):
            pygame.sprite.Sprite.__init__(self)
            self.image = img_tubo
            self.rect = self.image.get_rect()
            self.rect.x = xpos
            self.rect.height = self.image.get_height()

            if inverted:
                self.image = pygame.transform.flip(self.image, False, True)
                self.rect.y = ypos - self.rect.height
            else:
                self.rect.y = ypos

        def update(self):
            self.rect.x -= VELOCIDADE_TUBOS

        def get_mask(self):
            return pygame.mask.from_surface(self.image)

    todos_sprites = pygame.sprite.Group()
    raposa_jogo = Raposa(img_raposa)
    todos_sprites.add(raposa_jogo)
    tubos = pygame.sprite.Group()

    def criar_tubos(xpos):
        tamanho = random.randint(100, 210)
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

    state = tela_final(screen)

    with open('pontuacoes.txt', 'a') as arquivo:
        pont_fps = (str(pontos))
        pontuacao_da_rodada = pont_fps[-1:] 
        arquivo.write(pontuacao_da_rodada) 
        arquivo.write('\n')  
          
    return state