from circleshape import *
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        self.screen = screen

        pygame.draw.circle(self.screen, (255,255,255), self.position, SHOT_RADIUS, 2)

    def update(self, dt):

        self.position += self.velocity * dt 