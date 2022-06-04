# Author: 2022 swissarmysam

# MACROPAD Hotkeys: Microsoft Teams for Desktop

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                    # REQUIRED dict, must be named 'app'
    'name' : 'Microsoft Teams', # Application name
    'macros' : [           # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x800080, 'Mute', [Keycode.CONTROL, Keycode.SHIFT, Keycode.M]),
        (0x000000, '', ['']),
        (0x800080, 'Temp Unmute', [Keycode.CONTROL, Keycode.SPACEBAR]), # Hold to unmute
        # 2nd row ----------
        (0x800080, 'Share Screen', [Keycode.CONTROL, Keycode.SHIFT, Keycode.E]),
        (0x000000, '', ['']),
        (0x800080, 'Admit', [Keycode.CONTROL, Keycode.SHIFT, Keycode.O]), # Admit from lobby
        # 3rd row ----------
        (0x800000, 'Sch. Meet', [Keycode.ALT, Keycode.SHIFT, Keycode.N]), # Schedule meeting
        (0x000000, '', ['']),
        (0x800080, 'Search', [Keycode.CONTROL, Keycode.F]),
        # 4th row ----------
        (0x34d399, 'Answer', [Keycode.CONTROL, Keycode.SHIFT, Keycode.S]),
        (0x000000, '', ['']),
        (0xfdba74, 'End', [Keycode.CONTROL, Keycode.SHIFT, Keycode.H]),
        # Encoder button ---s
        (0x000000, '', [''])
    ]
}