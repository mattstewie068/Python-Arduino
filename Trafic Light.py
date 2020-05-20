import pyfirmata
import time
import pygame

uno = pyfirmata.Arduino('COM5')

wled = uno.get_pin('d:10:o')
rled = uno.get_pin('d:9:o')
yled = uno.get_pin('d:8:o')
gled = uno.get_pin('d:7:o')


def falshing_yellow():
    yled.write(1)
    time.sleep(1)
    yled.write(0)
    time.sleep(1)


def falshing_red():
    rled.write(1)
    time.sleep(1)
    rled.write(0)
    time.sleep(1)


def traffic_pattern():
    gled.write(1)
    time.sleep(5)
    gled.write(0)
    yled.write(1)
    time.sleep(2)
    yled.write(0)
    rled.write(1)
    time.sleep(5)
    rled.write(0)


pygame.init()

SCREENWIDTH = 942
SCREENHEIGHT = 378
WINDOWSIZE = [SCREENWIDTH, SCREENHEIGHT]

screen = pygame.display.set_mode(WINDOWSIZE)

RUN = True
mouse = False
while RUN:
    for event in pygame.event.get():  # loop through all events sinse last loop
        if event.type == pygame.QUIT:
            RUN = False
        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            RUN = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse = True
            if pygame.mouse.get_pressed()[2] and mouse:
                falshing_yellow()

            if pygame.mouse.get_pressed()[1] and mouse:
                falshing_red()

            if pygame.mouse.get_pressed()[0] and mouse:
                traffic_pattern()

        elif event.type == pygame.MOUSEBUTTONUP:
            mouse = False

    screen.fill((0, 0, 0))

    pygame.display.flip()

pygame.quit()
