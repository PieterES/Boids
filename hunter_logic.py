import math
import random
from game_logic import within_cone_of_vision
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600

class Hunter:
    def __init__(self):
        self.x = random.randint(0, SCREEN_WIDTH)
        self.y = random.randint(0, SCREEN_HEIGHT)
        self.vx = random.uniform(-2, 2)
        self.vy = random.uniform(-2, 2)

        self.cone_angle = 90
        self.max_speed = 4
        self.min_speed = 1.5
        self.visual_range = 100
        self.turn_factor = 0.3
        self.centering_factor = 0.00005
        self.boid_factor = 0.02

    def update(self, boids):
        xpos_avg, ypos_avg, xvel_avg, yvel_avg = 0, 0, 0, 0
        neighboring_boids = 0
        for boid in boids:
            dx = self.x - boid.x
            dy = self.y - boid.y

            if (abs(dx) < self.visual_range and abs(dy) < self.visual_range):
                distance = dx * dx + dy * dy

                xpos_avg += boid.x
                ypos_avg += boid.y
                xvel_avg += boid.vx
                yvel_avg += boid.vy

                neighboring_boids += 1
        if neighboring_boids > 0:
            xpos_avg = xpos_avg / neighboring_boids
            ypos_avg = ypos_avg / neighboring_boids
            xvel_avg = xvel_avg / neighboring_boids
            yvel_avg = yvel_avg / neighboring_boids

            self.vx = (self.vx + (xpos_avg - self.x) * self.boid_factor)
            self.vy = (self.vy + (ypos_avg - self.y) * self.boid_factor)

        if self.y < 100:
            self.vy = self.vy + self.turn_factor
        if self.y > SCREEN_HEIGHT - 100:
            self.vy = self.vy - self.turn_factor
        if self.x < 100:
            self.vx = self.vx + self.turn_factor
        if self.x > SCREEN_WIDTH - 100:
            self.vx = self.vx - self.turn_factor

        speed = math.sqrt(self.vx * self.vx + self.vy * self.vy)

        if speed < self.min_speed:
            self.vx = (self.vx / speed) * self.min_speed
            self.vy = (self.vy / speed) * self.min_speed
        if speed > self.max_speed:
            self.vx = (self.vx / speed) * self.max_speed
            self.vy = (self.vy / speed) * self.max_speed

        self.x = self.x + self.vx
        self.y = self.y + self.vy