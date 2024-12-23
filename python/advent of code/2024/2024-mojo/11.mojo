from collections import Dict
from time import now

fn split(inout data: Dict[Int, Int]) raises -> None:#Dict[Int, Int]:
    var nextIter: Dict[Int, Int] = Dict[Int, Int](power_of_two_initial_capacity=len(data)*2)
    for i in data.keys():
        if i[] == 0:
            if 1 in nextIter:
                nextIter[1] += data[0]
            else:
                nextIter[1] = data[0]
         elif len(str(i[]))%2 == 0:
            var first: Int = int(str(i[])[ len(str(i[]))//2:])
            var last:  Int = int(str(i[])[:len(str(i[]))//2 ])
            if first in nextIter:
                nextIter[first] += data[i[]]
            else:
                nextIter[first] = data[i[]]
            if last in nextIter:
                nextIter[last] += data[i[]]
            else:
                nextIter[last] = data[i[]]
        else:
            if i[]*2024 in nextIter:
                nextIter[i[]*2024] += data[i[]]
            else:
                nextIter[i[]*2024] = data[i[]]
#    data.clear()
#    data.update(nextIter)
#    return nextIter
    data = nextIter^

fn main():
    var data: Dict[Int, Int] = Dict[Int, Int]()
    data[28]=1
    data[4]=1
    data[3179]=1
    data[96938]=1
    data[0]=1
    data[6617406]=1
    data[490]=1
    data[816207]=1
    var start: Int = now()
    for _ in range(1000):
        try:
            split(data)
        except:
            return
        #print(i)
    print((now() - start)/1e9)