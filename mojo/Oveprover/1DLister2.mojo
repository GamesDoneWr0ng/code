struct StrList:
    """
    List of strings takes a length and values in init function.\n
    Length is static, but StrList has __get_item__/__set_item__ functionality.
    """
    # reference ount for efficient copying
    var rc: Pointer[Int]

    var data: Pointer[StringLiteral]
    var length: Int

    fn __init__(inout self, length: Int, *values: StringLiteral):
        self.length = length
        self.data = Pointer[StringLiteral].alloc(self.length)
        self.rc = Pointer[Int].alloc(1)
        self.rc.store(1)
        for i in range(self.length):
            self.set(i, values[i])

    fn __copyinit__(inout self, other: Self):
        other._inc_rc()
        self.data = other.data
        self.rc = other.rc
        self.length = other.length
    
    fn __del__(owned self):
        self._dec_rc()

    @always_inline
    fn __getitem__(self, idx: Int) -> StringLiteral:
        return self.get(idx)

    @always_inline
    fn __setitem__(self, idx: Int, value: StringLiteral):
        self.set(idx, value)

    fn _get_rc(self) -> Int:
        return self.rc.load()
    
    fn _dec_rc(self):
        let rc = self._get_rc()
        if rc > 1:
            self.rc.store(rc - 1)
            return
        self._free()
    
    fn _inc_rc(self):
        let rc = self._get_rc()
        self.rc.store(rc + 1)
    
    fn _free(self):
        self.rc.free()
        self.data.free()

    @always_inline
    fn set(self, idx: Int, value: StringLiteral) -> None:
        self.data.store(self.length + idx if idx < 0 else idx, value)

    @always_inline
    fn get(self, idx: Int) -> StringLiteral:
        return self.data[self.length + idx if idx < 0 else idx]

struct IntList:
    # reference ount for efficient copying
    var rc: Pointer[Int]

    var data: Pointer[Int]
    var length: Int

    fn __init__(inout self, length: Int):
        self.length = length
        self.data = Pointer[Int].alloc(self.length)
        self.rc = Pointer[Int].alloc(1)
        self.rc.store(1)

    fn __init__(inout self, length: Int, *values: Int):
        self.length = length
        self.data = Pointer[Int].alloc(self.length)
        self.rc = Pointer[Int].alloc(1)
        self.rc.store(1)
        for i in range(self.length):
            self.set(i, values[i])

    fn __copyinit__(inout self, other: Self):
        other._inc_rc()
        self.data = other.data
        self.rc = other.rc
        self.length = other.length
    
    fn __del__(owned self):
        self._dec_rc()

    @always_inline
    fn __getitem__(self, idx: Int) -> Int:
        return self.get(idx)

    @always_inline
    fn __setitem__(self, idx: Int, value: Int):
        self.set(idx, value)

    fn _get_rc(self) -> Int:
        return self.rc.load()
    
    fn _dec_rc(self):
        let rc = self._get_rc()
        if rc > 1:
            self.rc.store(rc - 1)
            return
        self._free()
    
    fn _inc_rc(self):
        let rc = self._get_rc()
        self.rc.store(rc + 1)
    
    fn _free(self):
        self.rc.free()
        self.data.free()

    @always_inline
    fn set(self, idx: Int, value: Int) -> None:
        self.data.store(self.length + idx if idx < 0 else idx, value)

    @always_inline
    fn get(self, idx: Int) -> Int:
        return self.data[self.length + idx if idx < 0 else idx]

    fn count(self, value: Int) -> Int:
        var count: Int = 0
        for i in range(self.length):
            if self.get(i) == value:
                count += 1
        return count

    fn count(self, filter: fn(Int) -> Bool) -> Int:
        var count: Int = 0
        for i in range(self.length):
            if filter(self.get(i)):
                count += 1
        return count

    fn sort(self):
        var swapped: Bool = True
        while swapped:
            swapped = False
            for i in range(self.length - 2):
                if self.get(i) > self.get(i + 1):
                    let temp: Int = self.get(i)
                    self.set(i, self.get(i + 1))
                    self.set(i + 1, temp)
                    swapped = True
    
    fn max(self) -> Int:
        var result: Int = -2147483648
        for i in range(self.length):
            if self.get(i) > result:
                result = self.get(i)
        return result

    fn min(self) -> Int:
        var result: Int = 2147483647
        for i in range(self.length):
            if self.get(i) < result:
                result = self.get(i)
        return result


