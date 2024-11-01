#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Const import ENTITY_SPEED, ENTITY_SHOT_DELAY
from code.EnemyShot import EnemyShot
from code.Entity import Entity


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]

    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]

    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            return EnemyShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))

class Enemy3(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.surf = pygame.image.load('./asset/Enemy3.png').convert_alpha()
        self.rect = self.surf.get_rect(center=position)
        self.direction_y = -1  # Inicialmente subindo
        self.speed_y = ENTITY_SPEED[self.name]  # Velocidade vertical inicial
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]

    def move(self):
        # Movimento horizontal: da direita para a esquerda
        self.rect.centerx -= ENTITY_SPEED[self.name]

        # Movimento vertical: sobe e desce
        self.rect.centery += self.speed_y * self.direction_y
        if self.rect.bottom >= WIN_HEIGHT:  # Bateu na borda inferior
            self.direction_y = -1  # Mudar para subir
            self.speed_y = ENTITY_SPEED[self.name]
        elif self.rect.top <= 0:  # Bateu na borda superior
            self.direction_y = 1  # Mudar para descer
            self.speed_y = 2 * ENTITY_SPEED[self.name]  # Velocidade dobrada para descer

    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            return EnemyShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))
