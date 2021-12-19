import pygame
import random

pygame.init()


class Information():
    BLACK = 0, 0, 0
    WHITE = 255, 255, 255
    GREEN = 0, 255, 0
    RED = 255, 0, 0
    GRAY = 128, 128, 128
    BACKGROUND = WHITE

    SIDE_PAD = 100
    TOP_PAD = 150

    FONT = pygame.font.SysFont('comicsans', 30)
    LARGE_FONT = pygame.font.SysFont('comicsans', 40)

    GRADIENTS = [
        GRAY,
        (128, 128, 128),
        (160, 160, 160),
        (192, 192, 192),
    ]

    def __init__(self, width, height, list):
        self.width = width
        self.height = height
        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Test.....")
        self.set_list(list)

    def set_list(self, list):
        self.list = list
        self.max_val = max(list)
        self.min_val = min(list)
        self.block_width = (self.width - self.SIDE_PAD) / len(list)
        self.block_height = (self.height - self.TOP_PAD) / (self.max_val - self.min_val)
        self.start_x = self.SIDE_PAD // 2


def GenerateList(n, min_val, max_val):
    lst = [random.randint(min_val, max_val) for i in range(n)]
    return lst


def draw(draw_info):
    draw_info.window.fill(draw_info.WHITE)

    menu = draw_info.FONT.render('Write here you wanted....', 1, draw_info.BLACK)
    draw_info.window.blit(menu, (draw_info.width / 2 - menu.get_width() / 2, 5))

    sortMenu = draw_info.FONT.render('Write here you wanted....', 1, draw_info.BLACK)
    draw_info.window.blit(sortMenu, (draw_info.width / 2 - sortMenu.get_width() / 2, 35))

    draw_bar(draw_info)
    pygame.display.update()


def draw_bar(draw_info, color_pos={}, clear_bg=False):
    if clear_bg:
        clear_rect = (draw_info.SIDE_PAD // 2, draw_info.TOP_PAD, draw_info.width - draw_info.SIDE_PAD,
                      draw_info.height - draw_info.TOP_PAD)
        pygame.draw.rect(draw_info.window, draw_info.BACKGROUND, clear_rect)
    for i, j in enumerate(draw_info.list):
        x = draw_info.start_x + i * draw_info.block_width
        y = draw_info.height - (j - draw_info.min_val) * draw_info.block_height

        color = draw_info.GRADIENTS[i % 3]

        if i in color_pos:
            color = color_pos[i]

        pygame.draw.rect(draw_info.window, color, (x, y, draw_info.block_width, draw_info.height))
        if clear_bg:
            pygame.display.update()


def bubbleSort(draw_info, accending=True):
    #lst = draw_info.list
    for i in range(len(draw_info.list) - 1):
        for j in range(len(draw_info.list) - 1 - i):
            num1 = draw_info.list[j]
            num2 = draw_info.list[j + 1]
            if (num1 > num2 and accending) or (num1 < num2 and not accending):
                draw_info.list[j], draw_info.list[j + 1] = draw_info.list[j + 1], draw_info.list[j]
                draw_bar(draw_info, {j: draw_info.GREEN, j + 1: draw_info.RED}, True)
                yield True

    return draw_info.list


def main():
    run = True
    clock = pygame.time.Clock()
    n, min_val, max_val = 50, 0, 100
    info = Information(800, 600, GenerateList(n, 0, 100))
    sorting = False
    accending = True

    algorithm1 = bubbleSort
    sorting_generate = None

    while run:
        clock.tick(60)
        if sorting:
            try:
                next(sorting_generate)
            except StopIteration:
                sorting = False
        else:
            draw(info)

        for event in pygame.event.get():
            if event == pygame.QUIT:
                run = False
            if event.type != pygame.KEYDOWN:
                continue
            if event.key == pygame.K_r:
                lst = GenerateList(n, min_val, max_val)
                info.set_list(lst)
                sorting = False
            elif sorting == False and event.key == pygame.K_SPACE:
                sorting = True
                sorting_generate = algorithm1(info, accending)
            elif not sorting and event.key == pygame.K_a:
                accending = True
            elif not sorting and event.key == pygame.K_d:
                accending = False

    pygame.quit()


if __name__ == "__main__":
    main()
