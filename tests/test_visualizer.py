import pytest

from cpsolver.board import Board
from cpsolver.piece import Piece
from cpsolver.visualizer import Visualizer

board_str = '''
###
###'''.split("\n")[1:]

piece_str = '''
###
##'''.split("\n")[1:]

expectation = '''\
┏━━━━━┓
┃   ┏━┛
┗━━━┛  '''

board = Board(board_str)
piece = Piece(piece_str)
q_values = [
        [[[0, 0, 0, 1, 0, 0, 0, 0]], [[0, 0, 0, 0, 0, 0, 0, 0]], [[0, 0, 0, 0, 0, 0, 0, 0]]],
        [[[0, 0, 0, 0, 0, 0, 0, 0]], [[0, 0, 0, 0, 0, 0, 0, 0]], [[0, 0, 0, 0, 0, 0, 0, 0]]]]

def test_visualize():
    r = '\n'.join(map(lambda x: ''.join(x), Visualizer().make_str([piece], board, q_values)))
    assert r == expectation

