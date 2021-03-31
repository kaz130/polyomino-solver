import pytest

from psolver.piece import Piece

piece_str = '''
 ##
###'''.split("\n")[1:]

piece = Piece(piece_str)

def test_get_block():
    assert any([piece.get_block(i, 0, 0) for i in range(8)]) == True
    assert all([piece.get_block(i, 0, 0) for i in range(8)]) == False
    assert all([piece.get_block(i, 1, 1) for i in range(8)]) == True
    assert all([piece.get_block(i, 3, 3) for i in range(8)]) == False

def test_get_blocks():
    assert len(piece.get_blocks(0)) == 5

    blocks = piece.get_blocks(0, (2, 3))
    for b in piece.get_blocks(0):
        assert (b[0]+2, b[1]+3) in blocks


def test_get_size():
    assert set([piece.get_size(i) for i in range(8)]) == {(2, 3), (3, 2)}

def test_placement_count():
    assert piece.placement_count == 8