struct Set: # suports ints 1-128 for instant speed
    # reference count for efficient copying
    var rc: Pointer[Int]

    var data: Pointer[Int8]

    fn __init__(inout self, liste: IntList):
        self.rc = Pointer[Int].alloc(1)
        self.rc.store(1)

        self.data = Pointer[Int8].alloc(127)
        for i in range(127):    # why do i need this????
            self.data.store(i, 0)
        for i in range(liste.length):
            self.data.store(liste.get(i)-1, liste.get(i))

    fn __copyinit__(inout self, other: Self):
        other._inc_rc()
        self.data = other.data
        self.rc = other.rc
    
    fn __del__(owned self):
        self._dec_rc()

    fn __str__(self) -> StringLiteral:
        for i in range(127):
            if self.data[i] != 0:
                print(i+1)
        return ""

    fn _get_rc(self) -> Int:
        return self.rc.load()
    
    fn _dec_rc(self):
        let rc = self._get_rc()
        if rc > 1:
            self.rc.store(rc - 1)
            return
        self._free()
    
    fn _inc_rc(self):
        let rc = self._get_rc()
        self.rc.store(rc + 1)
    
    fn _free(self):
        self.rc.free()
        self.data.free()

    fn insert(inout self, key: Int) -> None:
        self.data.store(key-1, key)

    fn intersection(self, other: Set) -> None:
        for i in range(127):
            if self.data[i] != 0 and other.data[i] != 0: # why is != 0 needed
                print(i+1)

    fn difference(self, other: Set) -> None:
        for i in range(127):
            if self.data[i] ^ other.data[i] != 0: # mom look i used the ^
                print(i+1)
    

def main():
    let tall: IntList = IntList(20, 3,1,2,6,8,2,7,7,6,8,2,7,5,8,6,3,5,4,1,6)
    let ord: StrList = StrList(13, "xax", "er", "foff", "and", "em", "nu", "nei", "nuet", "nan", "momom", "sopp", "ost", "yax")

    print(tall.count(7))

    fn filter(x: Int) -> Bool:
        return (x >= 2 and x <= 5)

    #print(tall.count(filter))

    print()

    # c ord med 3 eller flere tegn
    for i in range(ord.length):
        if len(ord[i]) >= 3:
            print(ord[i])

    print()

    # d ord med 3 eller flere tegn
    for i in range(ord.length):
        let length: Int = len(ord[i])
        let data = ord[i].data()
        if length >= 3 and data.load(0) == data.load(length-1):
            print(ord[i])

    print()

    # 2
    let tall3: IntList = IntList(40, 89, 3, 89, 87, 46, 63, 54, 68, 15, 69, 27, 20, 68, 62, 25, 26, 74, 19, 96, 85, 56, 88, 98, 87, 1, 78, 24, 64, 64, 39, 14, 9, 1, 30, 18, 82, 41, 52, 77, 81)
    tall3.sort()
    print(tall3.get(0))
    print(tall3.get(-1))
    print(tall3.get(1))
    print(tall3.get(-2))

    print()

    # 3
    var tall1: IntList = IntList(41, 7, 24, 10, 26, 35, 10, 29, 2, 29, 29, 40, 40, 26, 16, 8, 9, 26, 5, 18, 9, 13, 40, 28, 37, 32, 6, 11, 35, 9, 26, 6, 11, 2, 10, 11, 27, 4, 8, 22, 40, 19)
    let tall2: IntList = IntList(38, 56, 49, 28, 52, 58, 33, 26, 27, 58, 36, 36, 48, 55, 25, 58, 57, 30, 27, 36, 39, 39, 58, 28, 56, 52, 21, 39, 22, 27, 48, 37, 20, 32, 38, 31, 25, 42, 54)
    
    let unik1: Set = Set(tall1)
    let unik2: Set = Set(tall2)

    print(unik1.__str__())
    print(unik2.__str__())

    unik1.intersection(unik2)

    print()

    unik1.difference(unik2)