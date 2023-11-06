from time import now

fn main():
    let start: Int = now()
    var i: Int = 0
    while i < 1_000_000_000_000_000_000:
        i += 1

    print(i, now() - start)