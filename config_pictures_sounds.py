#! /usr/bin/env python3
# coding: utf-8

from pygame_start import *
from constants import *


class ConfigFiles:
    """ THIS CONFIGURATION LOADING THE PICTURE THE GAME """

    def __init__(self):
        """ NO USE THE __init__, THIS CLASS USE CLASSMETHOD """
        pass

    @classmethod                                                                                  # Use the class Method
    def cross_sprite(cls, file):                                                            # The cross plateform sprite
        """ CROSS PLATFORM JOIN TO SPRITE FILE """
        path1 = os.path.join('asset')
        sprite = os.path.join(path1, 'Sprites_cfg', file)
        return sprite                                                                            # Return the cross path

    @classmethod
    def load(cls):
        """ CONFIGURING PICTURE CHARGE AND DISPLAY """
        cls.loaded = {'background': pygame.image.load(cls.cross_sprite('background.png')).convert(),
                      # Load and convert picture
                      'wall': pygame.image.load(cls.cross_sprite('wall.png')).convert(),
                      'path': pygame.image.load(cls.cross_sprite('path.png')).convert(),
                      'start': pygame.image.load(cls.cross_sprite('start.png')).convert_alpha(),
                      'finish': pygame.image.load(cls.cross_sprite('finish.png')).convert_alpha(),
                      'murdoc': pygame.image.load(cls.cross_sprite('guard.png')).convert(),
                      'mac': pygame.image.load(cls.cross_sprite('macGyver.png')).convert_alpha(),
                      'loot1': pygame.image.load(cls.cross_sprite('loot1.png')).convert_alpha(),
                      'loot2': pygame.image.load(cls.cross_sprite('loot2.png')).convert_alpha(),
                      'loot3': pygame.image.load(cls.cross_sprite('loot3.png')).convert_alpha(),
                      'finalloot': pygame.image.load(cls.cross_sprite('finalLoot.png')).convert_alpha(),
                      'wingame': pygame.image.load(cls.cross_sprite('win.png')).convert(),
                      'overgame': pygame.image.load(cls.cross_sprite('over.png')).convert()}

        cls.surface = {'background': pygame.Surface(WINDOW_SIZE)}             # Convert the window = window surface game

        cls.rect = {'background': cls.loaded['background'].get_rect(center=(0, 0)),
                    'wingame': cls.loaded['wingame'].get_rect(center=(WIDHT / 2, HEIGHT / 2)),
                    'overgame': cls.loaded['overgame'].get_rect(center=(WIDHT / 2, HEIGHT / 2))}

        cls.scale = {'background': pygame.transform.scale(cls.loaded['background'], WINDOW_SIZE),
                     'wall': pygame.transform.scale(cls.loaded['wall'], (SPRITE_SIZE_WIDHT, SPRITE_SIZE_HEIGHT)),
                     'mac': pygame.transform.scale(cls.loaded['mac'], (SPRITE_SIZE_WIDHT, SPRITE_SIZE_HEIGHT)),
                     'path': pygame.transform.scale(cls.loaded['path'], (SPRITE_SIZE_WIDHT, SPRITE_SIZE_HEIGHT)),
                     'start': pygame.transform.scale(cls.loaded['start'], (SPRITE_SIZE_WIDHT, SPRITE_SIZE_HEIGHT)),
                     'finish': pygame.transform.scale(cls.loaded['finish'], (SPRITE_SIZE_WIDHT, SPRITE_SIZE_HEIGHT)),
                     'murdoc': pygame.transform.scale(cls.loaded['murdoc'], (SPRITE_SIZE_WIDHT, SPRITE_SIZE_HEIGHT)),
                     'loot1': pygame.transform.scale(cls.loaded['loot1'],
                                                     (SPRITE_SIZE_WIDHT, SPRITE_SIZE_HEIGHT)),
                     'loot2': pygame.transform.scale(cls.loaded['loot2'],
                                                     (SPRITE_SIZE_WIDHT, SPRITE_SIZE_HEIGHT)),
                     'loot3': pygame.transform.scale(cls.loaded['loot3'],
                                                     (SPRITE_SIZE_WIDHT, SPRITE_SIZE_HEIGHT)),
                     'finalloot': pygame.transform.scale(cls.loaded['finalloot'],
                                                         (SPRITE_SIZE_WIDHT, SPRITE_SIZE_HEIGHT)),
                     'wingame': pygame.transform.scale(cls.loaded['wingame'], CENTER),
                     'overgame': pygame.transform.scale(cls.loaded['overgame'], CENTER)}
