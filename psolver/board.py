class Board():

    def __init__(self, board_str):
        self.board_str = board_str
        h = len(self.board_str)
        w = max([len(l) for l in self.board_str])

        self.blocks = set()
        for y in range(len(board_str)):
            for x in range(len(board_str[y])):
                if self.board_str[y][x] == "#":
                    self.blocks.add((x, y))

    def get_block(self, x, y):
        return True if (x, y) in self.blocks else False

    def get_blocks(self):
        return self.blocks
    
    def get_size(self):
        h = max([b[1] for b in self.blocks]) + 1
        w = max([b[0] for b in self.blocks]) + 1
        return (h, w)
