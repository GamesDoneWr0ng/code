import numpy as np
from copy import deepcopy
from typing import Self
data = """#############################################################################################################################################
#...........#.....#.........#...#...#.............#.....#.......#.........#.......#...#...#.......#...........#.....#.#...#.......#.....#..E#
#.#######.#.#.###.#.#.#.#.#.#.#.#.#.#####.#########.#.#.#.###.###.#####.#.###.###.#.#.#.#.#.###.###.###.#####.###.#.#.#.#.#.#.###.#.#.#.###.#
#...#...#.#.#.#...#.#.#...#.#.#...#.....#.........#.#.#.#.#...#...#.....#...#.#...#.#...#.#...#.#...#...#.#...#...#.#.#.#...#...#.#.#.#...#.#
###.###.#.#.#.#####.#.#####.#.#########.#.#######.#.#.#.#.#.#.#.###.#######.#.#.###.#.###.###.#.#.###.###.#.###.###.#.#.#######.###.#.###.#.#
#.#.#...#.#...#...#.#.#...#.#.#.........#...#.....#.#.#.#.#.#.#.#.#.#.....#.#.#.#...#...#.....#.#.#.#...#...#...#...#.#.....#.#.....#.#.#.#.#
#.#.#.#.#.###.#.#.#.#.#.#.#.#.#.#.###########.#.###.#.#.###.###.#.#.#.###.#.#.#.#.#####.#######.#.#.###.###.###.###.#.#####.#.#######.#.#.#.#
#.....#.#...#...#.#.#.#.#...#...#.#.......#...#.#...#.#...#.....#.#...#.#.#...#.#.....#...#.....#.#...#...#...#...#...#.....#.......#.#.#.#.#
###########.#.###.#.#.#.#######.#.###.###.#.#####.###.###.#.#####.#####.#.#####.###.#.###.#.#####.#.#.###.###.#.#.#####.#######.#####.#.#.#.#
#.....#...#.#...#...#.#...#.....#.....#...#.........#.#...#.......#.....#...#.#...#.#.#...#.......#.#.#...#...#.#.#...#...#...#.#.....#.#.#.#
#.###.#.#.#.#.#####.#.###.#.#.#.#######.###.#########.#.#########.#.#.#####.#.###.#.#.#.###########.#.#.###.###.#.#.#.###.#.#.#.#.#####.#.#.#
#...#.#.#.#...#...#.#.#...#.#.....#...#...#...#.....#.#.....#.....#.#...#...#.#...#.#.......#.......#.#...#.......#.#...#...#...#...#...#.#.#
###.#.#.#.###.#.#.###.#.#######.#.#.#####.#####.###.#.#####.#.#.#######.#.#.#.#.#####.#####.#.#######.###.#####.###.###.#######.###.###.#.#.#
#...#.#.#...#.#.#.#...#.........#.#...........#.#.#...#...#...#.........#.#...#.......#...#.......#...#.#...#.#.#...#.#.#.......#...#...#...#
#.###.#.###.###.#.#.#.#########.#.###########.#.#.#######.###.#########.#.#.#.#######.###.#####.#.#.###.###.#.#.#.###.#.#.#######.###.#####.#
#.....#...#...#.#.#.#.#.....#.....#.......#.....#...........#...#...#.#.#.#.#.......#...#.......#.#.......#.#...#.#...#...#.......#.........#
#.#.#.###.###.#.#.#.#.#.###.#######.#####.#########.#.#####.###.#.#.#.#.#.#.#######.###.#####.###.###.#####.#.###.#.#.#####.#.#####.#########
#.#.#...#...#...#.#.#.#...#...#...#.#.#...#...#...#.#.#.....#...#.#...#.#.#...#...#...#.....#...#.....#.....#...#...#.....#.#...........#...#
#.#.###.###.#.#.#.#.#####.###.#.#.#.#.#.#.#.#.#.#.#.#.###.###.###.#####.#.###.#.#####.#####.#######.###.#####.#########.###.#.#########.#.#.#
#.............#.#...#...#.#.....#.....#.#.#.#...#.#.#...#.#...#.#.......#...#.#.#.....#...#.......#.#...#.....#...#.....#...#.#.....#...#.#.#
#.#####.#.###.#.#.#.#.#.#.#.#########.#.###.#####.#####.#.#.###.#.#######.#.#.#.#.#####.#########.#.#.#####.###.#.#.#####.###.#.###.#.###.#.#
#.....#...#.#.#.#.#...#.#...#.#.....#.......#...#.#.....#.#...#...#.....#.#.#.......#...#.......#.#.#.....#.#...#.#...#...#.#.#.#.#.#.....#.#
#.###.#####.#.#.###.###.###.#.#.###.#########.#.#.#.#####.###.#.###.###.###.#.#####.#.#.#.#####.#.#######.###.###.#.#.#.###.#.#.#.#.#####.#.#
#...#.#.......#...#.#...#.....#.#.#...............#.#...#.#...#.#...#.#.....#.#...#...#.#.....#.#.....#...#...#...#.#.#.....#.#.#.#...#.....#
#####.#.#########.#.#.###.#####.#.#################.#.#.#.#.###.#.#.#.#######.#.#.#########.###.#####.#.###.###.#.#.#.#.#.#.#.#.#.#.#.###.###
#.....#.....#...#...#.....#.....#.....#.............#.#...#.#.....#.#.........#.#...#.....#.#...#.....#.#...#.#...#...#.#.#...#.#...#...#.#.#
#.#########.#.#.###.#######.#####.###.#.###.#.###.###.#####.#.#####.#.###.#.#.#.###.#.#.###.#.#.#.#####.#.###.#.###.#.#.#.#####.###.###.#.#.#
#.....#...#...#...#.......#.#.....#...#...#.....#.#.......#.#.#.....#...#...#.#...#...#...#.......#.......#...#.#.......#...#...#.....#.#.#.#
#####.#.#.#######.#########.#.#####.###########.#.#########.#.#.#############.###.#######.#.#######.#####.#.###.#.#####.###.#.###.#.###.#.#.#
#.....#.#.........#...#.....#.#...............#.#.......#...#.#.#...........#...#...#.....#.#.........#...#...#.#.....#.#.....#...#.....#...#
#.#######.#########.#.#.#####.#############.#.#########.#.###.#.#####.###.#.###.###.#.#####.#.#.#####.#.#####.#.#####.#.#####.#.###.#####.#.#
#...#...#.....#.....#...#.................#...#.......#.#...#.#.#.....#.............#.......#.#.....#.........#.....#.......#...#...#...#...#
#.#.#.#.#####.###.#######.###.###########.#.###.#####.#.###.###.#.#####.###.###.#.###.#######.#####.#########.#####.#.#####.###.#.#.#.#.#.###
#.#...#.....#...#.#.............#...#...#.#.......#.#...#.#.....#.#.........#.#.#.#.....#...#.....#.#.....#...#...#...#.#.....#.#.#...#.....#
###########.#.#.#.#.###########.#.#.#.#.#.#.###.#.#.###.#.#######.#######.#.#.#.#.#.###.#.#######.#.#.###.#.###.#.#####.#.#####.#.#.#####.#.#
#...#.....#.#.#...#...#.......#...#...#.#.#.....#.#...#.....#...#.........#.#...#...#.#.#.........#.#...#.#.........#...#...#...#.#.#.#.....#
#.#.#.###.#.#.###.#.###.#####.###########.###.###.#.#.#####.#.###.#.#.#####.###.#####.#.#######.###.###.#.#.#######.#.#.###.#.###.#.#.#.#.#.#
#.#...#...#.#.....#...#...#.......#.......#...#...#...........#...#...#...#.......#...#.......#.#.....#.#.#.#...#.....#...#.....#.#.#.#.#...#
#.#####.###.#.#####.#.#.#.#######.#.#######.###.###.#####.#####.#######.#.#####.#.###.#######.#.#.#.###.#.#.#.#.###########.#####.#.#.#.###.#
#.#...#.#.....#.....#.#.#...........#.....#.#.....#.....#...#...#...#...#.....#.#...........#.#...#.#...#.#.#.#...........#...#...#...#...#.#
#.###.#.#####.#.#####.#.###.###.#.#######.#.#####.#.###.###.#.#####.#.###.###.#.#############.#####.#.###.#.#.###########.###.#.#####.###.#.#
#...#.#...#...#.#...#.#.#.#.....#.#.....#.#.......#...#...#.#...#...#.#.....#.#.............#...#.#.#.#.#.#.#.#.......#.#.#...#.#.......#.#.#
###.#.#.#.#.#.#.###.#.#.#.#.#######.###.#.#######.###.###.#####.#.###.#.#.#.#.#############.###.#.#.#.#.#.###.###.###.#.#.#.###.#.#######.#.#
#...#.....#...#...#.#.#...#.#...#...#...#.....#.....#.#.#.......#.#.......#.#.....#...#...#...#.....#.#...#...#...#.....#.#...#...#...#...#.#
#.#####.#####.###.#.#.#####.#.#.#.###.#####.###.#####.#.#########.#.#####.#####.#.#.#.#.#.#.#.#.#####.#.###.###.#######.#.#.#######.#.#.###.#
#.....#.....#...#...#.....#.#.#.#...#.#...#.......#...#.......#...#.#...#...#...#...#.#.#.#.#.#.......#.....#.#.......#.#.#.#.....#.#.#...#.#
#.###.#####.#.###.#.#####.#.#.#.###.#.#.#.#.#######.###.#####.###.#.#.#.###.#.#######.#.#.#.#.#.#.###########.#.#####.###.#.#.###.#.#.###.#.#
#.#.#.....#.#.....#.#.#...#...#.#...#.#.#.#...#.....#...#...#.#...#...#.#...#...#...#...#.#.#.#...#.#.....#...#.#...#.......#...#...#...#.#.#
#.#.#####.#.###.###.#.#.#####.#.#.###.#.#.#####.#######.#.#.#.#.#######.#.#.###.###.#####.#.#######.#.###.#.#.#.#.#.#######.###.#######.#.#.#
#.#...#...#...#...#...#.......#...#.#...#...#...#.......#.#.#.#.......#...#...#...#.#.....#.............#...#.....#...#...#...#...#...#...#.#
#.###.#.#####.###.###.#####.#.#####.#######.#.#####.#####.#.#.#.#.###.###.#######.#.#.#####.#############.###########.#.#.###.#.#.#.#.#####.#
#...#.#...#.#.....#...#.#.......#.........#.#...#...#...#.#...#.#...#.....#...#...#...#...#...#.....#...#.#...#.....#.#.#.......#...#...#...#
###.#.###.#.###.#.#.###.#.#####.###.#.#####.###.#.#####.#.#.#.#.#.#.#######.#.#.#.#.###.#.###.###.#.#.#.#.###.#.###.#.#.#.#####.#####.#.#.###
#.#...#...#.....#.#...#.#.#...#.....#.#.......#.#...#...#.#...#...#.......#.#...#...#...#...#.....#.#.#.#.....#.#.#.#.#.#.....#.....#.#.#...#
#.###.#.###.#####.###.#.#.#.#.#####.#.#.###.###.###.#.#.#.###############.#.#########.#####.#######.#.#.#######.#.#.###.#####.#####.###.###.#
#.....#...#...#.....#.#.#...#.#...#...#.#...#...#...#.#.#.#.....#...#.....#...#...#...#...#.#.......#.#...#...#.#.#...#...#.#...#.#.....#...#
#.#######.###.###.###.#.#####.#.###.###.#####.###.###.###.#.#.###.#.#.#######.#.#.#.###.###.#.#######.###.#.#.#.#.###.#.#.#.###.#.#######.###
#...#...#.#.....#.....#...#...#.......#.....#.#...#.......#.#...#.#.#.#...#...#.#.#.#...#...#.#.......#...#.#...#.....#.#.#.....#...#.....#.#
###.#.#.#.#####.###.###.#.#.#.#.#####.#####.#.#.#.#.#########.#.#.#.#.###.#.###.#.#.#.#.#.#####.#.#.###.###.#####.#######.#.#####.###.#####.#
#.................#.....#...#.#.....#...#...#...#.#...#.....#.#...#.#.....#.#...#...#.#.#.......#.#...#...#.#...#.......#.#.....#...#.#.....#
#.#.#.#######.###.###.#######.#####.###.#.#######.###.#.###.#.#####.#.#.#.#.#.#######.###########.###.#.#.#.#.#.#######.#.#####.###.#.###.#.#
#.#...#.....#.#...#...#.....#.#...#...#.#...........#...#.#.#...#.#.....#.#.#...#...#...........#...#...#...#.#...#...#.#.....#...#.#.....#.#
#.#.#.#.###.#.#.#######.###.#.#.#.###.#.#####.#####.#####.#.###.#.#####.#.#.###.#.#.#.#####.###.###.#.#.#####.###.###.#.#####.###.#.#######.#
#...#...#.#.#.#...#.....#.....#.#.....#.....#.....#.......#...#.#.....#...#...#.#.#.#.#...#...#...#.#.#.#...#...#.....#.......#.#.#.......#.#
#####.###.#.#.###.#.#############.#####.###.#####.#.#########.#.#.#.#.#.#####.#.#.###.#.#.###.###.#.#.#.#.#.#.#.#.#############.#.#.#.###.#.#
#...#...#.....#...#.......#.....#.........#.....#.#.#.........#...#.#.#.#.....#.#.....#.#...#...#.#.#.#.#.#...#.#.#.....#.......#.#.#...#.#.#
#.#.#.#.#######.###.#####.###.#.#.#####.###.#####.#.#.###.#######.#.#.###.#####.#.#####.###.###.###.#.#.#####.#.###.###.#.#.#####.#.###.###.#
#.#...#.....#...#.......#.#...#.#.....#.#...#.......#.#...........#.#.....#...#.#.#.....#.#...#.#...#.#.....#.#...#...#...#.......#.........#
#.###.#####.#.###########.#.###.#####.###.###.#####.#.#.###########.#####.#.#.#.#.#.#.#.#.###.#.#.#########.#.###.###.#############.#.#.#####
#.#.........#.#...........#.#...#...#...#...#.......#.#.....#...#...#.....#.#...#.#...#.#...#...#.#.......#.#...#.#...#.....#...........#...#
#.###.#####.#.###.#########.#.###.#####.###.#####.###.#####.#.###.###.###.#.#####.#.#.#.###.#.###.#.#.###.#.###.#.#.#####.#.###########.#.#.#
#.........#.#.#...#.........#...#...........#.....#...#.....#.#...#...#.#.#.......#.#.#.......#...#.#...#.#.#.#.#.#.#.....#.......#.....#.#.#
#####.###.#.#.#.#####.#.#######.#############.#.###.###.#####.#.###.###.###.#.#####.#.#.#.#####.###.###.#.#.#.#.#.#.#.###########.#####.#.#.#
#.........#.#...#...#.#.#.....#.#...#.....#...#.#...#.#.......#.#.....#...#.#...#...#...#.......#...#...#...#.#.#...#.......#.....#.....#.#.#
#.###.#####.#####.#.#.#.###.###.#.#.#.###.#.#.###.###.#####.#.#.#.#######.#.###.#.#.###############.#.#######.#.#####.#####.###.###.###.#.#.#
#.......#.........#.#.#...#...#...#...#.....#.....#...........#.#...#...#...#...#...#.............#.#.#.....#...#.....#...#...#.....#.#.#...#
#.###.#.#.#.#.#####.###.#.#.#.#########.#######.###.###########.###.#.#.#####.#####.#.#######.#.#.###.#.###.#.###.#####.#.###.#######.#.#.#.#
#.#...#.#...#...#.....#.#.#.#...#.....#.#.......#...#...........#.....#.....#.....#.#.#.....#...#.....#...#.#.#.........#...#...#.........#.#
#.#.#.#.###.###.#####.#.#.#.###.#.#.###.#.#######.###.#####.#.###.#########.#####.#.#.#.###.#.#############.#.#########.#######.#######.###.#
#...#.#.............#.#.#.#.......#.....#.#.........#.#.#...#.......#.......#...#.#.#.#...#...#.........#...#.......#...#.....#...#.....#...#
###.###.#.#.#.#####.#.###.###.###.#######.###########.#.#.###########.#####.#.###.#.#.#.#.#.###.#######.#.#.###.###.###.#.###.#.#.#.#.#.#.#.#
#.....#.#.#.....#...#.....#...#.....#.....#...........#.#.#...........#...#.#.#...#.#...#.#...#.......#...#.#.....#...#.#.#.....#.....#...#.#
#.###.###.#####.#.###.#####.#.#.#####.#.###.###########.#.###.#########.###.#.#.#.#.###.#.###.#######.#####.#.###.###.#.#.#.#####.###.#.#.#.#
#...#...#.....#.#...#.#...#.#.#...#.......#.#...........#...#.........#.....#.#.#...................#.#...#...#...#...#...#.....#.#.......#.#
#.#.###.#.###.#.###.###.#.#.#####.#.###.#.#.#.#######.#.###.#.#.#.###.#.#####.#.#.#########.#######.#.#.#.###.#.###.#.###.#.###.###.#.###.#.#
#.#.#...#.#...#.#.#.#.....#.....#.#.....#...#.#.........#.#...#.#.#.#.#.......#.#.#.............#.#.#.#.#.......#...#...#...#.#.....#.....#.#
#.#.#.###.#.###.#.#.#.###.#####.#.###########.#.#.###.###.#######.#.#.#######.#.#.#.###.#######.#.#.#.#.###########.###.###.#.#######.#.#.#.#
#.#.#...#...#.#.#.#.#...#.....#.........#.....#.#...............#.#...#.......#.#.#.#.#...#...#...#...#.......#.....#.#.....#.#.........#.#.#
#.#.###.###.#.#.#.#.###.#####.#########.#.#####.###.###########.#.#####.#######.###.#.###.#.#.###.#.#.#######.#.###.#.#.#####.#.###.#.#.#.#.#
#.#...#.....#.#...#...#.....#.#...#...#...#.....#...#...#...#.....#...#.#...#.#.....#...#.#.#.#...#.#.....#.#...#...#...#...#...#.#.....#.#.#
#####.#######.#.#.#.#.#####.#.#.#.###.###.#.###.#.#.#.#.#.#.#####.#.#.#.#.#.#.#######.#.#.#.#.#####.#.###.#.#####.###.###.#.#.###.###.#.#.#.#
#...#.......#.#...#.#.#...#.#...#...#.....#.#.....#...#...#...#...#.....#.#.....#.....#...#.#...#...#.#.#.#...#...#.......#...#.......#...#.#
#.#.###.###.#.#.###.###.#.#.#######.#.#.#.#.###.###########.#.#.#.#.#####.#######.#########.###.#.###.#.#.###.#.#####.#.###.###.###.#.#.#.#.#
#.#.#.......#.#...#.....#.......#...#.#...#.#...#.........#.#.#.#...#.#.........#.....#...#.#.#...#.....#...#...#...#.........#...#.#...#.#.#
#.#.#.#.#####.#.#########.#######.#########.#.###.#######.###.#.#.###.#.#######.#####.#.#.#.#.#####.#######.#.###.#.#########.#####.#.#.#.#.#
#.#...#...#.....#.......#.#.#.....#...#.....#.#...#...........#.#.#.............#.....#.#...#.......#.......#.....#.........#.#.....#.#...#.#
#.#####.#.#####.#.#####.#.#.#.#####.#.#.#####.#.###############.#.#########.###.#.#####.#####.#######.#####################.#.#.#####.###.#.#
#.#...#.#.#...#.#.#.....#.#.#.#.....#.#.#...#.#.........#.......#.......#...#.#.#.....#.....#.#.....#.......#...............#...#...#.#.#...#
#.#.#.#.#.#.#.###.#.#####.#.#.#.#####.#.#.#.#.#########.###############.#.###.#.###.#.#.###.#.#.###.#######.#.#######.###########.#.#.#.#.#.#
#.#.#...#...#.#...#.#...#...#...#...#...................#.............#...........#.#.#...#.#...#...#.....#.#.......#.#...#.....#.#.#.#...#.#
#.#.###.#####.#.###.#.#.###.#####.#.#############.###.###.#####.###########.#####.#.#.#.#.#.#####.###.#.#.#.#.#####.#.###.#.#.#.#.#.#.###.#.#
#.......#...#...#.#...#.#.....#...#.#.......#...#...........#...#.........#.#...#...#...#...#...#...#.#...#...#.....#...#...#.#...#...#...#.#
#.###.#.#.#######.#####.#######.###.#.#####.#.#.#############.###.###.###.#.#.#.###.#########.#.###.#.#.#####.#.#.#####.#####.###.#####.#.#.#
#.#...#.#.....#.......#...#.......#.#.....#...#.#.....#.....#...#.#.....#...#.#.......#...#...#.....#.#.......#.#.....#.......#...#.....#.#.#
#.#.###.#.###.#.#.#######.#.###.###.#####.#####.#.###.#.###.###.#.###.#.#####.#####.#.###.#.#################.#.###.#.#########.###.#####.#.#
#.....#.#.....#.#...#.....#.........#...#.#...#...#.#.#...#...#.#...#.#...#...#.#.......#.#.#.............#...#.....#.....#.........#...#...#
#####.#.#.#####.###.#.###.#.#.#######.#.#.#.#.###.#.#.###.###.#.###.#.#.#.#.###.#.#####.#.#.#.###.#.#####.#.#.###########.#.#####.#.#.#.#.###
#.#.....#.....#.#...#.#...#.#.........#.#.#.#.......#...#.#.#.#.#...#.#.#.#.#...#.#.....#.#.#.#...#...#...#.#...........#.#...#.#.#...#.....#
#.#.###.#.#.#.#.#.#.#.#####.###########.#.#.###.#######.#.#.#.#.#.###.#.#.#.###.#.#####.#.#.###.#.#.###.###.#####.#.###.#.###.#.#.#.#.###.#.#
#.#.#.....#.#...#.#.#.#...#.......#...#...#...#.......#.#.#.....#...#...#.#.#...#.....#...#.#...#.#.....#.......#.#...#.....#...#.#...#...#.#
#.#.#.#.#.#####.#.###.#.#.#######.#.#.#######.#######.#.#.#####.###.###.#.#.#.#.#####.#.###.#.###.#.#####.#####.###.#.#.###.#####.#.###.#.###
#.#...#.#.....#.#.#...#.....#.......#...#...........#.#.#.....#...#...#.#.#...#.......#.#...#...#.#...#.#.#.....#.....#...#...#...#...#.#...#
#.#####.#.###.###.#.###.###.#.#########.#######.#####.#.#####.#.#####.###.###.#####.#.###.#.#.#.#.###.#.#.#.###.#.###.#######.#.###.#.#.#.#.#
#...#...#.........#.......#.....#.....#.....#...#...#.#...#...#.#.....#...#...#...#.#...#...#.#.#...#.#...#...#.#.#.#.#.....#.#.....#.#.#.#.#
#.###.#.#.#######.###########.###.###.#####.#####.#.#.###.#.#####.#####.###.###.#.#####.###.###.#.#.#.#.#####.#.#.#.#.#.###.#.#####.#.#.#.#.#
#...#.#...#...#.......#...#.....#.#...#...#.#.....#.....#.#.#...#.#.....#...#...#.........#.....#.#...#...#.#.#.#.#.#.#.#...#...............#
#.#.#.#.#.#.#.#########.#.#.###.#.###.###.#.#.###.#######.#.#.#.#.###.###.###.###########.#######.#######.#.#.#.#.#.#.#.#.#.#.#.#.#.#####.#.#
#.#.#.#...#.#...........#...#...#...#...#.....#...#.......#...#.....#.#...#.#...#.....#...#.....#...#...#.#.#.#.#.#.#...#.#...#.#.#.....#.#.#
#.#.#.#.###.#####.###########.#####.###.#.#########.#######.#######.#.#.###.###.#.#.#.#.###.###.###.#.#.#.#.#.###.#.#####.#.###.#.#.###.#.#.#
#.#.#.#.#.........#.................#.#.#...........#.#.....#.....#...#...#...#.#...#...#...#...#...#.#.#...#...#.#.....#.#.#...#.....#.#.#.#
#.#.#.#.#.###.#####.#.###.#########.#.#.#####.#######.#.#####.###.#######.###.#.#.#.#####.###.###.###.#.###.###.#.#####.#.#.###.###.#.#.#.#.#
#.#...#.#...#.#.....#...#...#.......#.........#.....#.#...#...#.#.....#.............#.#.....#...#...#.#...#.#.#.#.#.....#.#...#.......#.#...#
#.#####.###.#.#.#######.#####.#####.#.###########.#.#.###.#.###.#####.#.#####.###.#.#.#.###.###.###.#.###.#.#.#.#.#.#.#.#.###.#####.#.#.#.#.#
#.#.....#...#.#...#.....#.....#...#.#.#...#.......#.#...#.......#...#.#.#...#...#.#.#.#.#...#.....#...#.#.#...#.....#.#.....#.......#.#...#.#
#.#.#####.#######.#.###.#.###.#.###.###.#.###.#####.#.###.#####.#.###.#.#.#.#####.#.#.#.#.#.#.###.#####.#.###.#######.#.###.#######.#######.#
#...#...#.#.......#...#.#.#.....#...#...#...#.#.....#.#...#.....#...#...#.#.......#...#...#.#.#...#.....#.#.#.#.#.......#.........#.........#
#.###.#.#.#.#########.###.#.#.#.#.###.#####.#.#####.#.#.#.#.#.#####.#####.#######.#########.#.#.#####.###.#.#.#.#.#.###.#.#######.###########
#.#...#...#...#.....#...#.#.#...#.....#.....#.....#...#...#.#...#...#...#.#...#...#.................#...#.#.....#.#...#.#.#...#...#.........#
#.#.#.#.#####.#.#.#####.#.#.#.#########.#######.#.#######.#.#.#.#.#.#.###.###.#.###.#.#####.#.#.#.#.###.#.#####.#.###.#.#.#.#.#####.#####.#.#
#.#.#.#.#...#.#.#.....#...#.#.#...#...#...#...#.#.#.......#.#.#...#.#...#...#...#...#.......#.#...#.....#...#...#.#...#.#.#.#.....#...#...#.#
###.#.#.#.#.#.#.#####.#####.#.#.#.#.#####.#.#.#.#.#.#######.#.#####.###.###.###.#.###########.#########.###.#.###.#.###.###.#####.#.#.#.###.#
#...........#.#...#...#.....#...#...#.....#.#.#.#.....#...#...#...#.......#...#.#...#.#.....#.......#.....#.#...#.......#.......#...#.#.#...#
#.###.###.#.#.###.#.#.#.#####.#####.#.#####.#.###.#####.#.###.#.#########.###.#####.#.#.#.#########.#######.###.#.#######.#######.###.#.#####
#.#.....#.#...#.....#...#...#.......#.......#...#.#.....#.....#.#.........#...#.....#.#.#.....#.#...#.......#...#...........#...#...#.#.....#
#.###.###.#####.#########.###.#################.###.#####.#.#.#.#.#########.###.#####.#.###.#.#.#.###.#######.###############.#.###.#.#####.#
#.........#...#.#...#.........#...#.................#.....#.#...#.#.....#...#...#...#...#.#.#...#.....#.....#...........#.....#...#...#.....#
#.###.#####.#.#.#.#.#.#####.#.#.#.#.#.#########.#.###.#.#.#.#####.###.#.#.###.###.###.###.#.###.#######.#.###.###########.#######.#####.###.#
#.#.........#...#.#.#.#.......#.#...#.#...#...#.#...#.#.#.#.#.....#...#.#...#.#...........#.#...#.....#.#.....#...#...#...#.#...#...#...#.#.#
#.###.###########.#.#.###.###.#.#######.#.#.#.#####.###.#.#.#.#####.###.###.#.#############.#.###.###.#########.#.#.#.#.###.#.#.###.#.###.#.#
#S....#...........#.......#...#.........#...#...........#.#.........#.....#.................#.....#.............#...#...#.....#.......#.....#
#############################################################################################################################################"""

