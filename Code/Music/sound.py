def musicPlayer(currentTheme):
	pygame.mixer.music.load(songList[currentTheme])
	pygame.mixer.music.play()
	
import sys, pygame
pygame.init() #Initialises pygame

#Sets event codes (Anything above 24 can be used)
eventCodes = {'SONGEND': 36}

#Handles the initial setup for the music
currentTheme = 'themeA'
songList = {'themeA': 'Tetris.mp3', 
			'themeB': 'Hep Cats.mp3', 
			'themeC': 'The Complex.mp3', 
			'themeD': 'The Show Must Be Go.mp3', }
pygame.mixer.music.set_endevent(eventCodes['SONGEND'])
musicPlayer(currentTheme)

screen = pygame.display.set_mode((800, 600))	#Creates a screen with the set size and displays it

while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()
		#Catches the event that fires when the current song ends
		if event.type == eventCodes['SONGEND']: musicPlayer(currentTheme)
		#Alternates between the themes
		#Uses space key to swap between songs for now until we have an options screen
		if pygame.key.get_pressed()[pygame.K_SPACE] != 0:
			if currentTheme == 'themeA':
				currentTheme = 'themeB'
				musicPlayer(currentTheme)
			elif currentTheme == 'themeB':
				currentTheme = 'themeC'
				musicPlayer(currentTheme)
			elif currentTheme == 'themeC':
				currentTheme = 'themeD'
				musicPlayer(currentTheme)
			elif currentTheme == 'themeD':
				currentTheme = 'themeA'
				musicPlayer(currentTheme)
				
	screen.fill((0,0,0))