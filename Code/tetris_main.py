from grovepi import analogRead
import sys, pygame, grovepi, time, random
from room_levels import *
from game_pieces import *
from game_board import *
from game_score import *
pygame.init()

# Screen Attributes
size = width, height = 750, 500
game_area = gWidth, gHeight = 250, 500
game_boundaries = gLeft, gRight, gTop, gBottom = 250, 500, 0, 500

# colour RGB values
BLACK = 0, 0, 0
WHITE = 255, 255, 255
GREEN = 0, 255, 0
BLUE = 0, 0, 255
RED = 255, 0, 0

# directions
DOWN = 25
UP = -25
LEFT = -25
RIGHT = 25

# Boolean to determine whether to call functions appropriate to the piece having been placed
placed = False

# boolean for whether the gme has ended
game_over = False

# Connect the Grove Button to digital PORT D3
button = 3
grovepi.pinMode(button,"INPUT")

# Temperature and humidity sensor PORT D7
dht_sensor_port = 7

# Ultrasonic Ranger PORT D4
ultrasonic_ranger = 4

# Shound sensor PORT A0
sound_sensor = 0
grovepi.pinMode(sound_sensor, "INPUT")

# Light Sensor PORT A1
light_sensor = 1
grovepi.pinMode(light_sensor, "INPUT")

# Analog Shtick PORT A2
x_pin = 2
grovepi.pinMode(x_pin, "INPUT")

# Set Screen Size and Colour
screen = pygame.display.set_mode(size)
screen.fill(BLACK)

#Instance of game score for tracking players score for the current session
cur_player_score = Game_score()

board_tiles = build_game_area()

cur_piece = random_piece()
next_piece = random_piece()

highScoreList = loadScores()

cur_img = pygame.image.load(cur_piece.get_image()).convert()
next_img = pygame.image.load(next_piece.get_image()).convert()

clock = pygame.time.Clock()

while True:
        try:
                screen.fill(BLACK)
        
                while menu_state:
                        
                        screen.fill(BLACK)
                        screen.blit(bg_img, bg_rect)
                        
                        x = 600
                        y = 100
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
                        
                        hand = ultrasonicRead(ultrasonic_ranger)
                        
                        if hand > 16 and hand < 22:
                                newGameButton = pygame.draw.rect(screen, WHITE, [300, 80, 60, 30], 0)
                                screen.blit(pygame.image.load("newGameSelected.png"), newGameButton)
                                
                                if button:
                                        state.menu_state = False
                        else:
                                newGameButton = pygame.draw.rect(screen, WHITE, [300, 80, 60, 30], 0)
                                screen.blit(pygame.image.load("newGameUnselected.png"), newGameButton)
                                
                        if hand > 6 and hand < 12:
                                quitGameButton = pygame.draw.rect(screen, WHITE, [300, 380, 60, 30], 0)
                                screen.blit(pygame.image.load("quitGameSelected.png"), quitGameButton)
                                
                                if button:
                                        pygame.quit()
                                        sys.exit()
                        else:    
                                quitGameButton = pygame.draw.rect(screen, WHITE, [300, 380, 60, 30], 0)
                                screen.blit(pygame.image.load("img/quitGameUnselected.png"), quitGameButton)
                                
                        pygame.display.flip()
                        

                curOne = pygame.draw.rect(screen, cur_piece.main_piece.colour, [cur_piece.main_piece.x, cur_piece.main_piece.y, 25, 25], 0)               
                curTwo = pygame.draw.rect(screen, cur_piece.second_piece.colour, [cur_piece.second_piece.x, cur_piece.second_piece.y, 25, 25], 0)
                curThree = pygame.draw.rect(screen, cur_piece.third_piece.colour, [cur_piece.third_piece.x, cur_piece.third_piece.y, 25, 25], 0)
                curFour = pygame.draw.rect(screen, cur_piece.fourth_piece.colour, [cur_piece.fourth_piece.x, cur_piece.fourth_piece.y, 25, 25], 0)
                
                next_one = pygame.draw.rect(screen, next_piece.main_piece.colour, [next_piece.main_piece.x - 250, next_piece.main_piece.y + 250, 25, 25], 0)               
                next_two = pygame.draw.rect(screen, next_piece.second_piece.colour, [next_piece.second_piece.x - 250, next_piece.second_piece.y + 250, 25, 25], 0)
                next_three = pygame.draw.rect(screen, next_piece.third_piece.colour, [next_piece.third_piece.x - 250, next_piece.third_piece.y + 250, 25, 25], 0)
                next_four = pygame.draw.rect(screen, next_piece.fourth_piece.colour, [next_piece.fourth_piece.x - 250, next_piece.fourth_piece.y + 250, 25, 25], 0)
                
                
                for event in pygame.event.get():
                    if event.type == pygame.QUIT: sys.exit()

                    if event.type == pygame.KEYDOWN:
                        k_down = event.key
                        if k_down == pygame.K_UP:
                                if not placed:
                                        cur_piece.changeOrientation()

