#! /usr/bin/env python3
# coding: utf-8

import os
from constants import *


class Maze:
    """ CREATE THE MAZE - LEGHT 15 X 15 """

    def __init__(self, maze, zones, display, scale):
        """ LOAD THE STRUCTURE THE MAZE """

        self.read_maze(maze, zones)
        self.construct_maze(display, scale)
        self.file = MAZE

    def read_maze(self, maze, zones):
        """ USE THE OS MODULE FOR OPEN THE FILE TXT """
        path1 = os.path.join('asset')                                                                # Use the os method
        maze = os.path.join(path1, 'maze_char.txt')

        """ LOAD AND STOCK THE MAZE STRUCTURE """
        with open(maze, 'r', encoding='UTF-8') as file:
            structure = [zones.append(list(line)) for line in file]              # Intended list load and stock the Maze
        return maze, structure                                                                    # Return the maze read

    def construct_maze(self, display, scale):
        """ CONSTRUCT AND DISPLAY THE MAZE """
        for x in range(0, 15):
            for y in range(0, 15):
                if ZONE[x][y] == '#':
                    wallpos = (x * SPRITE_SIZE_WIDHT), (y * SPRITE_SIZE_HEIGHT)            # Pixelated position and size
                    poswall = (x, y)                                                   # Stock the wall position x and y
                    WALL_LIST.append(poswall)                                       # Add position in the constants list
                    display.blit(scale['wall'], wallpos)                 # Blit the picture wall compared stock position
                elif ZONE[x][y] == ' ':
                    pathpos = (x * SPRITE_SIZE_WIDHT), (y * SPRITE_SIZE_HEIGHT)
                    pospath = (x, y)
                    PATH_LIST.append(pospath)
                    display.blit(scale['path'], pathpos)                   # Repeat this operation for for other objects
                elif ZONE[x][y] == 'S':
                    startpos = (x * SPRITE_SIZE_WIDHT), (y * SPRITE_SIZE_HEIGHT)
                    display.blit(scale['start'], startpos)
                elif ZONE[x][y] == 'F':
                    endpos = (x * SPRITE_SIZE_WIDHT), (y * SPRITE_SIZE_HEIGHT)
                    posfinish = (x, y)
                    FINISH_LIST.append(posfinish)
                    display.blit(scale['finish'], endpos)
                elif ZONE[x][y] == 'G':
                    murpos = (x * SPRITE_SIZE_WIDHT), (y * SPRITE_SIZE_HEIGHT)
                    GUARDIAN_LIST.append(murpos)
                    display.blit(scale['murdoc'], murpos)
                    return x, y