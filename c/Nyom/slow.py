from time import time
startTime = time()

i=0
while i < 1_000_000_000:
    i += 1

print("--- %s seconds ---" % (time() - startTime))