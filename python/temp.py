def test():
    for i in range(10):
        print(i)
        yield

start = test()

for i in start:
    break

for i in start:
    break

for i in start:
    break