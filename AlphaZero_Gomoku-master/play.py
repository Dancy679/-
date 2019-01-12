# -*- coding: utf-8 -*-

from __future__ import print_function
from game import Board, Game
from policy_value_net import PolicyValueNet
from mcts_pure import MCTSPlayer as MCTS_Pure
from mcts_alphaZero import MCTSPlayer
import pickle
import threading
import _thread as thread
from Graphic import Graphic


class myThread (threading.Thread):
    def __init__(self, graphic):
        threading.Thread.__init__(self)
        self.graphic = graphic
    def run(self):
        self.graphic.run()


class Human(object):

    def __init__(self, graphic):
        self.player = None
        self.graphic = graphic

    def set_player_ind(self, p):
        self.player = p

    def get_action(self, board):
        try:
            # location = input("Your move: ")
            print("is your turns")
            location = self.graphic.input()
            print(location)
            if isinstance(location, str):
                location = [int(n, 10) for n in location.split(",")]
            move = board.location_to_move(location)
        except Exception as e:
            move = -1
        if move == -1 or move not in board.availables:
            print("invalid move")
            move = self.get_action(board)
        return move

    def __str__(self):
        return "Human {}".format(self.player)


def run():
    n = 5
    width, height = 10, 10
    model_file = 'current_policy.model'
    try:
        board = Board(width=width, height=height, n_in_row=n)
        game = Game(board)
        graphic = Graphic()
        # graphic.run()
        print(1111)
        # thread1 = threading.Thread(target=graphic.run, args=())
        best_policy = PolicyValueNet(width, height, model_file='./model/' + model_file)
        mcts_player = MCTSPlayer(best_policy.policy_value_fn, c_puct=5, n_playout=1200)
        human = Human(graphic)
        # set start_player=0 for human first
        thread2 = threading.Thread(target=game.start_play, args=(human, mcts_player, graphic, 1, 1))
        # game.start_play(human, mcts_player, graphic, start_player=0, is_shown=1)
        thread2.setDaemon(True)
        thread2.start()
        graphic.run()
    except KeyboardInterrupt:
        print('\n\rquit')


if __name__ == '__main__':
    run()
