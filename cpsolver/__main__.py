import sys
import click

from cpsolver.puzzlesolver import PuzzleSolver

def main():
    solver = PuzzleSolver("sample.toml")
    solver.solve()

if __name__ == '__main__':
    main()

