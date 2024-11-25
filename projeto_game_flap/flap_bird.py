import pygame
import os
import random

TELA_LARGURA = 500
TELA_ALTURA = 800

IMAGEM_CANO = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'pipe.png')))
IMAGEM_CHAO = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'base.png')))
IMAGEM_BACKGROUND = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bg.png')))
IMAGENS_PASSARO = [
    pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird1.png')))
    pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird2.png')))
    pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird3.png')))
]

pygame.font.init()
FONT_PONTOS = pygame.font.SysFont('arial', 50)


class passaro:
    IMGS = IMAGENS_PASSARO
    # animação da rotação
    ROTACAO_MAXIMA = 25
    VELOCICADE_ROTACAO = 20
    TEMPO_ANIMACAO = 5

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angulo = 0
        self.velocidade = 0
        self.altura = self.y
        self.tempo = 0
        self.contagem_imagem = 0
        self.imagem = self.IMGS[0]


def pular(self):
    self.velocidade = -10.5
    self.tempo = 0
    self.altura = self.y

def mover(self):
    # clacular o deslocamento
    self.tempo += 1
    deslocamento = 1.5 * (self.tempo**2) + self.velocidade * self.tempo

    # restringir o deslocamento
    if deslocamento > 16:
        deslocamento = 16
    elif deslocamento < 0:
        deslocamento -= 2

    self.y += deslocamento

    # o angulo do passaro
    if deslocamento < 0 or self.y < (self.altura + 50):
        if self.angulo = self.ROTACAO_MAXIMA:
            self.ANGULO = self.ROTACAO_MAXIMA
        else:
            if self.angulo > -90:
                self.angulo -= self.VELOCIDADE_ROTACAO

def desenhar(self):
    # definir qual imagem do passaro vai usar
    self.contagem_imagem += 1

    if self.contagem_imagem < self.TEMPO_ANIMACAO:
        self.imagem = self.IMG[0]
    elif self.contagem_image  self.TEMPO_ANIMACAO*2:
        self.imagem = self.IMGS[1]
    elif self.contagem_imagem < self.TEMPO_ANIMACAO*3:
        self.imagem = self.imgs[2]

    # se o passaro tiver caindo eu nao vou bater asa
class cano:
    pass


class chao:
    pass
