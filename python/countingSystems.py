def convert(system):
    tall = [3141]
    tegn = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
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

convert(26)
convert(8)
convert(10)
convert(16)
