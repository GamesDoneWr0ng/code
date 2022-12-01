def convert(system):
    tall = [0, 12, 25, 52, 81]
    tegn = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
    for i in tall:
        result = ""
        n = 1
        while n < i:
            n *= system
    
        if n == 1:
            result += "0"
        while n != 1/system:
            if i-n >= 0:
                var = i // n
                result += tegn[int(var)]
                i = i-n*var
            else:
                result += "0"
            n = n/system
        print(result[1:]+f"({system})")
    print("")

convert(2)
convert(8)
convert(10)
convert(16)
