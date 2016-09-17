from highScoreHandler import *

class Game_score(object):

    def __init__(self):
        self.score = 0
        self.line = 100
        self.name = "TMP"
        
        self.two = 1.5
        self.three = 2
        self.four = 4
        
        
    def calc_score(self, score_counter):
        
        if score_counter == 1:
            self.score += self.line
        elif score_counter == 2:
            self.score += self.line * self.two
        elif score_counter == 3:
            self.score += self.line * self.three
        elif score_counter == 4:
            self.score += self.line * self.four
        
    def set_high_score(self):
        addScoreToList(currentPlayer, loadScores())
    
    def reset_scores(self):
        self.score = 0
        self.name = "TMP"
    
        
        
    #The highscore code here for gameover condition
    #[[500, "AAA"],[400, "BBB"],[300, "CCC"],[200, "DDD"],[100, "EEE"]]