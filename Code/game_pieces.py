import random

# RGB colour values
WHITE = 255, 255, 255
GREEN = 0, 255, 0
BLUE = 0, 0, 255
RED = 255, 0, 0
PURPLE = 160, 32, 240
CYAN = 0, 255, 255
YELLOW = 255, 255, 51
ORANGE = 255, 128, 0

# Setting the position that the pieces appear on the game board
initial_x_pos = 375
initial_y_pos = -100

# values of how many pixels each move takes
SHIFT_left = -25
SHIFT_right = 25
SHIFT_up = -25
SHIFT_down = 25

# return a random game piece
def random_piece():
        num = random.randint(0, 6)
        if num == 0:
            return I_piece()
        elif num == 1:
            return O_piece()
        elif num == 2:
            return T_piece()
        elif num == 3:
            return J_piece()
        elif num == 4:
            return Z_piece()
        elif num == 5:
            return S_piece()
        elif num == 6:
            return L_piece()
            

class Segment(object):

    def __init__(self, x, y, colour):            
        self.x = x
        self.y = y
        self.x_grid = (x - 250) / 25
        self.y_grid = y / 25
        self.colour = colour
        self.top = y
        self.bottom = y + 25
        self.left = x
        self.right = x + 25

    def move_segment(self):
        self.top = self.y
        self.bottom = self.y + 25
        self.left = self.x
        self.right = self.x + 25
        self.x_grid = (self.x - 250) / 25
        self.y_grid = self.y / 25



class T_piece (object):

    def __init__(self):
        self.main_piece = Segment(initial_x_pos, initial_y_pos, PURPLE)
        self.second_piece = Segment(self.main_piece.x + SHIFT_left, self.main_piece.y, PURPLE)
        self.third_piece = Segment(self.main_piece.x + SHIFT_right, self.main_piece.y, PURPLE)
        self.fourth_piece = Segment(self.main_piece.x, self.main_piece.y + SHIFT_up, PURPLE)

        self.left = self.second_piece.x
        self.right = self.third_piece.x + 25
        self.bottom = self.main_piece.y + 25
        
        self.orientation = "up"

    def changeOrientation(self):
        if self.orientation == "up":
            self.orientation = "right"
        elif self.orientation == "right":
            self.orientation = "down"
        elif self.orientation == "down":
            self.orientation = "left"
        elif self.orientation == "left":
            self.orientation = "up"
        self.setOrientation()

    def setOrientation(self):
        if self.orientation == "up":
            self.second_piece.x = self.second_piece.x + SHIFT_left
            self.second_piece.y = self.second_piece.y + SHIFT_up
            self.third_piece.x = self.third_piece.x + SHIFT_right
            self.third_piece.y = self.third_piece.y + SHIFT_down
            self.fourth_piece.x = self.fourth_piece.x + SHIFT_right
            self.fourth_piece.y = self.fourth_piece.y + SHIFT_up

            self.left = self.second_piece.x
            self.right = self.third_piece.x + 25
            self.bottom = self.main_piece.y + 25
                
        elif self.orientation == "right":
            self.second_piece.x = self.second_piece.x + SHIFT_right
            self.second_piece.y = self.second_piece.y + SHIFT_up
            self.third_piece.x = self.third_piece.x + SHIFT_left
            self.third_piece.y = self.third_piece.y + SHIFT_down
            self.fourth_piece.x = self.fourth_piece.x + SHIFT_right
            self.fourth_piece.y = self.fourth_piece.y + SHIFT_down
           
            self.left = self.second_piece.x
            self.right = self.fourth_piece.x + 25
            self.bottom = self.third_piece.y + 25

        elif self.orientation == "down":
            self.second_piece.x = self.second_piece.x + SHIFT_right
            self.second_piece.y = self.second_piece.y + SHIFT_down
            self.third_piece.x = self.third_piece.x + SHIFT_left
            self.third_piece.y = self.third_piece.y + SHIFT_up
            self.fourth_piece.x = self.fourth_piece.x + SHIFT_left
            self.fourth_piece.y = self.fourth_piece.y + SHIFT_down

            self.left = self.third_piece.x
            self.right = self.second_piece.x + 25
            self.bottom = self.fourth_piece.y + 25

        elif self.orientation == "left":
            self.second_piece.x = self.second_piece.x + SHIFT_left
            self.second_piece.y = self.second_piece.y + SHIFT_down
            self.third_piece.x = self.third_piece.x + SHIFT_right
            self.third_piece.y = self.third_piece.y + SHIFT_up
            self.fourth_piece.x = self.fourth_piece.x + SHIFT_left
            self.fourth_piece.y = self.fourth_piece.y + SHIFT_up

            self.left = self.fourth_piece.x
            self.right = self.main_piece.x + 25
            self.bottom = self.second_piece.y + 25

        self.main_piece.move_segment()
        self.second_piece.move_segment()
        self.third_piece.move_segment()
        self.fourth_piece.move_segment()

        if self.left < 0:
            self.movePiece("right")
        elif self.right > 100:
            self.movePiece("left")


    def movePiece(self, direction):
        if direction == "down":
            self.main_piece.y = self.main_piece.y + SHIFT_down
            self.second_piece.y = self.second_piece.y + SHIFT_down
            self.third_piece.y = self.third_piece.y + SHIFT_down
            self.fourth_piece.y = self.fourth_piece.y + SHIFT_down

            self.bottom = self.bottom + SHIFT_down
            
        elif direction == "left":
            self.main_piece.x = self.main_piece.x + SHIFT_left
            self.second_piece.x = self.second_piece.x + SHIFT_left
            self.third_piece.x = self.third_piece.x + SHIFT_left
            self.fourth_piece.x = self.fourth_piece.x + SHIFT_left

            self.left = self.left + SHIFT_left
            self.right = self.right + SHIFT_left
            
        elif direction == "right":
            self.main_piece.x = self.main_piece.x + SHIFT_right
            self.second_piece.x = self.second_piece.x + SHIFT_right
            self.third_piece.x = self.third_piece.x + SHIFT_right
            self.fourth_piece.x = self.fourth_piece.x + SHIFT_right

            self.left = self.left + SHIFT_right
            self.right = self.right + SHIFT_right

        self.main_piece.move_segment()
        self.second_piece.move_segment()
        self.third_piece.move_segment()
        self.fourth_piece.move_segment()

            
    def get_image(self):
        return "tPiece.png"


