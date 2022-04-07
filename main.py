import pygame
import random
from Box import Box
from Particle import Particle

pygame.init()

WIDTH, HEIGHT = 1000, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Particle Simulation")

colors = [(255, 255, 255), (255, 255, 10), (0, 255, 20), (180, 40, 50), (80, 80, 80), (10, 20, 255)]

if __name__ == "__main__":
    run = True
    clock = pygame.time.Clock()

    SPEED_MULTI = 1

    box = Box(WIDTH / Particle.SCALE, HEIGHT / Particle.SCALE, 0)
    for i in range(20):
        box.add_particle(
            Particle(random.randint(3, WIDTH / Particle.SCALE - 3), random.randint(3, HEIGHT / Particle.SCALE - 3),
                     random.randint(2, 2), random.randint(5, 30), colors[random.randint(1, 5)],
                     WIDTH / Particle.SCALE, HEIGHT / Particle.SCALE, random.randint(0, 2) / 10 * SPEED_MULTI,
                     random.randint(0, 2) / 10 * SPEED_MULTI))

    while run:
        clock.tick(60 * Box.TIME_SCALE)
        WIN.fill(colors[0])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        box.update()
        box.draw(WIN)

        pygame.display.update()

    pygame.quit()
