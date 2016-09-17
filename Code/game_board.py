

def build_game_area():
    board = [[0 for y in range(21)] for x in range(10)]
    
    for x in range(10):
        for y in range(21):
            board[x][y] = Tile(x, y)

    return board


class Tile(object):

    def __init__(self, x, y):
        self.active = False
        self.x = x
        self.y = y
        self.x_pos = x * 25 + 250
        self.y_pos = y * 25
        self.image = ""
        self.top = self.y_pos
        self.bottom = self.y_pos + 25
        self.left = self.x_pos
        self.right = self.x_pos + 25