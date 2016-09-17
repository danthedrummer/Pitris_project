import pygame, sys
from pygame import *
from highScoreHandler import *
import pickle

high_scores = loadScores()

pygame.init()

def drawHighScore(highScoreList, x, y):
    FONT = pygame.font.SysFont("monospace", 25)#creats a font object
    SURFACEFONT = FONT.render("TOP 5!", True,white,black)
    SURFACE = SURFACEFONT.get_rect() # this will be a rectangle value
    SURFACE =(x+25,y)
    screen.blit(SURFACEFONT, SURFACE)
    
    for z in highScoreList:# goes through the list takes displays it
        y+=50
        FONT = pygame.font.SysFont("monospace", 20)#creats a font object
        SURFACEFONT = FONT.render(z[1]+"    "+str(z[0]), True,white,black)
        SURFACE = SURFACEFONT.get_rect() # this will be a rectangle value
        SURFACE =(x,y)
        screen.blit(SURFACEFONT, SURFACE)

def drawMenuButtons(): #function that draws the menu buttons
    if True:# check if new game is selected
        #if 15 <= ultrasonic <=30 (this is the shorthand of the ranger working) 
        newGameButton = pygame.draw.rect(screen, WHITE, [300, 80, 60, 30], 0)
        screen.blit(pygame.image.load("img/newGameSelected.png"), newGameButton)
            #if button = 1:"true or pressed"
            #menuFlag=False
            #gameMenu=True
        
    else:
        newGameButton = pygame.draw.rect(screen, WHITE, [300, 80, 60, 30], 0)
        screen.blit(pygame.image.load("img/newGameUnselected.png"), newGameButton)

    if False:# check if quit game is selected
        #if 0 <= ultrasonic <=15 (this is the shorthand of the ranger working)
        quitGameButton = pygame.draw.rect(screen, WHITE, [300, 380, 60, 30], 0)
        screen.blit(pygame.image.load("img/quitGameSelected.png"), quitGameButton)
            #if button = 1:"true or pressed"
                #pygame.quit()
                #sys.exit()

    else:    
        quitGameButton = pygame.draw.rect(screen, WHITE, [300, 380, 60, 30], 0)
        screen.blit(pygame.image.load("img/quitGameUnselected.png"), quitGameButton)
    
    
    

width = 790

height = 540

title = pygame.display.set_caption("PI Tetris")

screen = pygame.display.set_mode((width,height))

GameImage = pygame.image.load("img/background.png")
screen.blit(GameImage,(0,0))
pygame.display.update()

red = (230,50,50)
white = (255,255,255)
black = (0,0,0)
menuFlag = True





while True:
    for event in pygame.event.get():
        if pygame.key.get_pressed()[pygame.K_SPACE] != 0:
            menuFlag=False
            print "HEY!"
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    if menuFlag:
        
        

        drawHighScore(high_scores, 600, 100)

        pygame.draw.rect(screen, WHITE, [350, 100, 60, 30], 0)

        drawMenuButtons()

    

        pygame.display.update()

    else:

        pygame.draw.rect(screen, RED, [350, 100, 500, 500], 0)
        pygame.display.update()
        
