import math
import sys
from math import radians

import pygame
import pymunk
import pymunk.pygame_util
import pygame.draw

import time

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

def main():
    rot = 0
    movex=0
    movey=0

    rot_speed = 2
    where = 118, 70
    where2x = 100
    where2y=90
    pygame.init()
    clock = pygame.time.Clock()
    clock.tick(5)



    # create new surface with white BG
    surf = pygame.Surface((5, 50))
    surf.fill((255, 255, 255))
    surf2 = pygame.Surface((40, 40))
    surf2.fill((255, 255, 255))
    # set a color key for blitting
    surf.set_colorkey((255, 0, 0))
    surf2.set_colorkey((255, 0, 0))

    # create shapes so you can tell rotation is happenning
    bigger = pygame.Rect(0, 0, 5, 50)
    smaller = pygame.Rect(0, 0, 40, 40)
    #draw those two shapes to that surface
    pygame.draw.rect(surf, (100, 0, 0), bigger)
    pygame.draw.rect(surf2, (0, 100, 0), smaller)

    screen = pygame.display.set_mode((400, 400))
    blittedRect = screen.blit(surf, where)
    blittedRect2 = screen.blit(surf2, (where2x,where2y))

    pygame.font.init()
    myfont = pygame.font.SysFont('Comic Sans MS', 20)
    pygame.display.set_caption("First Game")
    global angle
    draw_options = pymunk.pygame_util.DrawOptions(screen)


    while True:


        pygame.time.delay((100))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)

        keys = pygame.key.get_pressed()

        if keys[pygame.K_q]:
            if rot <= 45:
                rot = (rot + rot_speed)

        if keys[pygame.K_e]:
            if rot >= -45:
                rot = (rot - rot_speed)
        if keys[pygame.K_d]:
            where2x+=5
            blittedRect.centerx += 5
        if keys[pygame.K_SPACE]:
            space.gravity = (0, -980)
            circle_body.apply_impulse_at_world_point((100 * math.cos(radians(angle)), 100 * math.sin(radians(angle))), (50, 50))
        if keys[pygame.K_q] and angle < 90:
            angle = angle + 1
        if keys[pygame.K_e] and angle > 0:
            angle = angle - 1

        space.step(1 / 50.0)
        screen.fill((0, 0, 0))
        space.debug_draw(draw_options)
        #pygame.draw.line(screen, (255, 255, 255), (0, 0), (400, 400))
        # text = 'Angle: ' + str(angle)
        textsurface = myfont.render('Angle: ' + str(angle), False, (255, 255, 255))
        screen.blit(textsurface, (10, 10))
        textsurface = myfont.render('Force: 100', False, (255, 255, 255))
        screen.blit(textsurface, (10, 40))
        pygame.display.flip()
        #clock.tick(40)
        print(circle_body.position.y)


        #    blittedRect.
        #screen = pygame.display.set_mode((400, 400))
       # screen.fill((0, 0, 0))

        ##ROTATED
        # get center of surf for later
        oldCenter = blittedRect.center

        # rotate surf by DEGREE amount degrees
        rotatedSurf = pygame.transform.rotate(surf, rot)

        # get the rect of the rotated surf and set it's center to the oldCenter
        rotRect = rotatedSurf.get_rect()
        rotRect.center = oldCenter
        # draw rotatedSurf with the corrected rect so it gets put in the proper spot
        blittedRect = screen.blit(rotatedSurf, rotRect)
        blittedRect2 = screen.blit(surf2, (where2x,where2y))
        pygame.display.flip()

if __name__ == "__main__":
    main()
