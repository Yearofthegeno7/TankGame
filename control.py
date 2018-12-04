import random, os.path

import math
import sys
from math import radians

import pygame
import pymunk
import pymunk.pygame_util
pygame.init()
win = pygame.display.set_mode((800,800))
pygame.display.set_caption("Controls")

x=250
y=250
vel=5
turnCount=0
right=False
left=False

turnRight=[pygame.image.load('persptanksRIGHT.png'),pygame.image.load("persptankDOWN.png"),pygame.image.load("persptanksLEFT.png"),pygame.image.load("persptankUP.png")]
turn=[pygame.image.load("tank sprites/tank-180.png "),pygame.image.load("tank sprites/tank-150.png"),pygame.image.load("tank sprites/tank-120.png"),pygame.image.load("tank sprites/tank-90.png"),pygame.image.load("tank sprites/tank-60.png"),pygame.image.load("tank sprites/tank-30.png"),pygame.image.load("tank sprites/tank-0.png"),pygame.image.load("tank sprites/tank+30.png"),pygame.image.load("tank sprites/tank+60.png"),pygame.image.load("tank sprites/tank+90.png"),pygame.image.load("tank sprites/tank+120.png"),pygame.image.load("tank sprites/tank+150.png"),pygame.image.load("tank sprites/tank-180.png")]

tank = pygame.image.load("persptankUP.png")

win.blit(tank,[x,y])
pygame.display.update()

############################
space = pymunk.Space()
space.gravity = (0, 0)

body = pymunk.Body(1, 1666, pymunk.Body.STATIC)
body.position = 0, 0
poly = pymunk.Poly.create_box(body, size=(800, 20))
space.add(body, poly)
mass = 1
radius = 30
angle = 45

circle_moment = pymunk.moment_for_circle(mass, 0, radius)
circle_body = pymunk.Body(mass, circle_moment)
circle_body.position = 50, 50
circle_shape = pymunk.Circle(circle_body, radius)
circle_shape.elasticity = 0.8
circle_shape.friction = 1.0
space.add(circle_body, circle_shape)

#################

def redrawGamemove():
    win.fill((0, 0, 0))
    win.blit(tank, [x, y])
    pygame.display.update()
def moveBall():
    space.step(1 / 50.0)
    win.fill((0, 0, 0))
    space.debug_draw(draw_options)
    # pygame.draw.line(screen, (255, 255, 255), (0, 0), (400, 400))
    # text = 'Angle: ' + str(angle)
    textsurface = myfont.render('Angle: ' + str(angle), False, (255, 255, 255))
    win.blit(textsurface, (10, 10))
    textsurface = myfont.render('Force: 100', False, (255, 255, 255))
    win.blit(textsurface, (10, 40))
    pygame.display.flip()
    clock.tick(40)
    print(circle_body.position.y)
run=True
while run:

    # def main():
        # pygame.init()
        pygame.font.init()
        myfont = pygame.font.SysFont('Comic Sans MS', 20)
        # screen = pygame.display.set_mode((400, 400))
        pygame.display.set_caption("First Game")
        global clock
        clock= pygame.time.Clock()
        global angle
        draw_options = pymunk.pygame_util.DrawOptions(win)


##################################

    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False

    keys=pygame.key.get_pressed()

    if keys[pygame.K_d]:
        x+=vel
        tank = pygame.image.load("persptanksRIGHT.png")
        redrawGamemove()
    if keys[pygame.K_a]:
        x-=vel
        tank = pygame.image.load("persptanksLEFT.png")
        redrawGamemove()
    if keys[pygame.K_SPACE]:
        space.gravity = (0, -980)
        circle_body.apply_impulse_at_world_point((100 * math.cos(radians(angle)), 100 * math.sin(radians(angle))),
                                                 (50, 50))
    if keys[pygame.K_q] and angle < 90:
        angle = angle + 1
    if keys[pygame.K_e] and angle > 0:
        angle = angle - 1

    ############################
# def main():
#     #pygame.init()
#     pygame.font.init()
#     myfont = pygame.font.SysFont('Comic Sans MS', 20)
#     #screen = pygame.display.set_mode((400, 400))
#     pygame.display.set_caption("First Game")
#     clock = pygame.time.Clock()
#     global angle
#     draw_options = pymunk.pygame_util.DrawOptions(win)

    # while True:
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             sys.exit(0)
    #
    #     keys = pygame.key.get_pressed()
    #
    #     if keys[pygame.K_SPACE]:
    #         space.gravity = (0, -980)
    #         circle_body.apply_impulse_at_world_point((100 * math.cos(radians(angle)), 100 * math.sin(radians(angle))), (50, 50))
    #     if keys[pygame.K_q] and angle < 90:
    #         angle = angle + 1
    #     if keys[pygame.K_e] and angle > 0:
    #         angle = angle - 1
    #
    #     space.step(1 / 50.0)
    #     win.fill((0, 0, 0))
    #     space.debug_draw(draw_options)
    #     #pygame.draw.line(screen, (255, 255, 255), (0, 0), (400, 400))
    #     # text = 'Angle: ' + str(angle)
    #     textsurface = myfont.render('Angle: ' + str(angle), False, (255, 255, 255))
    #     win.blit(textsurface, (10, 10))
    #     textsurface = myfont.render('Force: 100', False, (255, 255, 255))
    #     win.blit(textsurface, (10, 40))
    #     pygame.display.flip()
    #     clock.tick(40)
    #     print(circle_body.position.y)


if __name__ == "__main__":
    main()



##draws it on the screen with x y coordinates




