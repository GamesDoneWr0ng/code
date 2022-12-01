from microbit import *
import random

screen = ["00000:",
          "90000:",
          "00000:",
          "00000:",
          "00000:"]
x = 1
count = 0

def addBeam(x):
    screen = ["00000:",
              "00000:",
              "00000:",
              "00000:",
              "00000:"]
    new = []
    y = random.randint(0,3)
    for index, i in enumerate(screen):
        if index != y and index != y+1:
            new.append(i.replace("9","0").replace("0:", "9:"))
        else:
            new.append(i)
    new[x] = "9"+new[x][1:]
    return new
            
            
while True:
    if count == 0:
        screen = addBeam(x)
        count = 4
    count -= 1
    
    screen[x] = "0" + screen[x][1:]
    if button_a.get_presses():
        if x < 5:
            x -= 1
    else:
        x += 1
        if x < 0:
            display.show(Image.SAD)
            sleep(10000)
    screen[x] = "9" + screen[x][1:]

    if "99" in screen[x]:
        display.show(Image.SAD)
        sleep(10000)

    new = []
    for i in screen:
        new.append(i.replace("09", "90"))
    screen = new

    display.show(Image("".join(screen)))
    sleep(500)