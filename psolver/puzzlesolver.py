import os
from dotenv import load_dotenv
from tomlkit import parse
from amplify import (
    BinaryPoly,
    BinaryQuadraticModel,
    gen_symbols,
    Solver,
    decode_solution,
)
from amplify.constraint import equal_to
from amplify.client import FixstarsClient

from psolver.piece import Piece 
from psolver.board import Board 
from psolver.visualizer import Visualizer

class PuzzleSolver():

    def __init__(self, puzzle):

        load_dotenv()
        self.client = FixstarsClient()
        self.client.token = os.getenv("TOKEN")
        self.client.parameters.timeout = 10000
        self.client.parameters.outputs.duplicate = False
        if os.getenv("https_proxy") is not None:
            self.client.proxy = os.getenv("https_proxy")

        with open(puzzle) as f:
            puzzle = parse(f.read())

        can_rotate = puzzle.get("can_rotate", True)
        can_reverse = puzzle.get("can_reverse", True) if can_rotate else False

        pieces_str = list(map(lambda x: x.split("\n"), puzzle["pieces"].split("\n\n")))
        pieces_str = list(map(lambda p: list(filter(lambda x: '#' in x, p)), pieces_str))
        pieces_str = list(filter(lambda x: len(x) != 0, pieces_str))
        self.pieces = list()
        for p in pieces_str:
            self.pieces.append(Piece(p, can_rotate, can_reverse))

        board_str = puzzle["board"].split("\n")
        self.board = Board(board_str)

    def solve(self):
        q = gen_symbols(BinaryPoly, *self.board.get_size(), len(self.pieces), 8)


        # 制約(a) 重複する置き方のピースは除外する
        for y in range(self.board.get_size()[0]):
            for x in range(self.board.get_size()[1]):
                for i in range(len(self.pieces)):
                    for j in range(self.pieces[i].placement_count, 8):
                        q[y][x][i][j] = BinaryPoly(0)

        # 制約(b) ピースはボードから外に出ない
        for y in range(self.board.get_size()[0]):
            for x in range(self.board.get_size()[1]):
                for i in range(len(self.pieces)):
                    for j in range(self.pieces[i].placement_count):
                        if len(self.pieces[i].get_blocks(j, (x, y)) - self.board.get_blocks()) > 0:
                            q[y][x][i][j] = BinaryPoly(0)

        # 制約(c) ピース同士は重ならずボードを全て埋める
        s = dict()
        for b in self.board.get_blocks():
            s[b] = BinaryPoly()
        for y in range(self.board.get_size()[0]):
            for x in range(self.board.get_size()[1]):
                for i in range(len(self.pieces)):
                    for j in range(self.pieces[i].placement_count):
                        for p in self.pieces[i].get_blocks(j, (x, y)) & self.board.get_blocks():
                            s[p] += q[y][x][i][j]
        board_constraints = [
                equal_to(q, 1) for q in s.values()
                ]

        # 制約(d) 全てのピースは一度ずつ使われる
        piece_constraints = [
                equal_to(sum(q[y][x][i][j]
                    for y in range(self.board.get_size()[0])
                    for x in range(self.board.get_size()[1])
                    for j in range(8)), 1)
                for i in range(len(self.pieces))
                ]

        constraints = (
                sum(board_constraints)
                + sum(piece_constraints)
                )

        solver = Solver(self.client)

        model = BinaryQuadraticModel(constraints)
        result = solver.solve(model)
        if len(result) == 0:
            raise RuntimeError("Any one of constaraints is not satisfied.")

        solution = result[0]
        values = solution.values
        q_values = decode_solution(q, values)
        Visualizer().visualize(self.pieces, self.board, q_values)