class O_piece (object):

    def __init__(self):
        self.main_piece = Segment(initial_x_pos, initial_y_pos, YELLOW)
        self.second_piece = Segment(self.main_piece.x + SHIFT_right, self.main_piece.y, YELLOW)
        self.third_piece = Segment(self.main_piece.x, self.main_piece.y + SHIFT_down, YELLOW)
        self.fourth_piece = Segment(self.main_piece.x + SHIFT_right, self.main_piece.y + SHIFT_down, YELLOW)

        self.left = self.main_piece.x
        self.right = self.second_piece.x + 25
        self.bottom = self.third_piece.y + 25
        
        self.orientation = "up"

    def changeOrientation(self):
        if self.orientation == "up":
            self.orientation = "right"
        elif self.orientation == "right":
            self.orientation = "down"
        elif self.orientation == "down":
            self.orientation = "left"
        elif self.orientation == "left":
            self.orientation = "up"

    def movePiece(self, direction):
        if direction == "down":
            self.main_piece.y = self.main_piece.y + SHIFT_down
            self.second_piece.y = self.second_piece.y + SHIFT_down
            self.third_piece.y = self.third_piece.y + SHIFT_down
            self.fourth_piece.y = self.fourth_piece.y + SHIFT_down

            self.bottom = self.bottom + SHIFT_down
            
        elif direction == "left":
            self.main_piece.x = self.main_piece.x + SHIFT_left
            self.second_piece.x = self.second_piece.x + SHIFT_left
            self.third_piece.x = self.third_piece.x + SHIFT_left
            self.fourth_piece.x = self.fourth_piece.x + SHIFT_left

            self.left = self.left + SHIFT_left
            self.right = self.right + SHIFT_left
            
        elif direction == "right":
            self.main_piece.x = self.main_piece.x + SHIFT_right
            self.second_piece.x = self.second_piece.x + SHIFT_right
            self.third_piece.x = self.third_piece.x + SHIFT_right
            self.fourth_piece.x = self.fourth_piece.x + SHIFT_right

            self.right = self.right + SHIFT_right
            self.left = self.left + SHIFT_right

        self.main_piece.move_segment()
        self.second_piece.move_segment()
        self.third_piece.move_segment()
        self.fourth_piece.move_segment()

    def get_image(self):
        return "oPiece.png"
            
