fn f(x: Float64) -> Float64:
    return x**2

fn main():
    var a: Float64 = 0
    var b: Float64 = 1
    var dx: Float64 = 2
    dx = dx**-32

    var c: Float64 = a
    var sum: Float64 = 0
    while c <= b:
        sum += f(c)*dx
        c += dx

    print(sum)