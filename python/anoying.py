# pip3 install pynput
# i terminal før du skjører koden

import webbrowser as a
import pynput as b
c,d,e,f,g='cRnNVgdeoFØ"QM0IdLaQLS+OÆMgs','8t7tyuef','ABCDEFGHIJKLMNOPQRSTUVWXYZÆØÅabcdefghijklmnopqrstuvwxyzæøå .,?-_;:+1234567890"/','8t7tyuef',''
h,i=len(f),len(e)
for j, l in enumerate(c):
    k = e.find(l) 
    m = e.find(f[j % h])
    n = (k - m) % i
    g += e[n]
a.open(g)
while True:
    b.keyboard.Controller().press(b.keyboard.Key.down)