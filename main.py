#　メインプログラム

import pygame
import copy
from blocks import Block
from ground import Ground
from code import Code
from menu import Menu

WIDTH = 180
HEIGHT = 40
GAP = 15
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
ORANGE = (250, 160, 0)
BLUE = (0, 0, 255)
GREEN = (0, 204, 102)
GRAY = (200, 200, 200)
GRAY2 = (100, 100, 100)
GRAY3 = (150, 150, 150)
GRAY4 = (250, 250, 250)
BLACK = (0, 0, 0)
CODES = ["Hello, World!を表示"]
P_CODES = ["print(\"Hello, World!\")"]
EX_LIST = ["Hello, World!"]

def set_screen():
    screens = []
    block_screen = Ground(0, 20, 20, 300, 950, GRAY2, "BLOCKS")
    codeB_screen = Ground(1, 330, 20, 320, 950, GRAY3, "BLOCK CODE")
    codeP_screen = Ground(2, 660, 20, 340, 950, GRAY3, "PYTHON CODE")
    menu_screen = Ground(3, 1020, 770, 750, 200, WHITE, "MENU")
    exe_screen = Ground(4, 1020, 20, 750, 700, WHITE, "EXE SCREEN")
    screens.append(block_screen)
    screens.append(codeB_screen)
    screens.append(codeP_screen)
    screens.append(menu_screen)
    screens.append(exe_screen)
    blocks = Block(1000, 40, 30, 50, 20, GRAY2, "BLOCKS")
    codeB = Block(1001, 380, 30, 50, 20, GRAY3, "BLOCKS CODE")
    codeP = Block(1002, 710, 30, 50, 20, GRAY3, "PYTHON CODE")
    menu = Block(1003, 1050, 790, 40, 20, WHITE, "MENU")
    exes = Block(1004, 1060, 40, 60, 20, WHITE, "EXE SCREEN")
    screens.append(blocks)
    screens.append(codeB)
    screens.append(codeP)
    screens.append(menu)
    screens.append(exes)
    draw_ground(screens)
    return screens

def draw_ground(lscreen):
    fontg = pygame.font.Font('ipaexg.ttf', 20)
    for s in lscreen:
        s.draw(screen, fontg, GREEN)

def set_blocks():
    blocks = []
    (x, y) = (50, 80)
    for i in range(len(CODES)):
        block = Block(i, x, y, WIDTH, HEIGHT, GRAY, CODES[i])
        block.draw(screen, font, BLUE)
        blocks.append(block)
        y += HEIGHT + GAP
    return blocks

def set_menu():
    menus = []
    startb = Block(1005, 1080, 850, 80, 80, GRAY, "▶")
    stopb = Block(1006, 1200, 850, 80, 80, GRAY, "■")
    trashb = Block(1007, 1320, 850, 110, 80, GRAY, "erase")
    clearb = Block(1008, 1470, 850, 110, 80, GRAY, "clear")
    doneb = Block(1009, 1620, 850, 110, 80, GRAY, "done")
    start = Menu(screen, startb, True)
    trash = Menu(screen, trashb, False)
    stop = Menu(screen, stopb, False)
    clear = Menu(screen, clearb, True)
    done = Menu(screen, doneb, False)
    menus.append(start)   #0
    menus.append(stop)    #1
    menus.append(trash)   #2
    menus.append(clear)   #3
    menus.append(done)    #4
    draw_menu(menus)
    return menus

def flip_block(mlist):
    # ブロック選択時のメニュー表示(erase, trashだけ表示)
    mlist[0].flip()
    mlist[2].flip()

def flip_exec(mlist):
    # 実行時のメニュー表示(□だけ表示)
    mlist[0].flip()
    mlist[1].flip()
    mlist[3].flip()

def flip_done(mlist):
    # 編集終了のメニュー表示(doneを表示)
    mlist[4].flip()

def draw_menu(mlist):
    fontm = pygame.font.Font('ipaexg.ttf', 40)
    for menu in mlist:
        menu.draw(screen, fontm, BLUE)

def add_bcode(blist, num, i):
    ny = 80 + i * (HEIGHT + 2)
    block = Block(i, 360, ny, WIDTH, HEIGHT, GRAY, CODES[num])
    bcode = Code(screen, block)
    bcode.code = EX_LIST[num]
    blist.append(bcode)

def add_pcode(plist, num, i):
    ny = 80 + i * (HEIGHT + 2)
    block = Block(i, 690, ny, WIDTH, HEIGHT, GRAY, P_CODES[num])
    pcode = Code(screen, block)
    pcode.code = EX_LIST[num]
    plist.append(pcode)

def draw_blocks(blist, bc, pc):
    for block in blist:
        block.draw(screen, font, BLUE)
    for bcode in bc:
        bcode.draw(screen, font, BLUE)
    for pcode in pc:
        pcode.draw(screen, font, BLUE)