class I_piece (object):

    def __init__(self):
        self.main_piece = Segment(initial_x_pos, initial_y_pos, CYAN)
        self.second_piece = Segment(self.main_piece.x + SHIFT_right, self.main_piece.y, CYAN)
        self.third_piece = Segment(self.main_piece.x + SHIFT_right * 2, self.main_piece.y, CYAN)
        self.fourth_piece = Segment(self.main_piece.x + SHIFT_right * 3, self.main_piece.y, CYAN)

        self.left = self.main_piece.x
        self.right = self.fourth_piece.x + 25
        self.bottom = self.fourth_piece.y + 25

        self.orientation = "up"

    def changeOrientation(self):
        if self.orientation == "up":
            self.orientation = "right"
        elif self.orientation == "right":
            self.orientation = "down"
        elif self.orientation == "down":
            self.orientation = "left"
        elif self.orientation == "left":
            self.orientation = "up"
        self.setOrientation()

    def setOrientation(self):
        if self.orientation == "up":
            self.main_piece.x = self.main_piece.x + SHIFT_left
            self.main_piece.y = self.main_piece.y + SHIFT_up * 2
            self.second_piece.y = self.second_piece.y + SHIFT_up
            self.third_piece.x = self.third_piece.x + SHIFT_right
            self.fourth_piece.x = self.fourth_piece.x + SHIFT_right * 2
            self.fourth_piece.y = self.fourth_piece.y + SHIFT_down

            self.left = self.main_piece.x
            self.right = self.fourth_piece.x + 25
            self.bottom = self.fourth_piece.y + 25
            
        elif self.orientation == "right":
            self.main_piece.x = self.main_piece.x + SHIFT_right * 2
            self.main_piece.y = self.main_piece.y + SHIFT_up
            self.second_piece.x = self.second_piece.x + SHIFT_right
            self.third_piece.y = self.third_piece.y + SHIFT_down
            self.fourth_piece.x = self.fourth_piece.x + SHIFT_left
            self.fourth_piece.y = self.fourth_piece.y + SHIFT_down * 2

            self.left = self.fourth_piece.x
            self.right = self.fourth_piece.x + 25
            self.bottom = self.fourth_piece.y + 25

            
        elif self.orientation == "down":
            self.main_piece.x = self.main_piece.x + SHIFT_right
            self.main_piece.y = self.main_piece.y + SHIFT_down * 2
            self.second_piece.y = self.second_piece.y + SHIFT_down
            self.third_piece.x = self.third_piece.x + SHIFT_left
            self.fourth_piece.x = self.fourth_piece.x + SHIFT_left * 2
            self.fourth_piece.y = self.fourth_piece.y + SHIFT_up

            self.left = self.fourth_piece.x
            self.right = self.main_piece.x + 25
            self.bottom = self.fourth_piece.y + 25

            
        elif self.orientation == "left":
            self.main_piece.x = self.main_piece.x + SHIFT_left * 2
            self.main_piece.y = self.main_piece.y + SHIFT_down
            self.second_piece.x = self.second_piece.x + SHIFT_left
            self.third_piece.y = self.third_piece.y + SHIFT_up
            self.fourth_piece.x = self.fourth_piece.x + SHIFT_right
            self.fourth_piece.y = self.fourth_piece.y + SHIFT_up * 2

            self.left = self.main_piece.x
            self.right = self.main_piece.x + 25
            self.bottom = self.main_piece.y + 25

        self.main_piece.move_segment()
        self.second_piece.move_segment()
        self.third_piece.move_segment()
        self.fourth_piece.move_segment()

        if self.left < 0:
            self.movePiece("right")
        elif self.right > 100:
            self.movePiece("left")


    def movePiece(self, direction):
        if direction == "down":
            self.main_piece.y = self.main_piece.y + SHIFT_down
            self.second_piece.y = self.second_piece.y + SHIFT_down
            self.third_piece.y = self.third_piece.y + SHIFT_down
            self.fourth_piece.y = self.fourth_piece.y + SHIFT_down

            self.bottom = self.bottom + SHIFT_down
            
        elif direction == "left":
            self.main_piece.x = self.main_piece.x + SHIFT_left
            self.second_piece.x = self.second_piece.x + SHIFT_left
            self.third_piece.x = self.third_piece.x + SHIFT_left
            self.fourth_piece.x = self.fourth_piece.x + SHIFT_left

            self.left = self.left + SHIFT_left
            self.right = self.right + SHIFT_left
            
        elif direction == "right":
            self.main_piece.x = self.main_piece.x + SHIFT_right
            self.second_piece.x = self.second_piece.x + SHIFT_right
            self.third_piece.x = self.third_piece.x + SHIFT_right
            self.fourth_piece.x = self.fourth_piece.x + SHIFT_right

            self.left = self.left + SHIFT_right
            self.right = self.right + SHIFT_right

        self.main_piece.move_segment()
        self.second_piece.move_segment()
        self.third_piece.move_segment()
        self.fourth_piece.move_segment()
            
    def get_image(self):
        return "iPiece.png"


