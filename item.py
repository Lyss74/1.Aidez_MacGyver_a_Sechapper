#! /usr/bin/env python3
# coding: utf-8

import pygame
import random

from config_pictures_sounds import *
from the_maze import *


class Item:
    """ THE ITEM CLASS, CREATE THE OBJECT, AND BLIT IN THE RANDOM POSITION """

    def __init__(self, item):
        """ CREATION OF ITEM """
        self.loot = pygame.transform.scale(item, (SPRITE_SIZE_WIDHT, SPRITE_SIZE_HEIGHT))             # Size the picture
        self.item_rect = item.get_rect()                                                            # Create this object

        self.position = (0, 0)                                                                       # Init the position
        self.generate_position()                                       # Automatically generate the position this object
        self.x, self.y = self.position                                          # Separate the x and y position for blit
        self.dropped = False

    def generate_position(self):                                                 # Choose just one position in PATH_LIST
        """ RANDOMISE THE POSITION THE OBJECTS """
        self.position = random.choice(PATH_LIST)
        return self.position                                                                  # Return the item position

    def random_blit_item(self, display, x, y):                                # Pixelize the picture and blit the object
        """ PIXELIZE THE PICTURE AND BLIT IN THE POSITION """
        self.position = (self.x * SPRITE_SIZE_WIDHT, self.y * SPRITE_SIZE_HEIGHT)
        display.blit(self.loot, self.position)
        return self.position                                                                  # Return the item position

    def space_item(self, item1, item2, item3):
        """ PREVENTS THE DOUBLE FOR ITEM POSITION """
        if item1 == item2:
            if item1 == item3:                                          # Prevents the double item for the same position
                random.choice(PATH_LIST)
            random.choice(PATH_LIST)

        if item2 == item1:
            if item2 == item3:                                          # Prevents the double item for the same position
                random.choice(PATH_LIST)
            random.choice(PATH_LIST)

        if item3 == item1:
            if item3 == item2:                                          # Prevents the double item for the same position
                random.choice(PATH_LIST)
            random.choice(PATH_LIST)
        return item1, item2, item3                                                            # Return the item position
