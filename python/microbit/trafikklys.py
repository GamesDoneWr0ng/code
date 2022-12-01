from microbit import *
import time

button = pin5
fRed = pin0
fGreen = pin1
bRed = pin8
bYellow = pin12
bGreen = pin2

def trykk(lastPress):
    sleep(1000)
    bGreen.write_digital(0)
    bYellow.write_digital(1)
    sleep(1000)
    bYellow.write_digital(0)
    bRed.write_digital(1)
    sleep(1000)

    fRed.write_digital(0)
    fGreen.write_digital(1)
    
    sleep(5000)

    fGreen.write_digital(0)
    fRed.write_digital(1)

    sleep(1000)
    
    bRed.write_digital(0)
    bYellow.write_digital(1)
    sleep(1000)
    bYellow.write_digital(0)
    bGreen.write_digital(1)

    lastPress = time.ticks_ms()
    return lastPress

lastPress = time.ticks_ms()

bGreen.write_digital(1)
fRed.write_digital(1)

while True:
    
    if button.read_digital() and time.ticks_diff(lastPress, time.ticks_ms()) < -10000:
        display.scroll(lastPress)
        lastPress = trykk(lastPress)
        
    