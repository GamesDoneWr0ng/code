import sympy
 
# Klima on Venus
 
def temperatureAt(layers):
    S = 652.5 # Energy from the sun
    sigma = 5.67e-8  # Stefan-Boltzmann constant
    albedo = 0.75
    #layers = 100 # More layers give more accuracy
 
    # Define the symbols for the temperature variables T_0 is the ground
    T_n = [sympy.Symbol(f'T_{n}', positive=True, real=True) for n in range(layers)]
 
    # Define the equations for the temperature variables
    equations = []
 
    equations.append(S + sigma*T_n[1]**4 -(S*albedo + sigma*T_n[0]**4))
 
    for n in range(1, len(T_n)-1):
        # Add the equation for the temperature variable T
        equations.append(sigma*T_n[n-1]**4 +sigma*T_n[n+1]**4 - 2*sigma*T_n[n]**4)
 
    equations.append(sigma*T_n[-2]**4- 2 *sigma*T_n[-1]**4)

    return sympy.nsolve(equations, T_n, [231.597766315292*(layers-i)**0.25 for i in range(layers)])#, [231.6*layers**0.25 for i in range(layers)])

#values = []
#for i in range(3, 100):
#    print(i)
#    values += list(temperatureAt(i))

#print(str(values).replace(", ", "], ["))
print(temperatureAt(93))