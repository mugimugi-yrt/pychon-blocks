# ブロッククラス(全ての基盤)

import pygame
from dataclasses import dataclass

BOX_WIDTH = 150
BOX_HEIGHT = 30
BOX_GAP = 15
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
GRAY = (200, 200, 200)
GRAY2 = (100, 100, 100)
GRAY3 = (150, 150, 150)
BLACK = (0, 0, 0)

@dataclass
class Block:
    id: int
    pos: tuple
    color: tuple
    code: str

    def __init__(self, id, x, y, width, height, color, code):
        self.id = id
        self.pos = (x, y, width, height)
        self.color = color
        self.code = code
    
    def draw(self, screen, font, scol):
        pygame.draw.rect(screen, self.color, self.pos)
        self.rect = pygame.draw.rect(screen, self.color, self.pos)
        text = font.render(str(self.code), True, scol)
        position = text.get_rect()
        position.center = self.rect.center # 中央に表示
        screen.blit(text, position)  # テキストを画面に転送する
    
    # クリックしたらクリックしたブロックのidを返す
    def click(self, event, screen, font, scol):
        if (event.button == 1 \
            and self.rect.collidepoint(event.pos)):
            # event 座標が自分の箱の中だったら、処理
            screen.fill(BLACK)
            self.draw(screen, font, scol)
            return self.id
    
    # 色付け
    def colorup(self, screen, font, scol):
        if (self.rect.collidepoint(pygame.mouse.get_pos()) \
            and self.color == GRAY):
            screen.fill(BLACK)
            # print(pygame.mouse.get_pos())
            self.color = YELLOW
            self.draw(screen, font, scol)
            return True
        elif (not self.rect.collidepoint(pygame.mouse.get_pos()) \
            and self.color == YELLOW):
            screen.fill(BLACK)
            self.color = GRAY
            self.draw(screen, font, scol)
            return True