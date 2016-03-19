from sense_hat import SenseHat
import pygame.mixer

import time

pygame.mixer.init()
def audio(music):
    pygame.mixer.music.load(music)
    pygame.mixer.music.play(1)
    

sense = SenseHat()
#sense.show_message("Ready to party!!", text_colour=[255,255,0])
cold = "./music/loop_amen.wav"
hot = "./music/loop_industrial.wav"
while True:
    temperature = sense.get_temperature()
    print(round(temperature))
    time.sleep(1)
    if round(temperature) < 33:
        audio(cold)
        sense.show_message("COLD", scroll_speed=0.03,text_colour=[0,0,255])
    elif round(temperature) == 33:
        audio(hot)
        sense.show_message("HOT", scroll_speed=0.03, text_colour=[255,0,0])
        
        