m = set()
start = 0+0j
end = 0+0j
for y, row in enumerate(data.split("\n")):
    for x, letter in enumerate(row):
        if letter == "#":
            continue
        pos = x+y*1j
        if letter == "S":
            start = pos
            m.add(pos)
            continue
        elif letter == "E":
            end = pos
            m.add(pos)
            continue
        m.add(pos)

class Node:
    def __init__(self, pos, dir, parrent, end=end):
        self.pos = pos
        self.dir = dir
        self.end = end
        self.parrents = [parrent]
        if parrent != None:
            if parrent.pos == self.pos:
                self.cost = parrent.cost + 1000
            else:
                self.cost = parrent.cost + 1
        else:
            self.cost = 0
    
    def fullCost(self):
        return self.cost + abs(self.end-self.pos)
    
    def open(self, m):
        nodes = []
        if self.pos + self.dir in m:
            nodes.append(Node(self.pos+self.dir, self.dir, self))
        if self.pos + self.dir*1j in m:
            nodes.append(Node(self.pos, self.dir*1j, self))
        if self.pos + self.dir*-1j in m:
            nodes.append(Node(self.pos, self.dir*-1j, self))
        return nodes

    def __le__(self, other: Self): return self.fullCost() <= other.fullCost()
    def __ge__(self, other: Self): return self.fullCost() >= other.fullCost()
    def __lt__(self, other: Self): return self.fullCost() < other.fullCost()
    def __gt__(self, other: Self): return self.fullCost() > other.fullCost()
    def __eq__(self, other: Self): 
        if other == None:
            return False
        return self.pos == other.pos and self.dir == other.dir
    def __str__(self):
        return f"{abs(self.pos.real)}+{abs(self.pos.imag)} {abs(self.dir.real)}+{abs(self.dir.imag)}"
    def __hash__(self):
        return hash(self.__str__())

