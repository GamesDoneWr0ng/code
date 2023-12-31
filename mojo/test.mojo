from testing import assert_false
from benchmark import keep
from time import sleep

fn main():
    sleep(30)
    var running: Int = 100
    var i: Int = 0
    print(i < running)
    while i < running:
        running += 2
        i += 1
        keep(i)
        keep(running)

    print(i < running, i, running)
    _=assert_false(i < running, "huh")