# MACROPAD Hotkeys example: Function keys

from utils.apps.key import Key, KeyApp
from utils.commands import (
    ConsumerControlCode,
    Keycode,
    Media,
    Press,
    PreviousAppCommand,
)
from utils.constants import COLOR_FUNC


class FuncKeysApp(KeyApp):
    name = "Function Keys"

    # First row
    key_0 = Key("F1|13", COLOR_FUNC, Press(Keycode.F1), double_tap_command=Press(Keycode.F13))
    key_1 = Key("F2|14", COLOR_FUNC, Press(Keycode.F2), double_tap_command=Press(Keycode.F14))
    key_2 = Key(
        "F3", COLOR_FUNC, Press(Keycode.F3), double_tap_command=PreviousAppCommand()
    )

    # Second row
    key_3 = Key("F4|15", COLOR_FUNC, Press(Keycode.F4), double_tap_command=Press(Keycode.F15))
    key_4 = Key("F5|16", COLOR_FUNC, Press(Keycode.F5), double_tap_command=Press(Keycode.F16))
    key_5 = Key("F6|17", COLOR_FUNC, Press(Keycode.F6), double_tap_command=Press(Keycode.F17))

    # Third row
    key_6 = Key("F7|18", COLOR_FUNC, Press(Keycode.F7), double_tap_command=Press(Keycode.F18))
    key_7 = Key("F8|19", COLOR_FUNC, Press(Keycode.F8), double_tap_command=Press(Keycode.F19))
    key_8 = Key("F9|20", COLOR_FUNC, Press(Keycode.F9), double_tap_command=Press(Keycode.F20))

    # Fourth row
    key_9 = Key("F10|21", COLOR_FUNC, Press(Keycode.F10), double_tap_command=Press(Keycode.F21))
    key_10 = Key("F11|22", COLOR_FUNC, Press(Keycode.F11), double_tap_command=Press(Keycode.F22))
    key_11 = Key("F12|23", COLOR_FUNC, Press(Keycode.F12), double_tap_command=Press(Keycode.F23))

    encoder_button = PreviousAppCommand()

    encoder_increase = Media(ConsumerControlCode.VOLUME_INCREMENT)
    encoder_decrease = Media(ConsumerControlCode.VOLUME_DECREMENT)