class S_piece (object):

    def __init__(self):
        self.main_piece = Segment(initial_x_pos, initial_y_pos, GREEN)
        self.second_piece = Segment(self.main_piece.x + SHIFT_left, self.main_piece.y, GREEN)
        self.third_piece = Segment(self.main_piece.x, self.main_piece.y + SHIFT_up, GREEN)
        self.fourth_piece = Segment(self.main_piece.x + SHIFT_right, self.main_piece.y + SHIFT_up, GREEN)

        self.left = self.second_piece.x
        self.right = self.fourth_piece.x + 25
        self.bottom = self.second_piece.y + 25

        self.orientation = "up"

    def changeOrientation(self):
        if self.orientation == "up":
            self.orientation = "right"
        elif self.orientation == "right":
            self.orientation = "down"
        elif self.orientation == "down":
            self.orientation = "left"
        elif self.orientation == "left":
            self.orientation = "up"
        self.setOrientation()

    def setOrientation(self):
        if self.orientation == "up":
            self.second_piece.x = self.second_piece.x + SHIFT_left
            self.second_piece.y = self.second_piece.y + SHIFT_up
            self.third_piece.x = self.third_piece.x + SHIFT_right
            self.third_piece.y = self.third_piece.y + SHIFT_up
            self.fourth_piece.x = self.fourth_piece.x + SHIFT_right * 2

            self.left = self.second_piece.x
            self.right = self.fourth_piece.x + 25
            self.bottom = self.second_piece.y + 25
            
        elif self.orientation == "right":
            self.second_piece.x = self.second_piece.x + SHIFT_right
            self.second_piece.y = self.second_piece.y + SHIFT_up
            self.third_piece.x = self.third_piece.x + SHIFT_right
            self.third_piece.y = self.third_piece.y + SHIFT_down
            self.fourth_piece.y = self.fourth_piece.y + SHIFT_down * 2

            self.left = self.second_piece.x
            self.right = self.third_piece.x + 25
            self.bottom = self.fourth_piece.y + 25
            
        elif self.orientation == "down":
            self.second_piece.x = self.second_piece.x + SHIFT_right
            self.second_piece.y = self.second_piece.y + SHIFT_down
            self.third_piece.x = self.third_piece.x + SHIFT_left
            self.third_piece.y = self.third_piece.y + SHIFT_down
            self.fourth_piece.x = self.fourth_piece.x + SHIFT_left * 2

            self.left = self.fourth_piece.x
            self.right = self.third_piece.x + 25
            self.bottom = self.fourth_piece.y + 25
            
        elif self.orientation == "left":
            self.second_piece.x = self.second_piece.x + SHIFT_left
            self.second_piece.y = self.second_piece.y + SHIFT_down
            self.third_piece.x = self.third_piece.x + SHIFT_left
            self.third_piece.y = self.third_piece.y + SHIFT_up
            self.fourth_piece.y = self.fourth_piece.y + SHIFT_up * 2

            self.left = self.third_piece.x
            self.right = self.second_piece.x + 25
            self.bottom = self.second_piece.y + 25

        self.main_piece.move_segment()
        self.second_piece.move_segment()
        self.third_piece.move_segment()
        self.fourth_piece.move_segment()

        if self.left < 0:
            self.movePiece("right")
        elif self.right > 100:
            self.movePiece("left")


    def movePiece(self, direction):
        if direction == "down":
            self.main_piece.y = self.main_piece.y + SHIFT_down
            self.second_piece.y = self.second_piece.y + SHIFT_down
            self.third_piece.y = self.third_piece.y + SHIFT_down
            self.fourth_piece.y = self.fourth_piece.y + SHIFT_down

            self.bottom = self.bottom + SHIFT_down
            
        elif direction == "left":
            self.main_piece.x = self.main_piece.x + SHIFT_left
            self.second_piece.x = self.second_piece.x + SHIFT_left
            self.third_piece.x = self.third_piece.x + SHIFT_left
            self.fourth_piece.x = self.fourth_piece.x + SHIFT_left

            self.left = self.left + SHIFT_left
            self.right = self.right + SHIFT_left
            
        elif direction == "right":
            self.main_piece.x = self.main_piece.x + SHIFT_right
            self.second_piece.x = self.second_piece.x + SHIFT_right
            self.third_piece.x = self.third_piece.x + SHIFT_right
            self.fourth_piece.x = self.fourth_piece.x + SHIFT_right

            self.left = self.left + SHIFT_right
            self.right = self.right + SHIFT_right

        self.main_piece.move_segment()
        self.second_piece.move_segment()
        self.third_piece.move_segment()
        self.fourth_piece.move_segment()
            
    def get_image(self):
        return "sPiece.png"


