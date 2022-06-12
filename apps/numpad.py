# MACROPAD Hotkeys example: Universal Numpad

from utils.apps.key import Key, KeyApp
from utils.commands import (
    ConsumerControlCode,
    Keycode,
    Media,
    Press,
    PreviousAppCommand,
    Text,
)
from utils.constants import COLOR_8, COLOR_CODE, COLOR_WARNING


class NumpadApp(KeyApp):
    name = "Numpad"

    # First row
    key_0 = Key("7", COLOR_CODE, Text("7"), double_tap_command=Text("/"))
    key_1 = Key("8", COLOR_CODE, Text("8"), double_tap_command=Text("*"))
    key_2 = Key("9", COLOR_CODE, Text("9"), double_tap_command=PreviousAppCommand())

    # Second row
    key_3 = Key("4", COLOR_CODE, Text("4"))
    key_4 = Key("5", COLOR_CODE, Text("5"))
    key_5 = Key("6", COLOR_CODE, Text("6"), double_tap_command=Text("-"))

    # Third row
    key_6 = Key("1", COLOR_CODE, Text("1"))
    key_7 = Key("2", COLOR_CODE, Text("2"))
    key_8 = Key("3", COLOR_CODE, Text("3"), double_tap_command=Text("+"))

    # Fourth row
    key_9 = Key(".", COLOR_8, Text("."))
    key_10 = Key("0", COLOR_CODE, Text("0"))
    key_11 = Key("Enter", COLOR_WARNING, Press(Keycode.KEYPAD_ENTER))

    encoder_button = Media(ConsumerControlCode.MUTE)

    encoder_increase = Media(ConsumerControlCode.VOLUME_INCREMENT)
    encoder_decrease = Media(ConsumerControlCode.VOLUME_DECREMENT)
