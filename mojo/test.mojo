from testing import assert_false

fn main():
    var running: Int = 100
    var i: Int = 0
    while i < running:
        running += 2
        i += 1

    _=assert_false(i < running, "huh")