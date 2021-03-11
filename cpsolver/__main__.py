import sys
import click

from cpsolver.puzzlesolver import PuzzleSolver

@click.command()
@click.argument('filename')
def main(filename):
    solver = PuzzleSolver(filename)
    solver.solve()

if __name__ == '__main__':
    main()

