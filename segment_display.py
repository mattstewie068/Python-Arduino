import time
import pyfirmata


uno = pyfirmata.Arduino('COM5')

it = pyfirmata.util.Iterator(uno)
it.start()

# assign pins and pin state to labels
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


def display_a():
    led_a.write(0)
    led_b.write(0)
    led_c.write(0)
    led_d.write(1)
    led_e.write(0)
    led_f.write(0)
    led_g.write(0)


def display_b():
    led_a.write(0)
    led_b.write(0)
    led_c.write(0)
    led_d.write(0)
    led_e.write(0)
    led_f.write(0)
    led_g.write(0)


def display_c():
    led_a.write(0)
    led_b.write(1)
    led_c.write(1)
    led_d.write(0)
    led_e.write(0)
    led_f.write(0)
    led_g.write(1)


def display_d():
    led_a.write(0)
    led_b.write(0)
    led_c.write(1)
    led_d.write(0)
    led_e.write(0)
    led_f.write(0)
    led_g.write(0)


def display_e():
    led_a.write(0)
    led_b.write(1)
    led_c.write(0)
    led_d.write(0)
    led_e.write(0)
    led_f.write(0)
    led_g.write(1)


def display_f():
    led_a.write(0)
    led_b.write(1)
    led_c.write(0)
    led_d.write(1)
    led_e.write(0)
    led_f.write(0)
    led_g.write(1)


def display_g():
    led_a.write(0)
    led_b.write(0)
    led_c.write(0)
    led_d.write(0)
    led_e.write(0)
    led_f.write(0)
    led_g.write(1)


def display_h():
    led_a.write(0)
    led_b.write(0)
    led_c.write(0)
    led_d.write(1)
    led_e.write(0)
    led_f.write(1)
    led_g.write(0)


def display_i():
    led_a.write(1)
    led_b.write(0)
    led_c.write(1)
    led_d.write(1)
    led_e.write(1)
    led_f.write(1)
    led_g.write(0)


def display_j():
    led_a.write(1)
    led_b.write(0)
    led_c.write(1)
    led_d.write(0)
    led_e.write(1)
    led_f.write(1)
    led_g.write(0)


def display_l():
    led_a.write(0)
    led_b.write(1)
    led_c.write(1)
    led_d.write(0)
    led_e.write(0)
    led_f.write(1)
    led_g.write(1)


def display_o():
    led_a.write(0)
    led_b.write(0)
    led_c.write(1)
    led_d.write(0)
    led_e.write(0)
    led_f.write(0)
    led_g.write(0)


def display_r():
    led_a.write(0)
    led_b.write(1)
    led_c.write(1)
    led_d.write(1)
    led_e.write(0)
    led_f.write(0)
    led_g.write(0)


def display_error():
    display_e()
    time.sleep(1)
    display_r()
    time.sleep(1)
    display_off()
    time.sleep(1)
    display_r()
    time.sleep(1)
    display_o()
    time.sleep(1)
    display_r()
    time.sleep(1)
    display_off()


def display_char(i):
    """displays on 7 segment LED display number that is specified"""
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


def switch_1_state():
    """returns the state of switch 1"""
    switch1_value = switch_1.read()
    return switch1_value


def switch_2_state():
    """returns the state of switch 2"""
    switch2_value = switch_2.read()
    return switch2_value


def switch_3_state():
    """returns the state of switch 3"""
    switch3_value = switch_3.read()
    return switch3_value


def switch_4_state():
    """returns the state of switch 4"""
    switch4_value = switch_4.read()
    return switch4_value


def pot_1_state():
    """returns the state of potentiometer 1"""
    pot1_value = pot1.read()
    return pot1_value


display_error()
display_char(4)
time.sleep(1)
display_char(0)
time.sleep(1)
display_char(4)
time.sleep(1)
display_off()
