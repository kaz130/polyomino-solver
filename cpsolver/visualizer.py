box_drawing_characters = [' ', '╹', '╺', '┗', '╻', '┃', '┏', '┣', '╸', '┛', '━', '┻', '┓', '┫', '┳', '╋']

class Visualizer():

    def __init__(self):
        pass

    def visualize(self, pieces, board, q_values):
        r = '\n'.join(map(lambda x: ''.join(x), self.make_str(pieces, board, q_values)))
        print(r)

    def make_str(self, pieces, board, q_values):
        solved_board = [[-1] * (board.get_size()[1] + 2) for i in range(board.get_size()[0] + 2)]
        for y in range(board.get_size()[0]):
            for x in range(board.get_size()[1]):
                for i in range(len(pieces)):
                    for j in range(8):
                        if q_values[y][x][i][j] == 1:
                            for b in pieces[i].get_blocks(j, offset=(x, y)):
                                solved_board[b[1]+1][b[0]+1] = i

        board_str = [[' '] * (board.get_size()[1] * 2 + 1) for i in range(board.get_size()[0] + 1)]
        for y, boad_line in enumerate(solved_board[:-1]):
            for x, b in enumerate(boad_line[:-1]):
                m = 0
                if solved_board[y][x] != solved_board[y][x+1]: m += 1
                if solved_board[y][x+1] != solved_board[y+1][x+1]: m += 2
                if solved_board[y+1][x] != solved_board[y+1][x+1]: m += 4
                if solved_board[y][x] != solved_board[y+1][x]: m += 8
                c = box_drawing_characters[m]
                board_str[y][x*2] = c
                if m & 2: board_str[y][x*2 + 1] = box_drawing_characters[10]
        return board_str
