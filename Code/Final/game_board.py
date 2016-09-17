
## cosntructs the game area grid with generic Tile objects. This is the starting
## position of the game
def build_game_area():
    board = [[0 for y in range(50)] for x in range(10)]
    
    for x in range(10):
        for y in range(50):
            board[x][y] = Tile(x, y)

    return board


## This object is a single piece on the game area grid. It tracks the attributes
## necessary for object collission
class Tile(object):

    def __init__(self, x, y):
        self.active = False
        self.x = x
        self.y = y
        self.x_pos = x * 25 + 279
        self.y_pos = y * 25 + 2
        self.image = ""
        self.top = self.y_pos
        self.bottom = self.y_pos + 25
        self.left = self.x_pos
        self.right = self.x_pos + 25