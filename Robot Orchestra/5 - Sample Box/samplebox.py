"""
Samplebox - A project to control sounds using buttons
Les Pounder
http:/bigl.es

For this project you will need

A Raspberry Pi
4 x Monentary Switches
A breadboard
Wires
Speaker or Monitor with audio.

"""

from gpiozero import Button
import pygame.mixer
from pygame.mixer import Sound
from signal import pause

pygame.mixer.init()

sound_pins = {
    2: Sound("samples/drum_tom_mid_hard.wav"),
    3: Sound("samples/drum_cymbal_open.wav"),
    4: Sound("samples/"),
    17: Sound("samples/")
}

buttons = [Button(pin) for pin in sound_pins]
for button in buttons:
    sound = sound_pins[button.pin.number]
    button.when_pressed = sound.play

pause()
