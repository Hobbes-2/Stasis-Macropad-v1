import board

# Imports from the kmk library
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros
from kmk.modules.encoder import EncoderHandler

# Main instance of the keyboard
keyboard = KMKKeyboard()

encoder_handler = EncoderHandler()

# Add the macro extension
macros = Macros()
keyboard.modules.append(macros)
keyboard.modules.append(encoder_handler)

# Pins for keys
PINS = [board.D4, board.D1, board.D5, board.D2, board.D6, board.D3]

#encoder pins - regular direction encoder and a button
encoder_handler.pins = (board.GP17, board.GP15, board.GP14)



# Tell kmk we are not using a key matrix
keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

zoom_in = KC.LCTL(KC.EQUAL)
zoom_out = KC.LCTL(KC.MINUS)

# Look here for keycodes: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/keycodes.md
# And here for macros: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/macros.md
keyboard.keymap = [
    [KC.LCTL(KC.X), KC.LCTL(KC.C), KC.LCTL(KC.V), KC.MACRO("Test"), KC.LCTL(KC.TAB), KC.LCTL(KC.LSFT(KC.TAB))],
    [KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO]
]

encoder_handler.map = [
    ((KC.VOLD, KC.VOLU, KC.MUTE),),
    ((zoom_in, zoom_out, KC.NO),)
]


# Start kmk!
if __name__ == '__main__':
    keyboard.go()
