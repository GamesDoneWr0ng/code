fn main() raises:
    print("Oppgave1: \n")

    def summer(tall1: Int, tall2: Int) -> None:
        let sumen: Int = tall1 + tall2
        print(sumen)

    summer(4,5)



    print("\n\nOppgave2: \n")

    var ord: StringLiteral = "funksjon"

    def minFunksjon(tekst: StringLiteral) -> StringLiteral:
        let ord: StringLiteral = tekst                     # ord er utenfor scope så en ny en blir lagd
        return ord

    print(minFunksjon('hei'))
    print(ord)

    
    
    print("\n\nOppgave3: \n")

    def arealTrekant(grunnlinje: Float32, hoyde: Float32) -> Float32:
        return grunnlinje * hoyde / 2

    print("Arealet av trekanten blir:", arealTrekant(7,3))



    print("\n\nOppgave4: \n")

    from random import random_si64 # import random random_si64 is like randint. Always uses the seed 1 unless specifyed.
    from utils.vector import DynamicVector # import DynamicVector basicly a list but mojo doesent have a good implementation of lists yet

    fn generateNumbers() -> DynamicVector[Int64]:
        """Generate the 7 winning numbers and the extra number."""
        var numbers: DynamicVector[Int64] = DynamicVector[Int64]() # Initialize the numbers Vector
        while len(numbers) < 8:                     # while we still need more numbers
            let number: Int64 = random_si64(1, 34)  # Generate a random number
            var duplicate = False                   # Check for fuplicate
            for i in range(len(numbers)):           # loop through previously generated numbers
                if numbers[i] == number:            # if there is a match we need to make a new number
                    duplicate = True                # set duplicate to True
                    break                           # exit the search for a duplicate
            if duplicate:                           # if there was a duplicate
                continue                            # go back and make a new number
            
            numbers.push_back(number) # add the number to the List

        return numbers # return the numbers

    fn getCupon(winner: DynamicVector[Int64]) -> String:
        """Gets a lotto cupon input is not suported so sets it to 1..7"""
        var cupon: DynamicVector[Int64] = DynamicVector[Int64]()    # Initialises the cupon
        for i in range(7):                                          # loop 0..6
            cupon.push_back(i+1)                                    # append i+1 to the back

        # counts amount of correct numbers
        var count: Int = 0                  # Initialises the count to 0
        for i in range(len(cupon)):         # for each number in the cupon
            for k in range(len(winner)-1):  # loop through each number in the winning numbers -1 since last number is extra
                if cupon[i] == winner[k]:   # check for match
                    count += 1              # If match add to count
                    break                   # already found a match for this number go to next number in cupon

        # check extra number
        var extra: Int = 0
        for i in range(len(cupon)):         # for each number in cupon
            if cupon[i] == winner[-1]:      # if extra number matches
                extra = 1                   # update extra
                break                       # extra is found exit loop
        
        return String(count) + " + " + String(extra) # return the points as Sting

    fn factorial(n: Int) -> Float64:
        """Returns the factorial of the numbers."""
        var summen: Float64 = 1 # Initialises the sum
        for i in range(2, n+1): # for each number up to n
            summen *= i # multiply the sum by the number

        return summen
    #from math.math import factorial # only returns 5040? #

    fn posibleCombinations() -> Float64:
        """Returns the amount of posible lotto combinations by using some math."""
        return factorial(34) / (factorial(7) * factorial(27))


    let winner: DynamicVector[Int64] = generateNumbers() # Generates the winning numbers
    for i in range(len(winner)):
        if i < len(winner)-1: # Printer første 7 tallene i listen
            print("Winner tall", String(i+1)+":", winner[i]) # prints the winning numbers DynamicVector[Int64] doesn't have a __str__ method
        else:
            print("Ekstra tall:", winner[i]) # Ekstratallet
    
    print("\nAntall riktige:", getCupon(winner)) # Gets the cupon input is not suported so sets it to range(1,8)

    print("\nPosible combinations:", posibleCombinations()) # Gets the amount of posible lotto combinations.