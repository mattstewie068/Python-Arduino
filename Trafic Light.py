import pyfirmata
import time
import pygame

uno = pyfirmata.Arduino('COM5')

it = pyfirmata.util.Iterator(uno)
it.start()

wled = uno.get_pin('d:6:o')
bled = uno.get_pin('d:7:o')
rled = uno.get_pin('d:8:o')
yled = uno.get_pin('d:9:o')
gled = uno.get_pin('d:10:o')
button1 = uno.get_pin('d:11:i')
button2 = uno.get_pin('d:12:i')
pot1 = uno.get_pin('a:0:i')
pot2 = uno.get_pin('a:1:i')

buzz = uno.get_pin('d:5:o')


def flashing_yellow(slow):
    bled.write(1)
    time.sleep(1*slow)
    bled.write(0)
    time.sleep(1*slow)


def flashing_red(slow):
    rled.write(1)
    time.sleep(1*slow)
    rled.write(0)
    time.sleep(1*slow)


def traffic_pattern(slow):
    gled.write(1)
    time.sleep(5*slow)
    gled.write(0)
    yled.write(1)
    time.sleep(2*slow)
    yled.write(0)
    rled.write(1)
    time.sleep(5*slow)
    rled.write(0)


def falshing_cop(slow):
    bled.write(1)
    time.sleep(2*slow)
    bled.write(0)
    wled.write(1)
    time.sleep(2*slow)
    wled.write(0)
    # rled.write(1)
    # time.sleep(2*slow)
    # rled.write(0)


pygame.init()

SCREENWIDTH = 942
SCREENHEIGHT = 378
WINDOWSIZE = [SCREENWIDTH, SCREENHEIGHT]

screen = pygame.display.set_mode(WINDOWSIZE)

RUN = True
while RUN:
    for event in pygame.event.get():  # loop through all events sinse last loop
        if event.type == pygame.QUIT:
            RUN = False
        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            RUN = False

    pot1_value = pot1.read()
    # print(pot1_value)
    pot2_value = pot2.read()
    # print(pot2_value)
    button1_value = button1.read()
    # print(button1_value)
    button2_value = button2.read()
    # print(button2_value)
    time.sleep(.1)

    if pygame.mouse.get_pressed()[2]:
        flashing_yellow(pot1_value)

    if pygame.mouse.get_pressed()[1]:
        flashing_red(pot1_value)

    if pygame.mouse.get_pressed()[0]:
        # traffic_pattern(pot1_value)
        falshing_cop(pot1_value)

    screen.fill((0, 0, 0))

    pygame.display.flip()

pygame.quit()