##                        if k_down == pygame.K_DOWN:            
##                              print "0, 25"

                        if k_down == pygame.K_LEFT:
                                if not placed:
                                        if cur_piece.left > gLeft and cur_piece.left != gLeft:
                                                if not board_tiles[cur_piece.main_piece.x_grid - 1][cur_piece.main_piece.y_grid].active and not board_tiles[cur_piece.second_piece.x_grid - 1][cur_piece.second_piece.y_grid].active and not board_tiles[cur_piece.third_piece.x_grid - 1][cur_piece.third_piece.y_grid].active and not board_tiles[cur_piece.fourth_piece.x_grid - 1][cur_piece.fourth_piece.y_grid].active:
                                                        cur_piece.movePiece("left")

                        if k_down == pygame.K_RIGHT:
                                if not placed:
                                        if cur_piece.right <  gRight and cur_piece.right != gRight:
                                                if not board_tiles[cur_piece.main_piece.x_grid + 1][cur_piece.main_piece.y_grid].active and not board_tiles[cur_piece.second_piece.x_grid + 1][cur_piece.second_piece.y_grid].active and not board_tiles[cur_piece.third_piece.x_grid + 1][cur_piece.third_piece.y_grid].active and not board_tiles[cur_piece.fourth_piece.x_grid + 1][cur_piece.fourth_piece.y_grid].active:
                                                        cur_piece.movePiece("right")


                for x in range(10):
                    for y in range(21):
                        if board_tiles[x][y].active:
                                if board_tiles[cur_piece.main_piece.x_grid][cur_piece.main_piece.y_grid + 1].active or board_tiles[cur_piece.second_piece.x_grid][cur_piece.second_piece.y_grid + 1].active or board_tiles[cur_piece.third_piece.x_grid][cur_piece.third_piece.y_grid + 1].active or board_tiles[cur_piece.fourth_piece.x_grid][cur_piece.fourth_piece.y_grid + 1].active:
                                        board_tiles[cur_piece.main_piece.x_grid][cur_piece.main_piece.y_grid].active = True
                                        board_tiles[cur_piece.second_piece.x_grid][cur_piece.second_piece.y_grid].active = True
                                        board_tiles[cur_piece.third_piece.x_grid][cur_piece.third_piece.y_grid].active = True
                                        board_tiles[cur_piece.fourth_piece.x_grid][cur_piece.fourth_piece.y_grid].active = True

                                        board_tiles[cur_piece.main_piece.x_grid][cur_piece.main_piece.y_grid].image = cur_img
                                        board_tiles[cur_piece.second_piece.x_grid][cur_piece.second_piece.y_grid].image = cur_img
                                        board_tiles[cur_piece.third_piece.x_grid][cur_piece.third_piece.y_grid].image = cur_img
                                        board_tiles[cur_piece.fourth_piece.x_grid][cur_piece.fourth_piece.y_grid].image = cur_img
                                        
                                        cur_piece = next_piece
                                        next_piece = random_piece()
                                        placed = True


                if cur_piece.bottom == gBottom or cur_piece.bottom > gBottom:
                        board_tiles[cur_piece.main_piece.x_grid][cur_piece.main_piece.y_grid].active = True
                        board_tiles[cur_piece.second_piece.x_grid][cur_piece.second_piece.y_grid].active = True
                        board_tiles[cur_piece.third_piece.x_grid][cur_piece.third_piece.y_grid].active = True
                        board_tiles[cur_piece.fourth_piece.x_grid][cur_piece.fourth_piece.y_grid].active = True

                        board_tiles[cur_piece.main_piece.x_grid][cur_piece.main_piece.y_grid].image = cur_img
                        board_tiles[cur_piece.second_piece.x_grid][cur_piece.second_piece.y_grid].image = cur_img
                        board_tiles[cur_piece.third_piece.x_grid][cur_piece.third_piece.y_grid].image = cur_img
                        board_tiles[cur_piece.fourth_piece.x_grid][cur_piece.fourth_piece.y_grid].image = cur_img
                        
                        cur_piece = next_piece
                        next_piece = random_piece()
                        placed = True

                for x in range(10):
                    for y in range(21):
                        if board_tiles[x][y].active:
                            screen.blit(board_tiles[x][y].image, pygame.draw.rect(screen, WHITE, [board_tiles[x][y].x_pos, board_tiles[x][y].y_pos, 25, 25], 0))

                if placed:
                        score_counter = 0
                        for y in range(21):
                                counter = 0
                                for x in range(10):
                                        if not board_tiles[x][y].active:
                                                x = 9
                                        else:
                                                counter += 1
                                                
                                                if counter == 10:
                                                        score_counter += 1

                                                        for new_y in range(y, -1, -1):
                                                                for x in range(10):
                                                                        board_tiles[x][new_y].active = board_tiles[x][new_y-1].active
                                                                        board_tiles[x][new_y].image = board_tiles[x][new_y-1].image
                calc_score(score_counter)
                score_font = pygame.font.SysFont("monospace", 15)
                score_label = score_font.render(cur_player_score.score, 1, (255,255,0))
                
                
                if not state.game_over:
                        cur_piece.movePiece("down")
                else:
                        # Need code for allowing player to input 3 CHAR name
                        #
                        
                        while state.game_over:
                                screen.fill(BLACK)
                                screen.blit(pygame.image.load("menu_bg_image.png"), bg_rect)
                                g_o_font = pygame.font.SysFont("monospace", 50)
                                first_g_o_label = score_font.render(g_o.get_cur_letter(1), 1, (g_o.is_in_focus(g_o.first_letter_focus)))
                                second_g_o_label = score_font.render(g_o.get_cur_letter(2), 1, (g_o.is_in_focus(g_o.second_letter_focus)))
                                third_g_o_label = score_font.render(g_o.get_cur_letter(3), 1, (g_o.is_in_focus(g_o.third_letter_focus)))
                                enter_g_o_label = score_font.render(g_o.get_cur_letter(4), 1, (g_o.is_in_focus(g_o.enter_button_focus)))
                                
                                try:
                                        direction = analogRead()
                                except IOError:
                                        print "Analog error"
                                        
                                try:
                                        button_status = digitalRead(button)
                                except IOError:
                                        print "Button error"
                                
                                if direction < 505:
                                        move_focus("left")
                                elif direction > 520:
                                        move_focus("right")
                                        
                                if button and g_o.is_in_focus(g_o.enter_button_focus):
                                        cur_player_score.name = g_o.get_cur_letter(1) + g_o.get_cur_letter(2) + g_o.get_cur_letter(3)
                                        addScoreToList([cur_player_score.score, cur_player_score.name])
                                        highScoreList = loadScores()
                                        state.game_over = False
                                        state.reset_states()
                                elif button:
                                        g_o.move_letter()
                                        
                                screen.blit(first_g_o_label, (285, 200))
                                screen.blit(second_g_o_label, (345, 200))
                                screen.blit(third_g_o_label, (405, 200))
                                screen.blit(enter_g_o_label, (335, 375))
                        
                        



                screen.blit(label, (100, 400))
                
                screen.blit(cur_img, curOne)
                screen.blit(cur_img, curTwo)
                screen.blit(cur_img, curThree)
                screen.blit(cur_img, curFour)
                
                screen.blit(next_img, next_one)
                screen.blit(next_img, next_two)
                screen.blit(next_img, next_three)
                screen.blit(next_img, next_four)

                if placed:
                        cur_img = pygame.image.load(cur_piece.get_image()).convert()
                        next_img = pygame.image.load(next_piece.get_image()).convert()
                        placed = False

##                if not rect_list:
                pygame.display.flip()
##                else:
##                        pygame.display.flip()
##                        pygame.display.update(rect_list)


                time.sleep(.1)
                
        except IOError:
                print ("Error")