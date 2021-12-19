import pygame
import random
pygame.init()

class Information():
    BLACK = 0,0,0
    WHITE = 255,255,255
    GREEN = 0,255,0
    RED = 255,0,0
    GRAY = 128,128,128
    BACKGROUND = BLACK

    SIDE_PAD = 100
    TOP_PAD = 150

    GRADIENTS = [
        GRAY,
        (128,128,128),
        (160,160,160),
        (192,192,192),
    ]

    def __init__(self,width,height,list):
        self.width = width
        self.height = height
        self.window = pygame.display.set_mode((width,height))
        pygame.display.set_caption("Test.....")
        self.set_list(list)

    def set_list(self, list):
        self.list = list
        self.max_val = max(list)
        self.min_val = min(list)
        self.block_width = (self.width - self.SIDE_PAD) / len(list)
        self.block_height = (self.height - self.TOP_PAD) / (self.max_val - self.min_val)
        self.start_x = self.SIDE_PAD // 2

def GenerateList(n,min_val,max_val):
    lst = [random.randint(min_val,max_val) for i in range(n)]
    return lst

def draw(draw_info):
    draw_info.window.fill(draw_info.WHITE)
    draw_bar(draw_info)
    pygame.display.update()

def draw_bar(draw_info):
    for i,j in enumerate(draw_info.list):
        x = draw_info.start_x + i * draw_info.block_width
        y = draw_info.height - (j - draw_info.min_val) * draw_info.block_height

        color = draw_info.GRADIENTS[i%3]

        pygame.draw.rect(draw_info.window,color,(x,y,draw_info.block_width,draw_info.height))

def main():
    run = True
    clock = pygame.time.Clock()

    info = Information(800,600,GenerateList(50,0,100))
    while run:
        clock.tick(60)

        draw(info)

        for event in pygame.event.get():
            if event == pygame.QUIT:
                run = False

    pygame.quit()

if __name__ == "__main__":
    main()


