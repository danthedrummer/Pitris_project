
from grovepi import *
import sys, grovepi

def get_room_temp(port):
        avg_temp = 0
        counter = 0
        
        try:
                while counter < 8:
                        [ temp, hum ] = dht(port, 0)
                        avg_temp = avg_temp + temp
                        counter = counter + 1

                return avg_temp / 8

        except IOError:
                print ("TEMP error")


def get_room_sound_level(port):
        avg_sound = 0
        counter = 0
        
        try:
                while counter < 8:
                        sensor_value = grovepi.analogRead(port)
                        avg_sound = avg_sound + sensor_value
                        counter = counter + 1

                return avg_sound / 8

        except IOError:
                print("SOUND error")


def get_room_light_level(port):
        avg_light = 0
        counter = 0

        try:
                while counter < 8:
                        sensor_value = grovepi.analogRead(port)
                        avg_light = avg_light + sensor_value
                        counter = counter + 1

                return avg_light / 8

        except IOError:
                print("LIGHT error")