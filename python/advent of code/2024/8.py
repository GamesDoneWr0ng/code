data = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............"""

m = dict()
nodes = dict()
for y, row in enumerate(data.split("\n")):
    for x, letter in enumerate(row):
        pos = x + y*1j
        m[pos] = letter
        if letter != ".":
            if letter in nodes:
                nodes[letter].append(pos)
            else:
                nodes[letter] = [pos]

antinodes = set()
for f, positions in nodes.items():
    for node in positions:
        for otherNode in positions:
            if node == otherNode:
                continue
            dz = otherNode-node
            antiPos = node
            while antiPos-dz in m:
                antiPos-=dz
            while antiPos in m:
                antinodes.add(antiPos)
                antiPos += dz

print(len(antinodes))