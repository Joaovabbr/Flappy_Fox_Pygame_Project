import pygame
import random
import time
import textwrap
pygame.init()

#CRIANDO TELA DE CRÉDITOS

# tela_creditos = pygame.display.set_mode((800, 500))

# fonte_pixel = "assets/fonts/Pixelmania.ttf"
# fonte_tamanho = 24
# fonte = pygame.font.Font(fonte_pixel, fonte_tamanho)

# texto = fonte.render("POWERED BY IRA", True, (255, 255, 255))
# texto_rect = texto.get_rect(center=(400, 300))
# tela_creditos.blit(texto, texto_rect)
# pygame.display.flip()

# time.sleep(3)

# tela_creditos.fill((0, 0, 0))
# pygame.display.flip()

# #CRIANDO TELAS DE STORYTELLING/INSTRUÇÕES

# # Importando as bibliotecas necessárias.
# from os import path

# # Dados gerais do jogo.
# TITULO = 'STORYTELLING/INSTRUÇÕES'
# WIDTH = 900 # Largura da tela
# HEIGHT = 500 # Altura da tela
# FPS = 60 # Frames por segundo

# # Define algumas variáveis com as cores básicas
# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)
# RED = (255, 0, 0)
# GREEN = (0, 255, 0)
# BLUE = (0, 0, 255)
# YELLOW = (255, 255, 0)

# # Define a sequência de textos
# TEXT2_STATES = [
#     'Você sabia que a raposa é o mascote oficial do Insper?',
#     'Então, ela se perdeu da Vila OLímpia e agora está vivendo uma aventura na floresta',
#     'Ajude ela a passar pelos obstáculos e sobreviver até ser resgatada!!',
#     'Aperte espaço para iniciar o jogo e fazer a raposa pular'

# ]

# def game_tela_st(tela_st):
#     # Variável para o ajuste de velocidade
#     clock = pygame.time.Clock()

#     # Carrega a fonte pixel
#     fonte_pixel2 = "assets/fonts/dogica.ttf"
#     fonte_tamanho2 = 13
#     fonte2 = pygame.font.Font(fonte_pixel2, fonte_tamanho2)

#     # Vamos utilizar esta variável para controlar o texto a ser mostrado
#     text2_index = 0
#     game = True
#     while text2_index < len(TEXT2_STATES) and game:

#         # Ajusta a velocidade do jogo.
#         clock.tick(FPS)

#         # Processa os eventos (mouse, teclado, botão, etc).
#         for event in pygame.event.get():

#             # Verifica se foi fechado.
#             if event.type == pygame.QUIT:
#                 game = False

#             # Verifica se soltou alguma tecla.
#             if event.type == pygame.KEYDOWN:
#                 # Dependendo da tecla, altera o estado do jogador.
#                 if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
#                     text2_index += 1

#         # Depois de processar os eventos.
#         # Atualiza o texto a ser mostrado na tela
#         if text2_index < len(TEXT2_STATES):
#             text2 = TEXT2_STATES[text2_index]
#         else:
#             text2 = ''
#         text2_image = fonte2.render(text2, True, WHITE)

#         # Quebra o texto em linhas para caber na tela
#         linhas = textwrap.wrap(text2, 100)
#         y = 10
#         for linha in linhas:
#             text2_image = fonte2.render(linha, True, WHITE)
#             tela_st.blit(text2_image, (10, y))
#             y += fonte.get_height() + 10

#         # A cada loop, redesenha o fundo e os sprites
#         tela_st.fill(BLACK)
#         tela_st.blit(text2_image, (10, 10))

#         # Depois de desenhar tudo, inverte o display.
#         pygame.display.flip()


# # Inicialização do Pygame.
# pygame.init()
# pygame.mixer.init()

# # Tamanho da tela.
# tela_st = pygame.display.set_mode((WIDTH, HEIGHT))

# # Nome do jogo
# pygame.display.set_caption(TITULO)

# # Imprime instruções
# print('*' * len(TITULO))
# print(TITULO.upper())
# print('*' * len(TITULO))
# print('Aperte a tecla espaço para avançar para o próximo texto.')

# # Comando para evitar travamentos.
# try:
#     game_tela_st(tela_st)
# finally:
#     pygame.quit()



#VARIAVEIS DO JOGO

LARGURA = 900
ALTURA = 500  

LARGURA_RAPOSA = 75
ALTURA_RAPOSA = 65

LARGURA_TUBO = 400
ALTURA_TUBO = 800

ACELERACAO = 1
VELOCIDADE_TUBOS = 10 
ESPACO_ENTRE_TUBOS = 200
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
    
    #armazena as pontuações finais de cada rodada
with open('pontuacoes.txt', 'a') as arquivo:
    pont_fps = (str(pontos))
    pontuacao_da_rodada = pont_fps[-1:] 
    arquivo.write(pontuacao_da_rodada) 
    arquivo.write('\n')    

# #TELA DE GAME OVER (GO)
# BLACK = (0, 0, 0)
# WHITE = (255, 255, 255)

# tela_go_largura = 800
# tela_go_altura = 600
# tela_go = pygame.display.set_mode((tela_go_largura, tela_go_altura))
# pygame.display.set_caption("Game Over")

# game_over_texto = fonte.render("Game Over", True, WHITE)
# restart_texto = fonte.render("Click to Restart", True, WHITE)

# game_over_rect = game_over_texto.get_rect(center=(tela_go_largura // 2, tela_go_largura // 2 - 50))
# restart_rect = restart_texto.get_rect(center=(tela_go_largura // 2, tela_go_largura // 2 + 50))

# #se nao estiver mais jogando:

# while not jogando:

#     tela_go.fill(BLACK)

#     tela_go.blit(game_over_texto, game_over_rect)
#     tela_go.blit(restart_texto, restart_rect)

#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             jogando = False
#             pygame.quit()
#         elif event.type == pygame.MOUSEBUTTONDOWN:  # Verificar se o mouse foi clicado
#             jogando = True
            

#     pygame.display.flip()
#     pygame.display.update()