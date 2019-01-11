import pygame
from pygame.locals import *

imagePath = './Picture/'

d = 60


def array2index(array):
    return (array[0]-1)*10+array[1]


def index2array(index):
    l=index % 10
    return (index-l)/10+1,l


def array2pixel(array):
    if(array[0])==0:
        px, py = 60, 60 + (array[0] - 1) * d
        py = 600- py

    else :
        px, py = 120+ (array[1] - 1) * d, 60 + (array[0] - 1) * d
        py= 660-py
    return px,py


class GameStatus(object):
    def __init__(self):
        self._black = list()
        self._white = list()

        pygame.init()
        self._screen = pygame.display.set_mode((660, 660), 0, 32)
        pygame.display.set_caption('Gomoku')


        self.Chessboard = pygame.image.load(imagePath + 'QiPan.jpg').convert()
        self.BlackPiece = pygame.image.load(imagePath + 'black.png').convert_alpha()
        self.WhitePiece = pygame.image.load(imagePath + 'white.png').convert_alpha()

    def SetList(self,black,white):
            self._black = black
            self._white = white

    def black_append(self,index):
         self._black.append(index)

    def black_list(self):
        return self._black

    def white_append(self, index):
        self._white.append(index)

    def white_list(self):
        return self._white

    def white_count(self):
        return len(self._white)

    def empty_list(self):
        empty = list(range(0, 101))
        for i, j in zip(self._black, self._white):
            empty.remove(i)
            empty.remove(j)
        return empty

    def draw_background(self):
        self._screen.blit(self.Chessboard, (0, 0))

    def draw_pieces(self):
        for i in zip(self._black):
            x, y = array2pixel(index2array(i[0]))
            x -= self.BlackPiece.get_width() / 2
            y -= self.BlackPiece.get_height() / 2



            self._screen.blit(self.BlackPiece, (x, y))
        for  j in zip(self._white):
            x, y = array2pixel(index2array(j[0]))
            x -= 15
            y -= 15
            self._screen.blit(self.WhitePiece, (x, y))





