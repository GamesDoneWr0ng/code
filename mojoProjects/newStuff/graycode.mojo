fn step(mut seen: List[List[Int]], read length: Int, read last: Int = 0, read current: Int = 2) -> None:
    if current == 2**length:
        for i in seen:
            for j in i:
                print(j, end=" ")
            print()
        return

    if last != 0:
        for i in range(length):
            seen[current][i] = seen[current-1][i]
        seen[current][last-1] ^= 1
        
        var new: Bool = True
        for i in range(current):
            if seen[i] == seen[current]:
                new = False
                break
        if new:
            step(seen, length, last-1, current+1)
    
    if last != length-1:
        for i in range(length):
            seen[current][i] = seen[current-1][i]
        seen[current][last+1] ^= 1
        
        var new: Bool = True
        for i in range(current):
            if seen[i] == seen[current]:
                new = False
                break
        if new:
            step(seen, length, last+1, current+1)

def main():
    var length: Int = 1
    while True:
        print(length)
        var seen: List[List[Int]] = List[List[Int]](length=2**length, fill=List[Int](length=length, fill=0))
        seen[1][0] = 1
        step(seen, length)
        length += 1