def reset_blocks(cdlist):
    for cd in cdlist:
        cd.block.color = GRAY
        cd.select = False

def colorupper(l, g, s, f, c):
    c_tf = True
    for o in l:
        if type(o) == Menu:
            c_tf = o.output
        if c_tf:
            if type(o) == Code or type(o) == Menu:
                o = o.block
            if o.colorup(s, f, c):
                draw_ground(g)
                o.draw(s, f, c)

def swap_codes(codes, n1, n2):
    n_codes = []
    b1 = copy.deepcopy(codes[n1].block)
    b2 = copy.deepcopy(codes[n2].block)
    nb1 = Block(b1.id, b1.pos[0], b1.pos[1], b1.pos[2], b1.pos[3], b1.color, b2.code)
    nb2 = Block(b2.id, b2.pos[0], b2.pos[1], b2.pos[2], b2.pos[3], b2.color, b1.code)
    nc1 = Code(screen, nb1)
    nc1.code = codes[n2].code
    nc2 = Code(screen, nb2)
    nc2.code = codes[n1].code
    i = 0
    while i < len(codes):
        if i == n1:
            n_codes.append(nc1)
        elif i == n2:
            n_codes.append(nc2)
        else:
            n_codes.append(codes[i])
        i = i + 1
    return n_codes

def erase_codes(codes, n):
    n_codes = []
    i1 = 0
    while i1 < n:
        n_codes.append(codes[i1])
        i1 = i1 + 1
    for i2 in range(i1, len(codes)-1):
        b = copy.deepcopy(codes[i2].block)
        nb = Block(b.id, b.pos[0], b.pos[1], b.pos[2], b.pos[3], b.color, codes[i2+1].block.code)
        nc = Code(screen, nb)
        n_codes.append(nc)
    return n_codes

def e_check(codes):
    if len(codes) == 0:
        return 0
    else:
        return -1

def execute(pc_list):
    ex_list = []
    id = 100000
    x = 1040
    y = 100
    for pc in pc_list:
        exec(pc.block.code)
        exe = Block(id, x, y, pc.block.pos[2], pc.block.pos[3], GRAY4, pc.code)
        ex_list.append(exe)
        y = y + pc.block.pos[3]
    return ex_list

def end_list(l, x, y, col):
    fl = []
    for o in l:
        if type(o) == Code:
            o = o.block
        fb = Block(o.id, x, y, o.pos[2], o.pos[3], col, o.code)
        fl.append(fb)
        y = y + fb.pos[3] + 5
    return fl

# --- main ---
while True:
    i = input("表示したい文字列の入力(00で終了)>>")
    if str(i) == "00":
        break
    ns = str(i) + "を表示"
    np = "print(\"" + str(i) + "\")"
    CODES.append(ns)
    P_CODES.append(np)
    EX_LIST.append(str(i))

pygame.init() # pygame.font.init()
screen = pygame.display.set_mode((1800, 1000))
pygame.display.set_caption(u"ぱいちょんぶろっくす")
font = pygame.font.Font('ipaexg.ttf', 18)

