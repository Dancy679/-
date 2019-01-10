import pygame
from pygame.locals import *
from sys import exit
from Rules import GameStatus
from tkinter import *


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

    def input(self):
        # print(i, j)
        while True:
            if self.mouse != 0:
                return self.i, self.j

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
                # print("hahahha")
                '''
                if In != Inpre:
                    print (In)
                    # input()
                '''
                self.Inpre = In

                if i_tmp in range(0, 10) and j_tmp in range(0, 10):
                    self.i = i_tmp
                    self.j = j_tmp
                if ((In not in self.black) and (In not in self.white)):
                    self.black.append(In)
                 # print(i)
                 # print(j)
                '''
                if self.i != self.ipre or self.j != self.jpre:
                    print(self.i, self.j)
                    # input()
                ipre, jpre = [self.i, self.j]
                '''


            if not self.i is None and not self.j is None:
               #px, py = 60+(j - 1) * d, 60+ (i - 1) * d
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

            # 刷新一下画面
            pygame.display.update()


if __name__ == '__main__':
    graphic = Graphic()
    graphic.run()


