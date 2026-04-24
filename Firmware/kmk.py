import board
import busio

# Imports from the kmk library
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros
from kmk.modules.encoder import EncoderHandler

#For display
from kmk.extensions.display import Display, TextEntry, ImageEntry
from kmk.extensions.display.ssd1306 import SSD1306

#Main instance of the keyboard
keyboard = KMKKeyboard()

encoder_handler = EncoderHandler()

#Add the macro extension
macros = Macros()
keyboard.modules.append(macros)
keyboard.modules.append(encoder_handler)

#Pins for keys
PINS = [board.D4, board.D1, board.D5, board.D2, board.D6, board.D3]

#Encoder pins - regular direction encoder and a button
encoder_handler.pins = (board.GP17, board.GP15, board.GP14)


#Tell kmk we are not using a key matrix
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

#Display time
i2c_bus = busio.I2C(board.GP_SCL, board.GP_SDA)

driver = SSD1306(
    i2c = i2c_bus,
    device_address = 0x3C,
)

mainDisplay = Display(
    display = driver,
    width = 128,
    height = 32,
    powersave_off_time = 30
)

mainDisplay.entries = [
    ImageEntry(image = "FillerImage.jpg", x=0, y=0),
]

keyboard.extensions.append(mainDisplay)

#Start kmk
if __name__ == '__main__':
    keyboard.go()


# Im gonna work on this later, for now i just want a working script with the basic setup

# logged_keys = []
# max_keys = 20

# def logKeys(key_input, is_pressed):
#     print("Working...")
#     key_name = str(key_input)
#     logged_keys.append(key_name)
#     if len(logged_keys) > max_keys:
#         logged_keys.pop(0)
#     return key_input
