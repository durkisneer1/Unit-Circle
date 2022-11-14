import pygame as pg
from math import cos, sin
from constants import WIDTH, HEIGHT


class UnitCircle:
    def __init__(self, screen):
        self.screen = screen
        self.pos = pg.Vector2()
        self.degrees = 0
        self.center = (WIDTH / 2, HEIGHT / 2)

    def update_degrees(self, dt):
        self.degrees += 1 * dt
        if self.degrees >= 360:
            self.degrees = 0

    def update_cos(self):
        new_x_pos = cos(self.degrees)
        self.pos.x = (new_x_pos * 200) + (WIDTH / 2)
        pg.draw.line(self.screen, "red", (self.pos.x, 0), (self.pos.x, HEIGHT), 2)

    def update_sin(self):
        new_y_pos = sin(self.degrees)
        self.pos.y = (new_y_pos * 200) + (HEIGHT / 2)
        pg.draw.line(self.screen, "blue", (0, self.pos.y), (WIDTH, self.pos.y), 2)

    def draw_circle(self):
        pg.draw.circle(self.screen, "black", self.center, 200, 1)

    def draw_triangle(self):
        pg.draw.line(self.screen, "orange", self.center, (self.pos.x, HEIGHT / 2), 2)
        pg.draw.line(self.screen, "orange", (self.pos.x, HEIGHT / 2), self.pos, 2)
        pg.draw.line(self.screen, "orange", self.center, self.pos, 2)

    def draw(self, dt):
        # Calculations
        self.update_degrees(dt)
        self.update_cos()
        self.update_sin()

        # Drawing
        self.draw_circle()
        self.draw_triangle()
        pg.draw.circle(self.screen, "black", self.pos, 6)
