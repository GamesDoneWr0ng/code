# The goal is to find the biggest non infinite weight steve can lift, and at what speed to find the amount of jouls this man producess
# Non infinite is to pervent cheap tricks like holding 2 waterbuckets. The gamerule infiniteWatersources will be disabled as well, but there are other tricks as well.
from decimal import Decimal, getcontext

getcontext().prec = 484

maxStack = 127 # itemstand trick for maxstack = 127, in 1.21+ the game crashes above 99

# one block of ice can turn into 1 block of water at the topp of the world and flow into quite a bit of water
height  = Decimal(384) # height over void
volume  = Decimal(0)   # start volume
columns = Decimal(4)   # coulumns of water for a given height

# first 2 steps are a little different
volume += height
height -= Decimal(1/8)
volume += height * columns
columns += 2
height -= Decimal(1/8)

while height > 0:
    volume += height * columns
    columns += 2
    height -= Decimal(1/8)

massIce = volume * 1000 # 1 m^3 of water is 1000 kg
massBlueIceStack = massIce * 81 * maxStack # 1 blue ice is 9*9 ice
massBarrel = massBlueIceStack * 27 # 27 slotts in a barrel

# You can copy barrels with their content and put it in another barrel, there is a limit to this which i belive is 127
massRecursiveBarrel = massBarrel * Decimal(27*maxStack)**127 # 27 slots * maxstack ^ max recursion depth

massInventory = massRecursiveBarrel * maxStack * 37 # 4*9 rows + offhand

# you can add netherite armor as well, but at this point i dont think it matters.
# This is the max weight possible in minecraft that i know of
print(massInventory, "kg")

# A bit under the observable universe if it had the density of a neutron star to the power of 5
# Insert your mom joke here.

# We will calculate the maximum acceleration
# I will not count /tp as that likely just creates a wormhole which is a easy task considering the mass he is carrying

# Measured the acceleration in the first tick of movement to:
# horizontal/X = 200744.003 m/s^2
# vertical/jump = 1151.999 m/s^2
# You can jump 10 times per second
acceleration_squared = Decimal("200744.003")**2 + (Decimal("1151.999") * 10)**2

# Force in newtons
force = massInventory * acceleration_squared**Decimal(0.5)
#print(force, "N")

# watts (and same number for joules)
# squared since its force * acceleration (/1s) and force is mass * acceleration. We want to remove the rounding error with root
power = massInventory * acceleration_squared # /20 * 20 = 1
print(power, "watts")