from collections import List

fn checkRace(time: Int, distance: Int) -> Int:
    var i = 1
    while (time-i) * i <= distance:
        i += 1
    return time+1 - 2*i

fn main():
    #var data: List[List[Int]] = List[List[Int]](List[Int](7,9), List[Int](15,40), List[Int](30,200))
    #var data: List[List[Int]] = List[List[Int]](List[Int](40,233), List[Int](82,1011), List[Int](84,1110), List[Int](92,1487))
    var data: List[List[Int]] = List[List[Int]](List[Int](40828492, 233101111101487))
    #var data: List[List[Int]] = List[List[Int]](List[Int](71530, 940200))

    var result: Int = 1
    for race in data:
        result *= checkRace(race[][0], race[][1])
    print(result)