class Z_piece (object):

    def __init__(self):
        self.main_piece = Segment(initial_x_pos, initial_y_pos, RED)
        self.second_piece = Segment(self.main_piece.x + SHIFT_left, self.main_piece.y + SHIFT_up, RED)
        self.third_piece = Segment(self.main_piece.x, self.main_piece.y + SHIFT_up, RED)
        self.fourth_piece = Segment(self.main_piece.x + SHIFT_right, self.main_piece.y, RED)

        self.left = self.second_piece.x
        self.right = self.fourth_piece.x + 25
        self.bottom = self.fourth_piece.y + 25

        self.orientation = "up"

    def changeOrientation(self):
        if self.orientation == "up":
            self.orientation = "right"
        elif self.orientation == "right":
            self.orientation = "down"
        elif self.orientation == "down":
            self.orientation = "left"
        elif self.orientation == "left":
            self.orientation = "up"
        self.setOrientation()

    def setOrientation(self):
        if self.orientation == "up":
            self.second_piece.y = self.second_piece.y + SHIFT_up * 2
            self.third_piece.x = self.third_piece.x + SHIFT_right
            self.third_piece.y = self.third_piece.y + SHIFT_up
            self.fourth_piece.x = self.fourth_piece.x + SHIFT_right
            self.fourth_piece.y = self.fourth_piece.y + SHIFT_down

            self.left = self.second_piece.x
            self.right = self.fourth_piece.x + 25
            self.bottom = self.fourth_piece.y + 25
            
        elif self.orientation == "right":
            self.second_piece.x = self.second_piece.x + SHIFT_right * 2
            self.third_piece.x = self.third_piece.x + SHIFT_right
            self.third_piece.y = self.third_piece.y + SHIFT_down
            self.fourth_piece.x = self.fourth_piece.x + SHIFT_left
            self.fourth_piece.y = self.fourth_piece.y + SHIFT_down

            self.left = self.fourth_piece.x
            self.right = self.second_piece.x + 25
            self.bottom = self.fourth_piece.y + 25
            
        elif self.orientation == "down":
            self.second_piece.y = self.second_piece.y + SHIFT_down * 2
            self.third_piece.x = self.third_piece.x + SHIFT_left
            self.third_piece.y = self.third_piece.y + SHIFT_down
            self.fourth_piece.x = self.fourth_piece.x + SHIFT_left
            self.fourth_piece.y = self.fourth_piece.y + SHIFT_up

            self.left = self.fourth_piece.x
            self.right = self.second_piece.x + 25
            self.bottom = self.second_piece.y + 25
            
        elif self.orientation == "left":
            self.second_piece.x = self.second_piece.x + SHIFT_left * 2
            self.third_piece.x = self.third_piece.x + SHIFT_left
            self.third_piece.y = self.third_piece.y + SHIFT_up
            self.fourth_piece.x = self.fourth_piece.x + SHIFT_right
            self.fourth_piece.y = self.fourth_piece.y + SHIFT_up

            self.left = self.second_piece.x
            self.right = self.fourth_piece.x + 25
            self.bottom = self.second_piece.y + 25

        self.main_piece.move_segment()
        self.second_piece.move_segment()
        self.third_piece.move_segment()
        self.fourth_piece.move_segment()

        if self.left < 0:
            self.movePiece("right")
        elif self.right > 100:
            self.movePiece("left")

    def movePiece(self, direction):
        if direction == "down":
            self.main_piece.y = self.main_piece.y + SHIFT_down
            self.second_piece.y = self.second_piece.y + SHIFT_down
            self.third_piece.y = self.third_piece.y + SHIFT_down
            self.fourth_piece.y = self.fourth_piece.y + SHIFT_down

            self.bottom = self.bottom + SHIFT_down
            
        elif direction == "left":
            self.main_piece.x = self.main_piece.x + SHIFT_left
            self.second_piece.x = self.second_piece.x + SHIFT_left
            self.third_piece.x = self.third_piece.x + SHIFT_left
            self.fourth_piece.x = self.fourth_piece.x + SHIFT_left

            self.left = self.left + SHIFT_left
            self.right = self.right + SHIFT_left
            
        elif direction == "right":
            self.main_piece.x = self.main_piece.x + SHIFT_right
            self.second_piece.x = self.second_piece.x + SHIFT_right
            self.third_piece.x = self.third_piece.x + SHIFT_right
            self.fourth_piece.x = self.fourth_piece.x + SHIFT_right

            self.left = self.left + SHIFT_right
            self.right = self.right + SHIFT_right

        self.main_piece.move_segment()
        self.second_piece.move_segment()
        self.third_piece.move_segment()
        self.fourth_piece.move_segment()

    def get_image(self):
        return "zPiece.png"
    

