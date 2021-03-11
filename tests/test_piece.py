import pytest

from cpsolver.piece import Piece

piece_str = '''
 ##
###'''.split("\n")[1:]

piece = Piece(piece_str)

def test_get_block():
    assert any([piece.get_block(i, 0, 0) for i in range(8)]) == True
    assert all([piece.get_block(i, 0, 0) for i in range(8)]) == False
    assert all([piece.get_block(i, 1, 1) for i in range(8)]) == True
    assert all([piece.get_block(i, 3, 3) for i in range(8)]) == False

def test_get_size():
    assert set([piece.get_size(i) for i in range(8)]) == {(2, 3), (3, 2)}

def test_placement_count():
    assert piece.placement_count == 8
