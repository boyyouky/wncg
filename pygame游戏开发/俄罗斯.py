import sys
import pygame
from pygame.locals import *
import random

SIZE = 30  # 每个小方格大小
BLOCK_HEIGHT = 20  # 游戏区高度
BLOCK_WIDTH = 10   # 游戏区宽度
BORDER_WIDTH = 4   # 游戏区边框宽度
BORDER_COLOR = (40, 40, 200)  # 游戏区边框颜色
SCREEN_WIDTH = SIZE * (BLOCK_WIDTH + 5)  # 游戏屏幕的宽
SCREEN_HEIGHT = SIZE * BLOCK_HEIGHT      # 游戏屏幕的高
BG_COLOR = (40, 40, 60)  # 背景色
BLACK = (0, 0, 0)
S_SHAPE_TEMPLATE = [['.....',
                     '.....',
                     '..OO.',
                     '.OO..',
                     '.....'],
                    ['.....',
                     '..O..',
                     '..OO.',
                     '...O.',
                     '.....']]

Z_SHAPE_TEMPLATE = [['.....',
                     '.....',
                     '.OO..',
                     '..OO.',
                     '.....'],
                    ['.....',
                     '..O..',
                     '.OO..',
                     '.O...',
                     '.....']]

I_SHAPE_TEMPLATE = [['..O..',
                     '..O..',
                     '..O..',
                     '..O..'],
                    ['.....',
                     '.....',
                     'OOOO.',
                     '.....',
                     '.....']]

O_SHAPE_TEMPLATE = [['.....',
                     '.....',
                     '.OO..',
                     '.OO..',
                     '.....']]

J_SHAPE_TEMPLATE = [['.....',
                     '.O...',
                     '.OOO.',
                     '.....',
                     '.....'],
                    ['.....',
                     '..OO.',
                     '..O..',
                     '..O..',
                     '.....'],
                    ['.....',
                     '.....',
                     '.OOO.',
                     '...O.',
                     '.....'],
                    ['.....',
                     '..O..',
                     '..O..',
                     '.OO..',
                     '.....']]

L_SHAPE_TEMPLATE = [['.....',
                     '...O.',
                     '.OOO.',
                     '.....',
                     '.....'],
                    ['.....',
                     '..O..',
                     '..O..',
                     '..OO.',
                     '.....'],
                    ['.....',
                     '.....',
                     '.OOO.',
                     '.O...',
                     '.....'],
                    ['.....',
                     '.OO..',
                     '..O..',
                     '..O..',
                     '.....']]

T_SHAPE_TEMPLATE = [['.....',
                     '..O..',
                     '.OOO.',
                     '.....',
                     '.....'],
                    ['.....',
                     '..O..',
                     '..OO.',
                     '..O..',
                     '.....'],
                    ['.....',
                     '.....',
                     '.OOO.',
                     '..O..',
                     '.....'],
                    ['.....',
                     '..O..',
                     '.OO..',
                     '..O..',
                     '.....']]
PIECES = {'S': S_SHAPE_TEMPLATE,
          'Z': Z_SHAPE_TEMPLATE,
          'J': J_SHAPE_TEMPLATE,
          'L': L_SHAPE_TEMPLATE,
          'I': I_SHAPE_TEMPLATE,
          'O': O_SHAPE_TEMPLATE,
          'T': T_SHAPE_TEMPLATE}

def get_block():
    block_name = random.choice('OIZTLSJ')
    b = PIECES[block_name]
    idx = random.randint(0, len(b) - 1)
    return b[idx]
def get_next_block(block):
    b = PIECES[block.name]
    return b[block.next]
def _judge(pos_x, pos_y, block):
    nonlocal game_area
    for _i in range(block.start_pos.Y, block.end_pos.Y + 1):
        if pos_y + block.end_pos.Y >= BLOCK_HEIGHT:
            return False
        for _j in range(block.start_pos.X, block.end_pos.X + 1):
            if pos_y + _i >= 0 and block.template[_i][_j] != '.' and game_area[pos_y + _i][pos_x + _j] != '.':
                return False
    return True
def print_text(screen, font, x, y, text, fcolor=(255, 255, 255)):
    imgText = font.render(text, True, fcolor)
    screen.blit(imgText, (x, y))


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('俄罗斯方块')

    font1 = pygame.font.SysFont('SimHei', 24)  # 黑体24
    font_pos_x = BLOCK_WIDTH * SIZE + BORDER_WIDTH + 10  # 右侧信息显示区域字体位置的X坐标
    font1_height = int(font1.size('得分')[1])

    score = 0           # 得分

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()

        # 填充背景色
        screen.fill(BG_COLOR)
        # 画游戏区域分隔线
        pygame.draw.line(screen, BORDER_COLOR,
                         (SIZE * BLOCK_WIDTH + BORDER_WIDTH // 2, 0),
                         (SIZE * BLOCK_WIDTH + BORDER_WIDTH // 2, SCREEN_HEIGHT), BORDER_WIDTH)
        # 画网格线 竖线
        for x in range(BLOCK_WIDTH):
            pygame.draw.line(screen, BLACK, (x * SIZE, 0), (x * SIZE, SCREEN_HEIGHT), 1)
        # 画网格线 横线
        for y in range(BLOCK_HEIGHT):
            pygame.draw.line(screen, BLACK, (0, y * SIZE), (BLOCK_WIDTH * SIZE, y * SIZE), 1)

        print_text(screen, font1, font_pos_x, 10, f'得分: ')
        print_text(screen, font1, font_pos_x, 10 + font1_height + 6, f'{score}')
        print_text(screen, font1, font_pos_x, 20 + (font1_height + 6) * 2, f'速度: ')
        print_text(screen, font1, font_pos_x, 20 + (font1_height + 6) * 3, f'{score // 10000}')
        print_text(screen, font1, font_pos_x, 30 + (font1_height + 6) * 4, f'下一个：')

        pygame.display.flip()


if __name__ == '__main__':
    main()