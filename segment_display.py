import pyfirmata
import time
import pygame

uno = pyfirmata.Arduino('COM5')

it = pyfirmata.util.Iterator(uno)
it.start()

led_a = uno.get_pin('d:2:o')
led_b = uno.get_pin('d:3:o')
led_c = uno.get_pin('d:4:o')
led_d = uno.get_pin('d:5:o')
led_e = uno.get_pin('d:6:o')
led_f = uno.get_pin('d:7:o')
led_g = uno.get_pin('d:8:o')
pot1 = uno.get_pin('a:0:i')
switch_1 = uno.get_pin('d:12:i')
switch_2 = uno.get_pin('d:11:i')
switch_3 = uno.get_pin('d:10:i')
switch_4 = uno.get_pin('d:9:i')

# 0 = on, 1 = off


def display_off():
    led_a.write(1)
    led_b.write(1)
    led_c.write(1)
    led_d.write(1)
    led_e.write(1)
    led_f.write(1)
    led_g.write(1)


def display_0():
    led_a.write(0)
    led_b.write(0)
    led_c.write(1)
    led_d.write(0)
    led_e.write(0)
    led_f.write(0)
    led_g.write(0)


def display_1():
    led_a.write(1)
    led_b.write(0)
    led_c.write(1)
    led_d.write(1)
    led_e.write(1)
    led_f.write(1)
    led_g.write(0)


def display_2():
    led_a.write(0)
    led_b.write(1)
    led_c.write(0)
    led_d.write(0)
    led_e.write(1)
    led_f.write(0)
    led_g.write(0)


def display_3():
    led_a.write(1)
    led_b.write(0)
    led_c.write(0)
    led_d.write(0)
    led_e.write(1)
    led_f.write(0)
    led_g.write(0)


def display_4():
    led_a.write(1)
    led_b.write(0)
    led_c.write(0)
    led_d.write(1)
    led_e.write(0)
    led_f.write(1)
    led_g.write(0)


def display_5():
    led_a.write(1)
    led_b.write(0)
    led_c.write(0)
    led_d.write(0)
    led_e.write(0)
    led_f.write(0)
    led_g.write(1)


def display_6():
    led_a.write(0)
    led_b.write(0)
    led_c.write(0)
    led_d.write(0)
    led_e.write(0)
    led_f.write(0)
    led_g.write(1)


def display_7():
    led_a.write(1)
    led_b.write(0)
    led_c.write(1)
    led_d.write(1)
    led_e.write(1)
    led_f.write(0)
    led_g.write(0)


def display_8():
    led_a.write(0)
    led_b.write(0)
    led_c.write(0)
    led_d.write(0)
    led_e.write(0)
    led_f.write(0)
    led_g.write(0)


def display_9():
    led_a.write(1)
    led_b.write(0)
    led_c.write(0)
    led_d.write(0)
    led_e.write(0)
    led_f.write(0)
    led_g.write(0)


def display_char(i):
    switcher = {
        0: display_0,
        1: display_1,
        2: display_2,
        3: display_3,
        4: display_4,
        5: display_5,
        6: display_6,
        7: display_7,
        8: display_8,
        9: display_9,
        10: display_off,
    }
    func = switcher.get(i, "Only 0-9 available")
    return func()


display_char(4)

pygame.init()

SCREENWIDTH = 500
SCREENHEIGHT = 500
WINDOWSIZE = [SCREENWIDTH, SCREENHEIGHT]

screen = pygame.display.set_mode(WINDOWSIZE)

RUN = True
while RUN:

    # led_a.write(1)
    # led_b.write(1)
    # led_c.write(1)
    # led_d.write(1)
    # led_e.write(1)
    # led_f.write(1)
    # led_g.write(1)

    pot1_value = pot1.read()
    switch1_value = switch_1.read()
    switch2_value = switch_2.read()
    switch3_value = switch_3.read()
    switch4_value = switch_4.read()

    for event in pygame.event.get():  # loop through all events sinse last loop
        if event.type == pygame.QUIT:
            RUN = False
        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            RUN = False
        if pygame.key.get_pressed()[pygame.K_SPACE]:
            print(switch1_value)
            print(switch2_value)
            print(switch3_value)
            print(switch4_value)

    if pygame.mouse.get_pressed()[0]:
        display_0()
        time.sleep(pot1.read())
        display_1()
        time.sleep(pot1.read())
        display_2()
        time.sleep(pot1.read())
        display_3()
        time.sleep(pot1.read())
        display_4()
        time.sleep(pot1.read())
        display_5()
        time.sleep(pot1.read())
        display_6()
        time.sleep(pot1.read())
        display_7()
        time.sleep(pot1.read())
        display_8()
        time.sleep(pot1.read())
        display_9()
        time.sleep(pot1.read())

    screen.fill((0, 0, 0))

    pygame.display.flip()

pygame.quit()
