#! /usr/bin/env python3
# coding: utf-8

""" CONSTANT THIS GAME LOAD """
""" JUST CHANGE YOUR SIZE SCREEN """

WIDHT = 975                                                                               # Easy change this size screen
HEIGHT = 750                                                                              # Easy change this size screen

""" PYGAME CONSTANTS CONFIGURATION """
""" NO TOUCH THIS CONFIGURATION """
MAZE = 'maze_char.txt'                                                                              # The maze character
ZONE = []                                                                                      # stock of Maze structure
ITEM_LIST = []
WALL_LIST = []                                                                                  # The list position wall
PATH_LIST = []                                                                                    # Stock path positions
FINISH_LIST = []                                                                              # The list position finish
GUARDIAN_LIST = []                                                                          # The list position guardian

""" FRAME PER SECOND """
FPS = 30                                                                          # Frame per second (easily modifiable)

""" THE WINDOW SIZE """
WINDOW_SIZE = WIDHT, HEIGHT                                                               # This window size (L_x x H_y)
CENTER = (WIDHT // 2), (HEIGHT // 2)

""" THE CASE SCREEN IN SIZE """
X = 15                                                                                         # (HORIZONTAL, X = WIDHT)
Y = 15                                                                                           # (VERTICAL Y = HEIGHT)

""" THE SPRITE SIZE CONFIGURATION """
SPRITE = 1                                                                        # picture per case (easily modifiable)
SPRITE_WIDHT = X / SPRITE                                                                            # height of picture
SPRITE_HEIGHT = Y / SPRITE                                                                            # widht of picture
SPRITE_SIZE_WIDHT = int(WIDHT / SPRITE_WIDHT)                                                    # Sprite size x (widht)
SPRITE_SIZE_HEIGHT = int(HEIGHT / SPRITE_HEIGHT)                                                # Sprite size y (height)

""" THE CONSTANTS MOVEMENT CONFIGURATION """
MOVE_X = WIDHT / X                                                                            # The movement x direction
MOVE_Y = HEIGHT / Y                                                                           # The movement y direction
