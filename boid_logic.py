import math
import random
from game_logic import within_cone_of_vision
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600

class Boid:
    def __init__(self):
        self.x = random.randint(0, SCREEN_WIDTH)
        self.y = random.randint(0, SCREEN_HEIGHT)
        self.vx = random.uniform(-0.02, 0.02)
        self.vy = random.uniform(-0.02, 0.02)

        self.cone_angle = 135
        self.max_speed = 0.07
        self.min_speed = 0.02
        self.visual_range = 60
        self.protected_range = 30
        self.matching_factor = 0.0009
        self.centering_factor = 0.000004
        self.avoiding_factor = 0.000004
        self.turn_factor = 0.00002
        self.mouse_avoidance_factor = 0.0000005
        self.hunter_avoidance_factor = 0.0000009
        self.mouse_range = 40
        self.bias = 0.001

    def update(self, boids, hunters):

        for other_boid in boids:
            xpos_avg, ypos_avg, xvel_avg, yvel_avg, neighboring_boids, close_dx, close_dy = 0, 0, 0, 0, 0, 0, 0
            if other_boid != self:
                dx = self.x - other_boid.x
                dy = self.y - other_boid.y

                if (abs(dx) < self.visual_range and abs(dy) < self.visual_range):
                    distance = dx * dx + dy * dy

                    dx_heading = self.x + self.vx
                    dy_heading = self.y + self.vy

                    dx_other = other_boid.x + other_boid.vx
                    dy_other = other_boid.y + other_boid.vy

                    in_fov = within_cone_of_vision(dx_heading, dy_heading, dx_other, dy_other, self.cone_angle)

                    if distance < self.protected_range * self.protected_range and in_fov:
                        close_dx += self.x - other_boid.x
                        close_dy += self.y - other_boid.y

                    elif distance < self.visual_range * self.visual_range and in_fov:
                        xpos_avg += other_boid.x
                        ypos_avg += other_boid.y
                        xvel_avg += other_boid.vx
                        yvel_avg += other_boid.vy

                        neighboring_boids += 1
            if neighboring_boids > 0:
                xpos_avg = xpos_avg / neighboring_boids
                ypos_avg = ypos_avg / neighboring_boids
                xvel_avg = xvel_avg / neighboring_boids
                yvel_avg = yvel_avg / neighboring_boids

                self.vx = (self.vx + (xpos_avg - self.x) * self.centering_factor +
                           (xvel_avg - self.vx) * self.matching_factor)
                self.vy = (self.vy + (ypos_avg - self.y) * self.centering_factor +
                           (yvel_avg - self.vy) * self.matching_factor)

            self.vx = self.vx + (close_dx * self.avoiding_factor)
            self.vy = self.vy + (close_dy * self.avoiding_factor)

            # mouse_x, mouse_y = pygame.mouse.get_pos()
            #
            # dx = self.x - mouse_x
            # dy = self.y - mouse_y
            #
            # if (abs(dx) < self.mouse_range and abs(dy) < self.mouse_range):
            #
            #     self.vx = self.vx + (dx * self.mouse_avoidance_factor)
            #     self.vy = self.vy + (dy * self.mouse_avoidance_factor)

            for hunter in hunters:
                dx = self.x - hunter.x
                dy = self.y - hunter.y

                if (abs(dx) < self.visual_range and abs(dy) < self.visual_range):
                    self.vx = self.vx + (dx * self.hunter_avoidance_factor)
                    self.vy = self.vy + (dy * self.hunter_avoidance_factor)

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
                self.vx = (self.vx/speed) * self.min_speed
                self.vy = (self.vy/speed) * self.min_speed
            if speed > self.max_speed:
                self.vx = (self.vx/speed) * self.max_speed
                self.vy = (self.vy/speed) * self.max_speed

            self.x = self.x + self.vx
            self.y = self.y + self.vy