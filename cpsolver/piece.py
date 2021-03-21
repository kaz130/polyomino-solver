class Piece():

    def __init__(self, piece_str):
        self.piece_str = piece_str
        h = len(self.piece_str)
        w = max([len(l) for l in self.piece_str])

        blocks = set()
        for y in range(len(piece_str)):
            for x in range(len(piece_str[y])):
                if self.piece_str[y][x] == "#":
                    blocks.add((x, y))

        blocks_list = list()
        for i in range(2):
            for j in range(4):
                blocks_list.append(blocks)
                new_blocks = set()
                h, w = (w, h)
                for b in blocks:
                    new_blocks.add((b[1], -b[0]+h-1))
                blocks = new_blocks
            new_blocks = set()
            h, w = (w, h)
            for b in blocks:
                new_blocks.add((b[1], b[0]))
                blocks = new_blocks

        uniqued_blocks = sorted(set([tuple(sorted(blocks)) for blocks in blocks_list]))
        self.placement_count = len(uniqued_blocks)
        self.placed_pieces = tuple([set(blocks) for blocks in uniqued_blocks])

    def get_block(self, p, x, y):
        return True if (x, y) in self.placed_pieces[p] else False

    def get_blocks(self, p, offset=(0, 0)):
        return set(((b[0]+offset[0], b[1]+offset[1]) for b in self.placed_pieces[p]))

    def get_size(self, p):
        h = max([b[1] for b in self.placed_pieces[p]]) + 1
        w = max([b[0] for b in self.placed_pieces[p]]) + 1
        return (h, w)
