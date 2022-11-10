import pygame as pg
from constants import SCREEN_RES
from circle import UnitCircle

pg.init()
screen = pg.display.set_mode(SCREEN_RES)
pg.display.set_caption("Unit Circle")
clock = pg.time.Clock()

circle = UnitCircle(screen)


def main():
    run = True
    while run:
        dt = clock.tick(60)
        events = pg.event.get()
        for ev in events:
            if ev.type == pg.QUIT or (ev.type == pg.KEYDOWN and ev.key == pg.K_ESCAPE):
                run = False

        screen.fill("lightgray")
        circle.draw(dt)

        pg.display.flip()


if __name__ == "__main__":
    main()
