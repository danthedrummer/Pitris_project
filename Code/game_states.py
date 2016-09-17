import random
from room_levels import *

class Game_state(object):
    
    def __init__(self):
        self.normal_state = True
        self.frozen_state = False
        self.sleep_state = False
        self.bright_state = False
        self.menu_state = True
        self.game_over = False
        
        self.temp_avg = get_room_temp(7)
        self.sound_avg = get_room_sound_level(0)
        self.light_avg = get_room_light_level(1)
        
        
    def change_state(self):
        self.reset_states()
        self.normal_state = False
        num = random.randint(0, 2)
        if num == 0:
            self.frozen_state = True
        elif num == 1:
            self.sleep_state = True
        else:
            self.bright_state = True

    
    def state_image(self):
        if self.menu_state:
            return "menu_bg_image.png"
        elif self.frozen_state:
            return "frozen_bg_image.png"
        elif self.sleep_state:
            return "sleep_bg_image.png"
        elif self.bright_state:
            return "bright_bg_image.png"
        else:
            return "normal_bg_image.png"
    
    
    def defeat_state(self, sensor_reading):
        if self.frozen_state:
            if sensor_reading >= self.temp_avg + 4.5:
                self.reset_states()
        elif self.sleep_state:
            if sensor_reading >= self.sound_avg + 100:
                self.reset_states()
        elif self.bright_state:
            if sensor_reading <= self.light_avg + 75:
                self.reset_states()
    

    def reset_states(self):
        self.normal_state = True
        self.frozen_state = False
        self.sleep_state = False
        self.bright_state = False
        self.menu_state = False
        self.game_over = False
    