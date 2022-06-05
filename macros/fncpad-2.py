# SPDX-FileCopyrightText: 2022 swissarmysam

# MACROPAD Hotkeys: Function Keys Pad

from adafruit_hid.keycode import Keycode

app = {               
    'name' : 'Function Keys #2', 
    'macros' : [       
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x34d399, 'F12', [Keycode.F12]),
        (0x34d399, 'F13', [Keycode.F13]),
        (0x34d399, 'F14', [Keycode.F14]),
        # 2nd row ----------
        (0x34d399, 'F15', [Keycode.F15]),
        (0x34d399, 'F16', [Keycode.F16]),
        (0x34d399, 'F17', [Keycode.F17]),
        # 3rd row ----------
        (0x000000, '', [''])
        (0x34d399, 'F18', [Keycode.F18]),
        (0x000000, '', [''])
        # 4th row ----------
        (0x000000, '', ['']),
        (0x000000, '', ['']),
        (0x000000, '', [''])
        # Encoder button ---
        (0x000000, '', [''])
    ]
}
