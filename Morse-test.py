import machine
import utime

led_pin = machine.Pin(25, machine.Pin.OUT)

MORSE = {
    'A': '.-',   'B': '-...', 'C': '-.-.', 'D': '-..',  'E': '.',
    'F': '..-.', 'G': '--.',  'H': '....', 'I': '..',   'J': '.---',
    'K': '-.-',  'L': '.-..', 'M': '--',   'N': '-.',   'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.',  'S': '...',  'T': '-',
    'U': '..-',  'V': '...-', 'W': '.--',  'X': '-..-', 'Y': '-.--',
    'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--',
    '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...', ':': '---...',
    ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-',
    '"': '.-..-.', '$': '...-..-', '@': '.--.-.',
}

UNIT = 0.1  # seconds — adjust to taste

def dot():
    led_pin.value(1)
    utime.sleep(UNIT)
    led_pin.value(0)
    utime.sleep(UNIT)

def dash():
    led_pin.value(1)
    utime.sleep(3 * UNIT)
    led_pin.value(0)
    utime.sleep(UNIT)

def send_char(ch):
    code = MORSE.get(ch.upper())
    if code is None:
        return
    for symbol in code:
        if symbol == '.':
            dot()
        elif symbol == '-':
            dash()
    utime.sleep(2 * UNIT)  # letter gap (already have 1 unit from last symbol)

def send_text(text):
    for ch in text:
        if ch == ' ' or ch == '\n':
            utime.sleep(6 * UNIT)  # word gap (7 units total, 1 already elapsed)
        else:
            send_char(ch)

MESSAGE = """
She speaks.
O speak again bright angel for thou art
As glorious to this night being oer my head
As is a winged messenger of heaven
Unto the white upturned wondring eyes
Of mortals that fall back to gaze on him
When he bestrides the lazy puffing clouds
And sails upon the bosom of the air.

O Romeo Romeo Wherefore art thou Romeo
Deny thy father and refuse thy name
Or if thou wilt not be but sworn my love
And Ill no longer be a Capulet.

Shall I hear more or shall I speak at this.

Tis but thy name that is my enemy
Thou art thyself though not a Montague.
Whats Montague It is nor hand nor foot
Nor arm nor face nor any other part
Belonging to a man. O be some other name
Whats in a name That which we call a rose
By any other word would smell as sweet.
So Romeo would were he not Romeo called
Retain that dear perfection which he owes
Without that title. Romeo doff thy name
And for that name which is no part of thee
Take all myself.

I take thee at thy word.
Call me but love and Ill be new baptized
Henceforth I never will be Romeo.

What man art thou that thus bescreened in night
So stumblest on my counsel.

By a name
I know not how to tell thee who I am.
My name dear saint is hateful to myself
Because it is an enemy to thee.
Had I it written I would tear the word.

My ears have not yet drunk a hundred words
Of that tongues uttering yet I know the sound.
Art thou not Romeo and a Montague.
"""

send_text(MESSAGE)
