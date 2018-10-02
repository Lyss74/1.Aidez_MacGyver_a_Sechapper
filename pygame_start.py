#! /usr/bin/env python3
# coding: utf-8

import pygame
from pygame.locals import *
import os

from config_pictures_sounds import *
from player import *


def main():
    """P YGAME START """
    pygame.init()                                                                               # Init the module Pygame
    running = True                                                                                # Control the end game

    """ THE SCREEN IS ONLY CENTERED POSITION """
    os.environ['SDL_VIDEO_CENTERED'] = '1'                                      # The screen blit only centered position

    window = pygame.display.set_mode(WINDOW_SIZE)                                        # Size configuration the window
    clock = pygame.time.Clock()                                                                      # Refresh animation
    pygame.display.set_caption("P3 : Aidez MacGyver")                                                 # The title window

    rect = pygame.Rect((0, 0), WINDOW_SIZE)                                                      # The border rect limit
    ConfigFiles.load()                                                                  # Load the picture configuration
    window.blit(ConfigFiles.scale['background'], (0, 0))               # Associate screen display and background display
    Maze(MAZE, ZONE, window, ConfigFiles.scale)                                            # Load and construct the Maze
    macgyver = Player(ConfigFiles.loaded['mac'])                                              # Load the Player animated

    """ ITEM CONFIGURATION """

    item_1 = Item(ConfigFiles.scale['loot1'])
    item_2 = Item(ConfigFiles.scale['loot2'])
    item_3 = Item(ConfigFiles.scale['loot3'])

    item_1.random_blit_item(window, item_1.position, ZONE)                                # The items randomise and blit
    item_2.random_blit_item(window, item_2.position, ZONE)                                # The items randomise and blit
    item_3.random_blit_item(window, item_3.position, ZONE)

    """ PYGAME LOOP """
    while running:                                                                          # Easy control the loop game
        delta_mms = clock.tick(FPS)                                          # Use the constants FPS (easily modifiable)
        delta_s = delta_mms / 1000.00                                                                    # Split the FPS
        for event in pygame.event.get():                                                          # The loop game system
            if event.type == QUIT:                                                              # The quit Game function
                running = False                                                             # Easy control the loop game
            elif event.type == KEYDOWN:                                                          # Command the quit game
                if event.key == K_ESCAPE:
                    running = False

                # if event.key == K_RIGHT or K_LEFT or K_UP or K_DOWN:
                    # macgyver.event_key(event)
                    # if macgyver.pos == (0, 0):
                        # window.blit(ConfigFiles.scale['start'], macgyver.rect)
                        # window.blit(ConfigFiles.scale['start'], macgyver.rect)
                    # else:
                        # window.blit(ConfigFiles.scale['start'], macgyver.rect)
                macgyver.event_key(event)

            window.blit(ConfigFiles.scale["path"], macgyver.rect)                  # Fix the bug the movement the player
            window.blit(macgyver.mac, macgyver.pos)                                           # blit and moving the hero

            Item.space_item(ZONE, item_1.position, item_2.position, item_3.position)    # Blit the new position the item

            Player.animated_blit(ZONE, macgyver.pos, ConfigFiles.scale, item_1.position, item_2.position,
                                 item_3.position, FINISH_LIST, window)                      # Auto add the item the list

            macgyver.syringe_assembly(macgyver.pos, ConfigFiles.scale,
                                      item_1, item_2, item_3, window)               # Automatically assembly the serynge

            macgyver.final_fight(macgyver.pos, GUARDIAN_LIST, window, ConfigFiles.scale)     # Mac vs Murdoc final fight

            Player.border_limit(macgyver, ZONE, rect)                                          # Limit the border screen
            pygame.display.update()                                                               # Update the animation


if __name__ == '__main__':
    main()