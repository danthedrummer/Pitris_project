import sys, pygame
pygame.init() #Initialises pygame

size = width, height = 400, 800	#Sets the size of the game window
fall_speed = [0, 1]	#Speed of the horizontal and vertical movement
BLACK = 0, 0, 0
GREEN = 0, 255, 0

screen = pygame.display.set_mode(size)	#Creates a screen with the set size and displays it

square = pygame.image.load('square_piece.png')
piece = pygame.draw.rect(screen, GREEN, [50, 10, 10, 10], 0)

game_pieces = []

pygame.key.set_repeat(50, 50) # If player holds down left or riht arroe

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
            k_down = event.key
            if k_down == pygame.K_LEFT:
                piece = piece.move(-1, 0)
            elif k_down == pygame.K_RIGHT:
                piece = piece.move(1, 0)
        
    for piece in game_pieces:
        if piece.bottom > height:
            fall_speed[1] = 0
        
    piece = piece.move(fall_speed)
    screen.fill(BLACK)
    screen.blit(square, piece)
    pygame.display.flip()
    
# 	if ballRect.left < 0 or ballRect.right > width:
# 		speed[0] = -speed[0]
# 	if ballRect.top < 0 or ballRect.bottom > height:
# 		speed[1] = -speed[1]
