#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Const import WIN_HEIGHT, WIN_WIDTH
from code.menu import Menu
import pygame


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT ))

    def run(self):

        while True:
            menu = Menu(self.window)
            menu.run()
            pass