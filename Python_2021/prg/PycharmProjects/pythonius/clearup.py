from os import path
from re import L  # allows for the tile map to be ported and converted easily

# basics started by devin
WIN_WIDTH = (2 * (640))
WIN_HEIGHT = (832)
FPS = 60

# basic player values started by devin
PLAYER_LAYER = 3

GRASS_LAYER = 4

BLOCK_LAYER = 2

GROUND_LAYER = 1

# ground layer is first, it will run first and be on screen first, player will be behind it

TILESIZE = 32  # controlls size of player and most on screen visuals
RED = (255, 0, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

main_folder_space = path.dirname(__file__)  # its a destination for tile_map.txt
tilemap = []
with open(path.join(main_folder_space, 'tile_map.txt'), "r") as f:
    for line in f:
        tilemap.append(line)

# tilemap = [                                     # done by devin
#     'BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB',
#     'B............................GGGGGGGG..B',
#     'B..P...................................B',
#     'B......................................B',
#     'B.................GGG..................B',
#     'B......................................B',
#     'B.........................GGG..........B',
#     'B......................................B',
#     'B.......G..............................B',
#     'B......GGGGG...........................B',
#     'B.......G..............................B',
#     'B.................GG...................B',
#     'B......................................B',
#     'B......................................B',
#     'B......................................B',
#     'B......................................B',
#     'B.................GGG..................B',
#     'B......................................B',
#     'B......................................B',
#     'B......................................B',
#     'B......................................B',
#     'B.............GG.......................B',
#     'B......................................B',
#     'B...........................GGG........B',
#     'B.......GGGGGG.........................B',
#     'BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB',

# ]


# movement variables, started by devin
PLAYER_SPEED = 3