class J_piece (object):

    def __init__(self):
        self.main_piece = Segment(initial_x_pos, initial_y_pos, BLUE)
        self.second_piece = Segment(self.main_piece.x + SHIFT_left, self.main_piece.y + SHIFT_up, BLUE)
        self.third_piece = Segment(self.main_piece.x + SHIFT_left, self.main_piece.y, BLUE)
        self.fourth_piece = Segment(self.main_piece.x + SHIFT_right, self.main_piece.y, BLUE)

        self.left = self.third_piece.x
        self.right = self.fourth_piece.x + 25
        self.bottom = self.fourth_piece.y + 25

        self.orientation = "up"

    def changeOrientation(self):
        if self.orientation == "up":
            self.orientation = "right"
        elif self.orientation == "right":
            self.orientation = "down"
        elif self.orientation == "down":
            self.orientation = "left"
        elif self.orientation == "left":
            self.orientation = "up"
        self.setOrientation()

    def setOrientation(self):
        if self.orientation == "up":
            self.second_piece.y = self.second_piece.y + SHIFT_up * 2
            self.third_piece.x = self.third_piece.x + SHIFT_left
            self.third_piece.y = self.third_piece.y + SHIFT_up
            self.fourth_piece.x = self.fourth_piece.x + SHIFT_right
            self.fourth_piece.y = self.fourth_piece.y + SHIFT_down

            self.left = self.third_piece.x
            self.right = self.fourth_piece.x + 25
            self.bottom = self.fourth_piece.y + 25
            
        elif self.orientation == "right":
            self.second_piece.x = self.second_piece.x + SHIFT_right * 2
            self.third_piece.x = self.third_piece.x + SHIFT_right
            self.third_piece.y = self.third_piece.y + SHIFT_up
            self.fourth_piece.x = self.fourth_piece.x + SHIFT_left
            self.fourth_piece.y = self.fourth_piece.y + SHIFT_down

            self.left = self.fourth_piece.x
            self.right = self.second_piece.x + 25
            self.bottom = self.fourth_piece.y + 25
            
        elif self.orientation == "down":
            self.second_piece.y = self.second_piece.y + SHIFT_down * 2
            self.third_piece.x = self.third_piece.x + SHIFT_right
            self.third_piece.y = self.third_piece.y + SHIFT_down
            self.fourth_piece.x = self.fourth_piece.x + SHIFT_left
            self.fourth_piece.y = self.fourth_piece.y + SHIFT_up

            self.left = self.fourth_piece.x
            self.right = self.second_piece.x + 25
            self.bottom = self.second_piece.y + 25
            
        elif self.orientation == "left":
            self.second_piece.x = self.second_piece.x + SHIFT_left * 2
            self.third_piece.x = self.third_piece.x + SHIFT_left
            self.third_piece.y = self.third_piece.y + SHIFT_down
            self.fourth_piece.x = self.fourth_piece.x + SHIFT_right
            self.fourth_piece.y = self.fourth_piece.y + SHIFT_up

            self.left = self.second_piece.x
            self.right = self.third_piece.x + 25
            self.bottom = self.third_piece.y + 25

        self.main_piece.move_segment()
        self.second_piece.move_segment()
        self.third_piece.move_segment()
        self.fourth_piece.move_segment()

        if self.left < 0:
            self.movePiece("right")
        elif self.right > 100:
            self.movePiece("left")

    def movePiece(self, direction):
        if direction == "down":
            self.main_piece.y = self.main_piece.y + SHIFT_down
            self.second_piece.y = self.second_piece.y + SHIFT_down
            self.third_piece.y = self.third_piece.y + SHIFT_down
            self.fourth_piece.y = self.fourth_piece.y + SHIFT_down

            self.bottom = self.bottom + SHIFT_down
            
        elif direction == "left":
            self.main_piece.x = self.main_piece.x + SHIFT_left
            self.second_piece.x = self.second_piece.x + SHIFT_left
            self.third_piece.x = self.third_piece.x + SHIFT_left
            self.fourth_piece.x = self.fourth_piece.x + SHIFT_left

            self.left = self.left + SHIFT_left
            self.right = self.right + SHIFT_left
            
        elif direction == "right":
            self.main_piece.x = self.main_piece.x + SHIFT_right
            self.second_piece.x = self.second_piece.x + SHIFT_right
            self.third_piece.x = self.third_piece.x + SHIFT_right
            self.fourth_piece.x = self.fourth_piece.x + SHIFT_right

            self.left = self.left + SHIFT_right
            self.right = self.right + SHIFT_right

        self.main_piece.move_segment()
        self.second_piece.move_segment()
        self.third_piece.move_segment()
        self.fourth_piece.move_segment()
            
    def get_image(self):
        return "jPiece.png"
    

