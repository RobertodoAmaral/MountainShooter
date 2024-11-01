from code.Const import ENTITY_SPEED
from code.Entity import Entity


class PlayerShot(Entity):

    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

        if name == 'Enemy3Shot':
            self.surf = pygame.image.load('asset/Enemy3Shot.png').convert_alpha()

    def move(self, ):
        if self.name == 'Enemy3Shot':
            self.rect.centerx -= ENTITY_SPEED[self.name]
        else:
            self.rect.centerx += ENTITY_SPEED[self.name]
