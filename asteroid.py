import random
from circleshape import *
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

        self.position = pygame.Vector2(x, y)

    def draw(self, screen):
        self.screen = screen

        pygame.draw.circle(self.screen, (255,255,255), self.position, self.radius, 2)

    def split(self, asteroids):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        random_angle = random.uniform(20, 50)

        velocity_1 = self.velocity.rotate(random_angle) * 1.2
        velocity_2 = self.velocity.rotate(-random_angle) * 1.2 

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        new_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)

        new_asteroid_1.velocity = velocity_1
        new_asteroid_2.velocity = velocity_2

        asteroids.add(new_asteroid_1)
        asteroids.add(new_asteroid_2)

    def update(self, dt):

        self.position += self.velocity * dt 
