# 背景使用ブロッククラス

import pygame
from dataclasses import dataclass

BLUE = (0, 0, 255)

@dataclass
class Ground:
    id: int
    name: str
    pos: tuple
    color: tuple

    def __init__(self, id, x, y, width, height, color, name):
        self.id = id
        self.name = name
        self.pos = (x, y, width, height)
        self.color = color
    
    def draw(self, screen, font, scol):
        pygame.draw.rect(screen, self.color, self.pos)
        self.rect = pygame.draw.rect(screen, self.color, self.pos)