class L_piece (object):

    def __init__(self):
        self.main_piece = Segment(initial_x_pos, initial_y_pos, ORANGE)
        self.second_piece = Segment(self.main_piece.x + SHIFT_left, self.main_piece.y, ORANGE)
        self.third_piece = Segment(self.main_piece.x + SHIFT_right, self.main_piece.y, ORANGE)
        self.fourth_piece = Segment(self.main_piece.x + SHIFT_right, self.main_piece.y + SHIFT_up, ORANGE)

        self.left = self.second_piece.x
        self.right = self.third_piece.x + 25
        self.bottom = self.third_piece.y + 25


        self.orientation = "up"

    def changeOrientation(self):
        if self.orientation == "up":
            self.orientation = "right"
        elif self.orientation == "right":
            self.orientation = "down"
        elif self.orientation == "down":
            self.orientation = "left"
        elif self.orientation == "left":
            self.orientation = "up"
        self.setOrientation()

    def setOrientation(self):
        if self.orientation == "up":
            self.second_piece.x = self.second_piece.x + SHIFT_left
            self.second_piece.y = self.second_piece.y + SHIFT_up
            self.third_piece.x = self.third_piece.x + SHIFT_right
            self.third_piece.y = self.third_piece.y + SHIFT_down
            self.fourth_piece.x = self.fourth_piece.x + SHIFT_right * 2

            self.left = self.second_piece.x
            self.right = self.third_piece.x + 25
            self.bottom = self.third_piece.y + 25

        elif self.orientation == "right":
            self.second_piece.x = self.second_piece.x + SHIFT_right
            self.second_piece.y = self.second_piece.y + SHIFT_up
            self.third_piece.x = self.third_piece.x + SHIFT_left
            self.third_piece.y = self.third_piece.y + SHIFT_down
            self.fourth_piece.y = self.fourth_piece.y + SHIFT_down * 2

            self.left = self.third_piece.x
            self.right = self.fourth_piece.x + 25
            self.bottom = self.fourth_piece.y + 25
            
        elif self.orientation == "down":
            self.second_piece.x = self.second_piece.x + SHIFT_right
            self.second_piece.y = self.second_piece.y + SHIFT_down
            self.third_piece.x = self.third_piece.x + SHIFT_left
            self.third_piece.y = self.third_piece.y + SHIFT_up
            self.fourth_piece.x = self.fourth_piece.x + SHIFT_left * 2

            self.left = self.fourth_piece.x
            self.right = self.second_piece.x + 25
            self.bottom = self.fourth_piece.y + 25
            
        elif self.orientation == "left":
            self.second_piece.x = self.second_piece.x + SHIFT_left
            self.second_piece.y = self.second_piece.y + SHIFT_down
            self.third_piece.x = self.third_piece.x + SHIFT_right
            self.third_piece.y = self.third_piece.y + SHIFT_up
            self.fourth_piece.y = self.fourth_piece.y + SHIFT_up * 2

            self.left = self.fourth_piece.x
            self.right = self.second_piece.x + 25
            self.bottom = self.second_piece.y + 25

        self.main_piece.move_segment()
        self.second_piece.move_segment()
        self.third_piece.move_segment()
        self.fourth_piece.move_segment()

        if self.left < 0:
            self.movePiece("right")
        elif self.right > 100:
            self.movePiece("left")
            

    def movePiece(self, direction):
        if direction == "down":
            self.main_piece.y = self.main_piece.y + SHIFT_down
            self.second_piece.y = self.second_piece.y + SHIFT_down
            self.third_piece.y = self.third_piece.y + SHIFT_down
            self.fourth_piece.y = self.fourth_piece.y + SHIFT_down

            self.bottom = self.bottom + SHIFT_down
            
        elif direction == "left":
            self.main_piece.x = self.main_piece.x + SHIFT_left
            self.second_piece.x = self.second_piece.x + SHIFT_left
            self.third_piece.x = self.third_piece.x + SHIFT_left
            self.fourth_piece.x = self.fourth_piece.x + SHIFT_left

            self.left = self.left + SHIFT_left
            self.right = self.right + SHIFT_left
            
        elif direction == "right":
            self.main_piece.x = self.main_piece.x + SHIFT_right
            self.second_piece.x = self.second_piece.x + SHIFT_right
            self.third_piece.x = self.third_piece.x + SHIFT_right
            self.fourth_piece.x = self.fourth_piece.x + SHIFT_right

            self.left = self.left + SHIFT_right
            self.right = self.right + SHIFT_right

        self.main_piece.move_segment()
        self.second_piece.move_segment()
        self.third_piece.move_segment()
        self.fourth_piece.move_segment()
            
    def get_image(self):
        return "lPiece.png"