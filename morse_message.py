import machine
import time
import sys
from machine import Pin

try:
    led = machine.Pin("LED", machine.Pin.OUT)
except ValueError:
    led = machine.Pin(25, machine.Pin.OUT)
    
DOT_DURATION = 0.200
DASH_DURATION = DOT_DURATION * 3
ELEMENT_GAP = DOT_DURATION
LETTER_GAP = DOT_DURATION * 3
WORD_GAP = DOT_DURATION * 7

MORSE_DICT = {
    'A': '.-',    'B': '-...',  'C': '-.-.',  'D': '-..',   'E': '.',
    'F': '..-.',  'G': '--.',   'H': '....',  'I': '..',    'J': '.---',
    'K': '-.-',   'L': '.-..',  'M': '--',    'N': '-.',    'O': '---',
    'P': '.--.',  'Q': '--.-',  'R': '.-.',   'S': '...',   'T': '-',
    'U': '..-',   'V': '...-',  'W': '.--',   'X': '-..-',  'Y': '-.--',
    'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----'
}

def flash_code (sequence):
    for symbol in sequence:
        led.value(1)
        if symbol = ".":
            time.sleep(DOT_DURATION)
        elif symbol = "-":
            time.sleep(DASH_DURATION)
        
        led.value(0)
        time.sleep(ELEMENT_GAP)
        
    time.sleep(LETTER_GAP - ELEMENT_GAP)

print("Type your text in the Shell below and press Enter:")

while True:
    user_input = input("\nEnter text: ").upper()
    
    for char in user_input:
        if char in MORSE-DICT:
            flash_code(MORSE-DICT[char])
        elif char == " ":
            time.sleep(WORD_GAP - LETTER_GAP)
    
    
