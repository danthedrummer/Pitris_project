#Saves the high score list to a file
#If no argument is passed then the file written will be empty (Clears the list)
def storeScores(highScores = []):
    scoreFile = open('HighScores.pckl', 'w')
    if highScores == []:
        pickle.dump(getDefaultScoreList(), scoreFile)
    else:
        pickle.dump(highScores, scoreFile)  
    scoreFile.close()

#Loads the high score list from a file
def loadScores():
    if os.path.exists("HighScores.pckl"):
        try:
            scoreFile = open('HighScores.pckl', 'rb')
            highScores = pickle.load(scoreFile)
            scoreFile.close()
        #If the file is empty then return a set of default scores 
        except EOFError:    
            print "File empty\nSetting default values"
            return sortHighScores(getDefaultScoreList())
        return highScores
    else:
        #If the highscore file does not exist then return a set of default scores
        return sortHighScores(getDefaultScoreList())

#Returns default score list
def getDefaultScoreList():
    return [[500, "AAA"],[400, "BBB"],[300, "CCC"],[200, "DDD"],[100, "EEE"]] 

#Adds the current players score to the high score list 
#and sends it to be written to a file
def addScoreToList(currentPlayer):
    highScores.append(currentPlayer)
    storeScores(sortHighScores(loadScores()))

#Sorts the high score list passed in and displays the top 5 scores 
def sortHighScores(high_scores):
    high_scores.sort(reverse=True)
    return high_scores[:5]
    
#Returns the player's Score
def getPlayerScore():
    try:
        return int(raw_input("What was your score?"))
    except:
        print "Sorry, I need you to enter a number!"
    
#Returns the player's name
def getPlayerName():
    name = ""
    while name == "" or len(name) != 3:  #Will keep asking for a name until it is 3 characters long
        try:
            name = raw_input("What is your name? (3 letters)")
            if len(name) == 3:  #Will only accept a name that is 3 characters exactly
                break
            else:               #Otherwise it will pop a message and try get input again
                print "Sorry, your name must be 3 letters!"
        except:
            print "Sorry, I don't understand that!"
    return name
import pickle, os
from game_score import *

##Takes in the current players name and score
##Should be updated to only take in the users name with whatever score they achieve##


cur_player = Game_score()

# currentPlayer = [getPlayerScore(), getPlayerName()]
            #The score they get, the name they choose
addScoreToList(currentPlayer)

##Whatever the high score screen needs
print "\n\nTop 5!\n" + str(loadScores())