#! /usr/bin/env python3
# coding: utf-8

import time
from pygame_start import *
from item import *
from constants import *


class Player:
    """ PLAYER CREATION AND CONFIGURATION """

    def __init__(self, ressource):
        """ CREATING THE HERO """
        self.mac = pygame.transform.scale(ressource, (SPRITE_SIZE_WIDHT, SPRITE_SIZE_HEIGHT))
        self.rect = ressource.get_rect(topleft=(0, 0))
        self.pos = (0, 0)
        self.inventory = 0

    def moving(self, position, move):
        """ MOVE THE PLAYER """
        px, py = position                                                  # Define the mouvement the hero case per case
        mx, my = move
        position = (px + mx, py + my)
        return position                                                                            # Return the position

    def border_limit(self, macgyver, zone):
        """ LIMITE THE SURFACE GAME BORDER """                                                 # Limit the screen border
        X, Y = self.pos
        WIDHT, HEIGHT = self.rect.size                                                       # Use the rectangle picture

        if X < zone.left:
            X = zone.left
        elif X + WIDHT > zone.right:
            X = zone.right - SPRITE_SIZE_WIDHT

        if Y < zone.top:
            Y = zone.top
        elif Y + HEIGHT > zone.bottom:
            Y = zone.bottom - SPRITE_SIZE_HEIGHT

        self.pos = (X, Y)                                                                     # Init the player position
        self.rect.topleft = (X, Y)                                                              # Init the rect position
        return X, Y                                                                  # Return constants X and Y position

    def animated_blit(self, mac, scale, item_1, item_2, item_3, finish, display):
        """ LIST OF PICK-UP ITEM """
        if mac == item_1:                                                                   # Auto list item find needle
            display.blit(scale['loot1'], (715, 0))                                                  # List the item find

        elif mac == item_2:
            display.blit(scale['loot2'], (780, 0))                                                  # List the item find

        elif mac == item_3:
            display.blit(scale['loot3'], (845, 0))                                                  # List the item find

        elif mac == finish:                                                          # Define the victory or defeat game
            print('FINISH', FINISH_LIST)
            
        return item_1, item_2, item_3

    def syringe_assembly(self, mac, scale, item_1, item_2, item_3, display):
        """ ANIMATED BLIT ITEM """
        if mac == item_1.position and item_1.dropped == False:
            self.inventory += 1
            item_1.dropped = True

        if mac == item_2.position and item_2.dropped == False:
            self.inventory += 1
            item_2.dropped = True

        if mac == item_3.position and item_3.dropped == False:
            item_3.dropped = True
            self.inventory += 1

        if self.inventory == 3:
            display.blit(scale['wall'], (715, 0))
            display.blit(scale['wall'], (780, 0))
            display.blit(scale['wall'], (845, 0))
            display.blit(scale['finalloot'], (780, 0))                                       # Auto assembly the serynge
            return item_1, item_2, item_3

    def final_fight(self, mac, murdoc, display, scale):
        """ DEFINE THE VICTORY OF THE GAME """
        murdoc = (910, 650)                                                 # Define the victory game in the step finish
        if mac == murdoc:

            if self.inventory == 3:
                display.blit(scale['wingame'], (195.0, 150.0))
                pygame.display.update()                                                           # Update the animation
                time.sleep(1)
                quit()
            else:
                display.blit(scale['overgame'], (195.0, 150.0))
                pygame.display.update()                                                           # Update the animation
                time.sleep(1)
                quit()
            return self.inventory

    def event_key(self, events):
        """ ACTION AND MOVEMENT OF THE KEYS """
        X, Y = self.pos                                                                              # Init the position
        X = (X // MOVE_X)
        Y = (Y // MOVE_Y)                                                                         # Convert the movement

        if events.type == KEYDOWN:
            if events.key == K_RIGHT:
                newpos = (X + 1, Y)                                                            # Look the position X + 1
                if newpos not in WALL_LIST:                          # Compare the player position and the wall position
                    self.pos = self.moving(self.pos, (+MOVE_X, 0))                   # Autaurized the movement only path

            elif events.key == K_LEFT:
                newpos = (X - 1, Y)                                                            # Look the position X - 1
                if newpos not in WALL_LIST:
                    self.pos = self.moving(self.pos, (-MOVE_X, 0))

            elif events.key == K_UP:
                newpos = (X, Y - 1)                                                            # Look the position Y - 1
                if newpos not in WALL_LIST:
                    self.pos = self.moving(self.pos, (0, -MOVE_Y))

            elif events.key == K_DOWN:
                newpos = (X, Y + 1)                                                            # Look the position Y + 1
                if newpos not in WALL_LIST:
                    self.pos = self.moving(self.pos, (0, +MOVE_Y))

        elif events.type == KEYUP:

            if events.key == K_RIGHT and events.key == K_LEFT and events.key == K_UP and events.key == K_DOWN:
                self.pos = self.moving(self.pos, (0, 0))
        return self.pos                                                                            # Return the position
