import pygame
from pygame.locals import *
from sys import exit
from Rules import GameStatus
from tkinter import *
import time

class Graphic():
    black = []
    white = []

    def array2index(self,array):
        return (array[0])*10+array[1]

    i,j = None,None
    # i, j = 4, 4
    d=60
    status = GameStatus()
    Inpre = -1
    ipre = -1
    jpre = -1
    mouse = 0
    display_width = 660
    display_height = 660
    gameDisplay = pygame.display.set_mode((display_width, display_height))
    display_result = 0

    def input(self):
        # print(i, j)
        while True:
            if self.mouse != 0:
                return self.i, self.j

    def text_objects(self, text, font):
        black = (0,0,0)
        textSurface = font.render(text, True, black)
        return textSurface, textSurface.get_rect()

    def message_diaplay(self, text):
        largeText = pygame.font.Font('freesansbold.ttf', 49)
        TextSurf, TextRect = self.text_objects(text, largeText)
        TextRect.center = ((self.display_width / 2), (self.display_height / 2))
        self.gameDisplay.blit(TextSurf, TextRect)
        self.display_result = 1
        pygame.display.update()
        time.sleep(100)

    def run(self):
        while True:
            for event in pygame.event.get():
               if event.type == QUIT:
                    pygame,quit()
                    exit()
            self.mouse = 0
            pressed_mouse = pygame.mouse.get_pressed()


            if pressed_mouse[0]:
                self.mouse = 1
                x, y = pygame.mouse.get_pos()
                i_tmp, j_tmp = round((y - 60) / self.d) + 1, round((x - 60) / self.d) + 1
                i_tmp=10-i_tmp
                j_tmp = j_tmp - 1
                In = self.array2index((i_tmp, j_tmp))
                self.Inpre = In

                if i_tmp in range(0, 10) and j_tmp in range(0, 10):
                    self.i = i_tmp
                    self.j = j_tmp
                if ((In not in self.black) and (In not in self.white)):
                    self.black.append(In)

            if not self.i is None and not self.j is None:
               if (self.j) == 0:
                   px, py = 60, 60 + (self.i - 1) * self.d
                   py = 660 - py
               else:
                   px, py = (self.j - 1) * self.d, 60+(self.i - 1) * self.d
                   py = 660 - py
            self.status.SetList(self.black, self.white)
            # 绘制背景和棋子
            self.status.draw_background()
            self.status.draw_pieces()
            # self.message_diaplay('hahaha')

            # 刷新一下画面
            if self.display_result == 0 :
                pygame.display.update()


if __name__ == '__main__':
    graphic = Graphic()
    graphic.run()


