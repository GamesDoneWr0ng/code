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
        elif letter == "E":
            end = pos
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
    
    def __hash__(self):
        return hash(f"{self.pos} {self.dir}")

closed = dict()
opened = [Node(start, 1+0j, None)]
while len(opened) != 0:
    node = opened[0]
    if node not in closed:
        closed[node] = node.cost
        opened.extend(node.open(m))

    opened.pop(0)

minCost = np.inf
for i in closed.keys():
    if i.pos == end and i.cost < minCost:
        minCost = i.cost
print(minCost)