import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    fps = pygame.time.Clock()
    dt = 0
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    asteroid_field = AsteroidField()

    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)

    Player.containers = (updatable, drawable)
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)
    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        updatable.update(dt)
        
        for asteroid in asteroids:
            if asteroid.check_collision(player):
                print("Game over!")
                sys.exit()
        for asteroid in asteroids:
            for bullet in shots:
                if bullet.check_collision(asteroid):
                    bullet.kill()
                    asteroid.kill()
        screen.fill((0, 0, 0))

        for sprite in drawable:
            sprite.draw(screen)
        
        pygame.display.flip()
        dt = fps.tick(60) / 1000
        
if __name__ == "__main__":
    main()