# Imports go at the top
from microbit import *
import random
import time

# Code in a 'while True:' loop repeats forever

while True:
    sleep(random.randint(3000, 10000))
    valg = random.randint(0,2)
    tid = time.ticks_ms()
    if valg:
        display.show("A")
    else:
        display.show("B")
    while True:
        if button_a.is_pressed():
            if valg:
                display.show(Image.HAPPY, 500)
                time.sleep_ms(500)
            else:
                display.show(Image.SAD, 500)
                time.sleep_ms(500)
            display.scroll(time.ticks_diff(time.ticks_ms(),tid))
            break
        if button_b.is_pressed():
            if valg:
                display.show(Image.SAD, 500)
                time.sleep_ms(500)
            else:
                display.show(Image.HAPPY, 500)
                time.sleep_ms(500)
            display.scroll(time.ticks_diff(time.ticks_ms(),tid))
            break
        
                