import pygame
import sys
from constants import *
from player import *
from asteroid import *
from asteroidField import *
from circleshape import *

def main():
    pygame.init()

    print("Starting Asteroids!")

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    bullets = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (bullets, updatable, drawable)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    run = True
    clock = pygame.time.Clock()

    dt = 0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    player = Player(x,y)
    astroids = AsteroidField()

    while run == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        
        pygame.Surface.fill(screen, (0,0,0))
        

        clock.tick(60)
        dt = clock.tick(60) / 1000

        updatable.update(dt)

        for sprite in drawable:
            sprite.draw(screen)

        for astroid in asteroids:
            if astroid.collision(player) == True:
                sys.exit()

        for astroid in asteroids:
            for bullet in bullets:
                if astroid.collision(bullet) == True:
                    bullet.kill()
                    astroid.split(asteroids)

        pygame.display.update()
        


if __name__ == "__main__":
    main()
