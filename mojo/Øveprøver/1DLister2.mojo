#struct StrListe


struct IntListe:
    # reference ount for efficient copying
    var rc: Pointer[Int]

    var data: Pointer[Int]
    var lenght: Int

    # mojo does not yet allow for 
    fn __init__(inout self, lenght: Int):
        self.lenght = lenght
        self.data = Pointer[Int].alloc(self.lenght)
        self.rc = Pointer[Int].alloc(1)
        self.rc.store(1)

    fn __copyinit__(inout self, other: Self):
        other._inc_rc()
        self.data = other.data
        self.rc = other.rc
        self.lenght = other.lenght
    
    fn __del__(owned self):
        self._dec_rc()

    fn __str__(self) -> String:
        print("e")
        var string: String = ""
        for i in range(self.lenght):
            string += self.get(i)
        return string

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
        self.data.store(self.lenght + idx if idx < 0 else idx, value)

    @always_inline
    fn get(self, idx: Int) -> Int:
        return self.data[self.lenght + idx if idx < 0 else idx]

    fn count(self, value: Int) -> Int:
        var count: Int = 0
        for i in range(self.lenght):
            if self.get(i) == value:
                count += 1
        return count

    fn count(self, filter: fn(Int) capturing -> Bool) -> Int:
        var count: Int = 0
        for i in range(self.lenght):
            if filter(self.get(i)):
                count += 1
        return count

    fn sort(self):
        var swapped: Bool = True
        while swapped:
            swapped = False
            for i in range(self.lenght - 2):
                if self.get(i) > self.get(i + 1):
                    let temp: Int = self.get(i)
                    self.set(i, self.get(i + 1))
                    self.set(i + 1, temp)
                    swapped = True
    
    fn max(self) -> Int:
        var result: Int = -2147483648
        for i in range(self.lenght):
            if self.get(i) > result:
                result = self.get(i)
        return result

    fn min(self) -> Int:
        var result: Int = 2147483647
        for i in range(self.lenght):
            if self.get(i) < result:
                result = self.get(i)
        return result

    #fn pop(self, idx: Int) -> Int:
    #    let value: Int = self.get(idx)
#
#
    #    self.data.free(1)
    #    return value


    #fn append(self, value: Int, idx: Int = -1) -> None:
    #    self.lenght += 1
    #    self.data.alloc(1)
    #    self.data.store(self.lenght + 1 - idx if idx < 0 else idx, value)

    #fn copy(self) -> Self:
    #    raise NotImplementedError


def main():
    let tall = IntListe(20)
    #(3,1,2,6,8,2,7,7,6,8,2,7,5,8,6,3,5,4,1,6)
    # jeg fant ingen måte å iterere gjennom ellementer
    tall.set(0, 3)
    tall.set(1, 1)
    tall.set(2, 2)
    tall.set(3, 6)
    tall.set(4, 8)
    tall.set(5, 2)
    tall.set(6, 7)
    tall.set(7, 7)
    tall.set(8, 6)
    tall.set(9, 8)
    tall.set(10, 2)
    tall.set(11, 7)
    tall.set(12, 5)
    tall.set(13, 8)
    tall.set(14, 6)
    tall.set(15, 3)
    tall.set(16, 5)
    tall.set(17, 4)
    tall.set(18, 1)
    tall.set(19, 6)

    #var ord  = ["xax", "er", "foff", "and", "em", "nu", "nei", "nuet", "nan", "momom", "sopp", "ost", "yax"]
    print(tall.count(7))

    fn filter(x: Int) -> Bool:
        return (x >= 2 and x <= 5)

    #print(tall.count(lambda x: if x >= 2 and x <= 5))
    print(tall.count(filter))
    print()

    # 2
    tall.sort()
    print(tall.get(0))
    print(tall.get(-1))
    print(tall.get(1))
    print(tall.get(-2))