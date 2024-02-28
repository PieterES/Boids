import pygame
import sys
import random
import math
import vidmaker
from Boid_logic import Boid
from Hunter_logic import Hunter
from Game_logic import *
pygame.init()


SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Boids with Hunters')
video = vidmaker.Video(path='video2.mp4', late_export=True)

RED = (255, 0 ,0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
NUM_BOIDS = 100
NUM_HUNTERS = 2
boids = [Boid() for _ in range(NUM_BOIDS)]
hunters =[Hunter() for _ in range(NUM_HUNTERS)]

for _ in range(5000):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill(BLACK)

    for boid in boids:
        boid.update(boids, hunters)
    for hunter in hunters:
        hunter.update(boids)

    for boid in boids:
        desired_location = (boid.x + boid.vx, boid.y + boid.vy)
        points = rotate_triangle((boid.x, boid.y), 5, desired_location)
        pygame.draw.polygon(screen, WHITE, points)

    for hunter in hunters:
        desired_location = (hunter.x + hunter.vx, hunter.y + hunter.vy)
        points = rotate_triangle((hunter.x, hunter.y), 5, desired_location)
        pygame.draw.polygon(screen, RED, points)

    video.update(pygame.surfarray.pixels3d(screen).swapaxes(0, 1), inverted=False)
    pygame.display.flip()
video.export(verbose=True)
video.compress(target_size=2045, new_file=True)