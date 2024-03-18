import pygame
from config import WIDTH, HEIGHT,ACELERACAO, VELOCIDADE_TUBOS, load_img, LARGURA_TUBO, ALTURA_TUBO

class Botao(pygame.sprite.Sprite):
    def __init__(self, assets, nome_do_jogo):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.assets = assets
        self.image = assets['btn'] # assets é um dicionário de imagens, sons e fonts 
        self.mask = pygame.mask.from_surface(self.image)
        #todo objeto precisa de um rect
        # rect é a representação de retangulo feita pelo pygame
        self.rect = self.image.get_rect()
        # é preciso definir onde a imagem deve aparecer no jogo
        self.rect.x = 0
        self.rect.y = 0

        self.nome_do_jogo = nome_do_jogo

    def mouse_over(self, over):
        # Toda a lógica de movimentação deve ser feita aqui
        # Atualização da posição da nave
        if over:
            self.image = self.assets['btn_hover']
        else:
            self.image = self.assets['btn']

class Raposa(pygame.sprite.Sprite):
        def __init__(self, img):
            pygame.sprite.Sprite.__init__(self)
            self.image = img
            self.rect = self.image.get_rect()
            self.rect.centerx = WIDTH / 2
            self.rect.bottom = HEIGHT / 2
            self.speed_y = 0
            self.mask = pygame.mask.from_surface(self.image)

        def update(self):   
            self.speed_y += ACELERACAO
            self.rect.bottom += self.speed_y

            if self.rect.bottom > HEIGHT:
                self.rect.bottom = HEIGHT


class Tubo(pygame.sprite.Sprite):
        def __init__(self, inverted, xpos, ypos):
            pygame.sprite.Sprite.__init__(self)
            self.image = load_img('assets/imgs/tubo.png', LARGURA_TUBO, ALTURA_TUBO)
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
    