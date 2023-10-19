# メニュークラス

import pygame
from dataclasses import dataclass
from blocks import Block

BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
YELLOW = (255, 255, 0)

@dataclass
class Menu:
    block: Block
    output: bool

    def __init__(self, screen, block, p):
        self.block = block
        self.block.rect = pygame.draw.rect(screen, self.block.color, self.block.pos)
        self.output = p
    
    def draw(self, screen, font, scol):
        if self.output == True:
            self.block.draw(screen, font, scol) 

    def flip(self):
        if self.output == True:
            self.output = False
        else:
            self.output = True