from circleshape import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

        self.position = pygame.Vector2(x, y)

    def draw(self, screen):
        self.screen = screen

        pygame.draw.circle(self.screen, (255,255,255), self.position, self.radius, 2)

    def update(self, dt):

        self.position += self.velocity * dt 
