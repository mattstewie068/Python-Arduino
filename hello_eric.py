import pygame
import segment_display as sd

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

    for event in pygame.event.get():  # loop through all events sinse last loop
        if event.type == pygame.QUIT:
            RUN = False
        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            RUN = False
        if pygame.key.get_pressed()[pygame.K_SPACE]:
            print(sd.switch_1_state())
            print(sd.switch_2_state())
            print(sd.switch_3_state())
            print(sd.switch_4_state())

    if pygame.mouse.get_pressed()[0]:
        sd.display_h()
        sd.time.sleep(sd.pot1.read())
        sd.display_e()
        sd.time.sleep(sd.pot1.read())
        sd.display_l()
        sd.time.sleep(sd.pot1.read())
        sd.display_off()
        sd.time.sleep(0.25*sd.pot1.read())
        sd.display_l()
        sd.time.sleep(sd.pot1.read())
        sd.display_o()
        sd.time.sleep(1.2*sd.pot1.read())
        sd.display_off()
        sd.time.sleep(1.2*sd.pot1.read())
        sd.display_e()
        sd.time.sleep(sd.pot1.read())
        sd.display_r()
        sd.time.sleep(sd.pot1.read())
        sd.display_i()
        sd.time.sleep(sd.pot1.read())
        sd.display_c()
        sd.time.sleep(sd.pot1.read())
        sd.display_off()

    screen.fill((0, 0, 0))

    pygame.display.flip()

pygame.quit()
