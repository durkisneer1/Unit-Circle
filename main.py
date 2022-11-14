import pygame as pg
from circle import UnitCircle
from constants import WIN_RES

pg.init()
screen = pg.display.set_mode(WIN_RES)
pg.display.set_caption("Unit Circle")
clock = pg.time.Clock()

circle = UnitCircle(screen)


def main():
    run = True
    while run:
        dt = clock.tick(60) / 1000
        events = pg.event.get()
        for ev in events:
            if ev.type == pg.QUIT or (ev.type == pg.KEYDOWN and ev.key == pg.K_ESCAPE):
                run = False

        screen.fill("lightgray")
        circle.draw(dt)

        pg.display.flip()


if __name__ == "__main__":
    main()
    
