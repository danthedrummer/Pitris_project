import sys, pygame
pygame.init() #Initialises pygame

size = width, height = 400, 600    #Sets the size of the game window
speed = [2, 2]    #Speed of the horizontal and vertical movement
black = 0, 0, 0    #Sets the colour of the background

screen = pygame.display.set_mode(size)    #Creates a screen with the set size and displays it

ball = pygame.image.load("ball.gif")    #Loads in an image
ballRect = ball.get_rect()    #Gets the bounding rectangle of the image

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        
    ballRect = ballRect.move(speed)
    if ballRect.left < 0 or ballRect.right > width:
        speed[0] = -speed[0]
    if ballRect.top < 0 or ballRect.bottom > height:
        speed[1] = -speed[1]
        
    screen.fill(black)
    screen.blit(ball, ballRect)
    pygame.display.flip()