screens = set_screen()
blocks = set_blocks()
menus = set_menu()
bcodes = []
pcodes = []
loop = True
finish = False
(i, s1, s2, d, er) = (0, 0, 0, 0, -2)
error = Block(1000000, 1040, 100, 140, 40, GRAY4, "ERROR!!")
err_list = ["ブロック入力がありません。"]
err_size = [(1180, 100, 300, 40)]
n2 = None
n4 = None
ex_block = []
while loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
        elif event.type == pygame.MOUSEBUTTONUP:
            if n2 == None and n4 == None and d == 0:
                for block in blocks:
                    n = block.click(event, screen, font, BLUE)
                    if n != None:
                        add_bcode(bcodes, n, i)
                        add_pcode(pcodes, n, i)
                        i = i + 1
            if s2 == 0 and d == 0:
                for bcode in bcodes:
                    n1 = bcode.click(event, screen, font, BLUE)
                    if n1 != None:
                        s1 = s1 + 1
                        flip_block(menus)
                        if s1 == 2:
                            if n1 != n2:
                                nbcodes = swap_codes(bcodes, n1, n2)
                                bcodes = copy.deepcopy(nbcodes)
                                npcodes = swap_codes(pcodes, n1, n2)
                                pcodes = copy.deepcopy(npcodes)
                            s1 = 0
                        n2 = n1
                        n1 = None
                        if s1 == 0:
                            n2 = None
                    if bcode.select == True:
                        bcode.block.color = ORANGE
                        for pcode in pcodes:
                            if pcode.block.id == bcode.block.id:
                                pcode.block.color = ORANGE
                    else:
                        bcode.block.color = GRAY
            if s1 == 0 and d == 0:
                for pcode in pcodes:
                    n3 = pcode.click(event, screen, font, BLUE)
                    if n3 != None:
                        s2 = s2 + 1
                        flip_block(menus)
                        if s2 == 2:
                            if n3 != n4:
                                nbcodes = swap_codes(bcodes, n3, n4)
                                bcodes = copy.deepcopy(nbcodes)
                                npcodes = swap_codes(pcodes, n3, n4)
                                pcodes = copy.deepcopy(npcodes)
                            s2 = 0
                        n4 = n3
                        n3 = None
                        if s2 == 0:
                            n4 = None
                    if pcode.select == True:
                        pcode.block.color = ORANGE
                        for bcode in bcodes:
                            if bcode.block.id == pcode.block.id:
                                bcode.block.color = ORANGE
                    else:
                        pcode.block.color = GRAY
            for menu in menus:
                m = menu.block.click(event, screen, font, BLUE)
                if m != None:
                    if menu.output == True:
                        if m == 1005:
                            flip_exec(menus)
                            d = 1
                            er = e_check(bcodes)
                            if er == -1:
                                ex_block = execute(pcodes)
                                exec("print(\"---------------\")")
                                flip_done(menus)
                            else:
                                ex_block.append(error)
                                er_block = Block(100001, err_size[er][0], err_size[er][1], err_size[er][2], err_size[er][3], GRAY4, err_list[er])
                                ex_block.append(er_block)
                        elif m == 1006:
                            if er == -1:
                                flip_done(menus)
                            flip_exec(menus)
                            d = 0
                            ex_block = []
                        elif m == 1007:
                            if n2 != None:
                                nbcodes = erase_codes(bcodes, n2)
                                npcodes = erase_codes(pcodes, n2)
                                s1 = 0
                                n2 = None
                            elif n4 != None:
                                nbcodes = erase_codes(bcodes, n4)
                                npcodes = erase_codes(pcodes, n4)
                                s2 = 0
                                n4 = None
                            bcodes = copy.deepcopy(nbcodes)
                            pcodes = copy.deepcopy(npcodes)
                            reset_blocks(bcodes)
                            reset_blocks(pcodes)
                            flip_block(menus)
                            i = i - 1
                        elif m == 1008:
                            bcodes = []
                            pcodes = []
                            i = 0
                            (s1, s2) = (0, 0)
                            (n1, n2, n3, n4) = (None, None, None, None)
                            if menus[2].output:
                                flip_block(menus)
                        else:
                            screen.fill((0, 0, 0))
                            finish = True
                            loop = False
            if menus[0].output == True:
                reset_blocks(bcodes)
                reset_blocks(pcodes)
        elif event.type == pygame.MOUSEMOTION:
            if n2 == None and n4 == None and d == 0:
                colorupper(blocks, screens, screen, font, BLUE)
            if s2 == 0 and d == 0:
                colorupper(bcodes, screens, screen, font, BLUE)
            if s1 == 0 and d == 0:
                colorupper(pcodes, screens, screen, font, BLUE)
            colorupper(menus, screens, screen, font, BLUE)
    if loop == True:
        draw_ground(screens)
        draw_menu(menus)
        draw_blocks(blocks, bcodes, pcodes)
        if ex_block != []:
            for exe in ex_block:
                exe.draw(screen, font, BLUE)
    pygame.display.flip()

screen = pygame.display.set_mode((1500, 1000))
pygame.display.set_caption(u"Well Done!!")
ffont1 = pygame.font.Font('ipaexg.ttf', 100)
ffont2 = pygame.font.Font('ipaexg.ttf', 50)
wd = Block(1000000, 100, 0, 200, 100, BLACK, "Finish!!")
wd_str1 = Block(1000001, 100, 140, 570, 50, BLACK, "出来たコードはpythonで表すと")
wd_str2 = Block(1000002, 100, 200, 600, 50, BLACK, "コードは以下のようになります。")
codeP_screen = Ground(2, 20, 300, 700, 600, GRAY3, "PYTHON CODE")
exe_screen = Ground(4, 750, 300, 700, 600, WHITE, "EXE SCREEN")
codeP = Block(1002, 70, 320, 50, 20, GRAY3, "PYTHON")
exes = Block(1004, 790, 320, 60, 20, GRAY4, "実行画面")
fscreens = [codeP_screen, codeP, exe_screen, exes]
fpcodes = end_list(pcodes, 50, 350, GRAY)
fexe = end_list(ex_block, 750, 350, WHITE)

while finish:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish = False
    wd.draw(screen, ffont1, WHITE)
    wd_str1.draw(screen, ffont2, WHITE)
    wd_str2.draw(screen, ffont2, WHITE)
    for sc in fscreens:
        sc.draw(screen, font, BLACK)
    for fpc in fpcodes:
        fpc.draw(screen, font, BLUE)
    for fe in fexe:
        fe.draw(screen, font, BLACK)
    pygame.display.flip()