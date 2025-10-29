import pygame
from constants import *
from player import *
from asteroids import *
from asteroidfield import *

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    new_player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_group = pygame.sprite.Group()
    Asteroid.containers = (asteroid_group, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)
        pygame.Surface.fill(screen, "black")
        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()
        tick = clock.tick(60)
        dt = tick/1000
if __name__ == "__main__":
    main()
