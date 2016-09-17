
YELLOW = 255, 255, 0
RED = 255, 0, 0

class Game_over (object):
    
    def __init__(self):
        self.first_letter_focus = True
        self.second_letter_focus = False
        self.third_letter_focus = False
        self.enter_button_focus = False
        
        self.letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "Q", "X", "Y", "Z"]
        self.first_cur_letter = 0
        self.second_cur_letter = 0
        self.third_cur_letter = 0
        self.first_next_letter = 1
        self.second_next_letter = 1
        self.third_next_letter = 1
        
    def move_focus(self, direction):
        if direction == "right":
            if self.first_letter_focus:
                self.first_letter_focus = False
                self.second_letter_focus = True
            elif self.second_letter_focus:
                self.second_letter_focus = False
                self.third_letter_focus = True
            elif self.third_letter_focus:
                self.third_letter_focus = False
                self.enter_button_focus = True
            else:
                self.enter_button_focus = False
                self.first_letter_focus = True
        else:
            if self.first_letter_focus:
                self.first_letter_focus = False
                self.enter_button_focus = True
            elif self.second_letter_focus:
                self.second_letter_focus = False
                self.first_letter_focus = True
            elif self.third_letter_focus:
                self.third_letter_focus = False
                self.second_letter_focus = True
            else:
                self.enter_button_focus = False
                self.third_letter_focus = True
    
    def move_letter(self):
        if self.first_letter_focus:
            self.first_cur_letter = self.first_next_letter
            self.first_next_letter += 1
            if self.first_next_letter == 26:
                self.first_next_letter = 0
        elif self.second_letter_focus:
            self.second_cur_letter = self.second_next_letter
            self.second_next_letter += 1
            if self.second_next_letter == 26:
                self.second_next_letter = 0
        elif self.third_letter_focus:
            self.third_cur_letter = self.third_next_letter
            self.third_next_letter += 1
            if self.third_next_letter == 26:
                self.third_next_letter = 0
    
    def get_cur_letter(self, place):
        if place == 1:
            return self.letters[self.first_cur_letter]
        elif place == 2:
            return self.letters[self.second_cur_letter]    
        elif place == 3:
            return self.letters[self.third_cur_letter]
        elif place == 4:
            return "ENTER"
        
    
    def is_in_focus(self, focus):
        if focus:
            return RED
        else:
            return YELLOW