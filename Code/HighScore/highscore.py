def get_high_score():
    # Default high score
    high_score = ""
 
    # Try to read the high score from a file
    try:
        high_score_file = open("high_score.txt", "r")
        high_score = high_score_file.read()
        high_score_file.close()
        print("The high score is", high_score)
    except IOError:
        # Error reading file, no high score
        print("There is no high score yet.")
    except ValueError:
        # There's a file there, but we don't understand the number.
        print("I'm confused. Starting with no high score.")
 
    return high_score
 # pyuic4 -o OutFile_ui.py InFile.ui

def save_high_score(new_high_score):
    highScore = get_high_score()
    try:
        if highScore != "":
            # Write the file to disk
            high_score_file = open("high_score.txt", "w")
            high_score_file.write(highScore + "\n" + new_high_score)
            high_score_file.close()
        else:
            # Write the file to disk
            high_score_file = open("high_score.txt", "w")
            high_score_file.write(str(new_high_score))
            high_score_file.close()
    except IOError:
        # can't write it.
        print("Unable to save the high score.")
 
 
def main():
    """ Main program is here. """
    # Get the high score
    high_score = get_high_score()
 
    # Get teh user name
    current_name = ""
    # Get the score from the current game
    current_score = 0
    try:
        # Ask the user for their name
        current_name = raw_input("What is your name?")
        # Ask the user for score
        current_score = int(input("What is your score? "))
    except ValueError:
        # Error, can't turn what they typed into a number
        print("I don't understand what you typed.")
        
    save_high_score(current_name + " " + str(current_score))
    
    # See if we have a new high score
    """if current_score > high_score:
        # We do! Save to disk
        print("Yea! New high score!")
        save_high_score(current_name + " " + str(current_score))
    else:
        print("Better luck next time.")"""
 
# Call the main function, start up the game
if __name__ == "__main__":
    main()
