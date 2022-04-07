import math

import pygame.draw


class Particle:
    SCALE = 10  # 10 Pixels = 1 meter
    TIMESTEP = 1  # Seconds

    def __init__(self, x, y, radius, mass, color, max_x=0, max_y=0, x_vel=0, y_vel=0):
        self.x = x
        self.y = y
        self.radius = radius
        self.mass = mass
        self.color = color

        self.x_velocity = x_vel
        self.y_velocity = y_vel

        self.max_x = max_x
        self.max_y = max_y

    def hit(self, other):
        distance_x = self.x - other.x
        distance_y = self.y - other.y
        distance = math.sqrt(distance_x ** 2 + distance_y ** 2)
        return distance < self.radius + other.radius

    def hit_wall(self):
        return not (
                self.x - self.radius > 0 and self.x + self.radius < self.max_x and self.y - self.radius > 0 and self.y + self.radius < self.max_y)

    def wall_bounce(self):
        if self.hit_wall():
            if self.x - self.radius <= 0 or self.x + self.radius >= self.max_x:
                self.x_velocity = -self.x_velocity
            if self.y - self.radius <= 0 or self.y + self.radius >= self.max_y:
                self.y_velocity = -self.y_velocity

    @staticmethod
    def get_new_velocities(m1, m2, v1, v2):
        g_total = m1 * v1 + m2 * v2
        u1 = (g_total - m2 * (v1 - v2)) / (m1 + m2)
        u2 = v1 - v2 + u1
        return u1, u2

    def collide(self, other):
        if self.hit(other) and other is not self:
            u1_x, u2_x = self.get_new_velocities(self.mass, other.mass, self.x_velocity, other.x_velocity)
            u1_y, u2_y = self.get_new_velocities(self.mass, other.mass, self.y_velocity, other.y_velocity)
            self.x_velocity, self.y_velocity = u1_x, u1_y
            other.x_velocity, other.y_velocity = u2_x, u2_y

    def draw(self, win):
        x = self.x * self.SCALE
        y = self.y * self.SCALE
        radius = self.radius * self.SCALE

        pygame.draw.circle(win, self.color, (x, y), radius)

    def update(self, time_scale):
        self.x += self.x_velocity * (self.TIMESTEP / time_scale)
        self.y += self.y_velocity * (self.TIMESTEP / time_scale)
        self.wall_bounce()
