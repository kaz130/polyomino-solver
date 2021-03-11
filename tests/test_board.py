import pytest

from cpsolver.board import Board

board_str = '''
###
# #'''.split("\n")[1:]

board = Board(board_str)

def test_get_block():
    assert board.get_block(0, 0) == True
    assert board.get_block(1, 1) == False
    assert board.get_block(1, 0) == True
    assert board.get_block(3, 3) == False

def test_get_size():
    assert board.get_size() == (2, 3)

def test_get_blocks():
    assert len(board.get_blocks()) == 5