def draw(path, m=m, b=data):
    for y in range(b.count("\n")+1):
        row = ""
        for x in range(b.find("\n")):
            p = x+y*1j
            if p not in m:
                row += "#"
            elif p in path:
                row += "O"
            else:
                row += " "
        print(row)

closed = dict()
opened = [Node(start, 1+0j, None)]
path = {start, end}
while True:
    index = np.argmin([i.fullCost() for i in opened])
    node = opened[index]
    opened.pop(index)
    nodes = node.open(m)
    for i in nodes:
        if i.pos == end:
            print(i.cost)
            layer = {i}
#            for k in opened:
#                if str(k) in closed and k.cost <= closed[str(k)].cost:
#                    closed[str(k)].parrents.extend(i.parrents)
            while True:
                nextLayer = set()
                for i in layer:
                    for p in i.parrents:
                        if p == None:
                            break
                        nextLayer.add(p)
                        path.add(p.pos)
                    else:
                        continue # not sure if this is cursed
                    break
                else:
                    layer = nextLayer
                    continue
                break
            print(len(path))
            draw(path)
            #draw({i.pos for i in closed})
            exit()
        if str(i) not in closed:
            for j in opened:
                if i == j:
                    j.parrents.extend(i.parrents)
                    break
            else:
                opened.append(i)
        else:
            if i.cost <= closed[str(i)].cost:
                closed[str(i)].parrents.extend(i.parrents)

    closed[str(node)] = node