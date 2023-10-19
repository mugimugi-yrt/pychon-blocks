# 使用ブロック/コード表示クラス

from select import select
import pygame
from dataclasses import dataclass
from blocks import Block

BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
ORANGE = (250, 160, 0)

@dataclass
class Code:
    block: Block
    code: str
    select: bool

    def __init__(self, screen, block):
        self.block = block
        self.block.rect = pygame.draw.rect(screen, self.block.color, self.block.pos)
        self.code = block.code
        self.select = False
        
    def draw(self, screen, font, scol):
        self.block.draw(screen, font, scol)

    # クリックしたら色を変える
    def click(self, event, screen, font, scol):
        if (event.button == 1 \
            and self.block.rect.collidepoint(event.pos)):
            # event 座標が自分の箱の中だったら、処理
            if self.select == False:
                self.select = True
            else:
                self.select = False
            screen.fill(BLACK)
            self.draw(screen, font, scol)
            return self.block.id