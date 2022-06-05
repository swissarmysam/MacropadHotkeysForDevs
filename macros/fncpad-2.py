# SPDX-FileCopyrightText: 2022 swissarmysam

# MACROPAD Hotkeys: Extra Function Keys Pad

from adafruit_hid.keycode import Keycode

app = {               
    'name' : 'Function Keys #2', 
    'macros' : [       
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x34d399, 'F13', [Keycode.F13]),
        (0x34d399, 'F14', [Keycode.F14]),
        (0x34d399, 'F15', [Keycode.F15]),
        # 2nd row ----------
        (0x34d399, 'F16', [Keycode.F16]),
        (0x34d399, 'F17', [Keycode.F17]),
        (0x34d399, 'F18', [Keycode.F18]),
        # 3rd row ----------
        (0x000000, 'F19', [Keycode.F19]),
        (0x000000, 'F20', [Keycode.F20]),
        (0x000000, 'F21', [Keycode.F21]),
        # 4th row ----------
        (0x34d399, 'F22', [Keycode.F22]),
        (0x000000, 'F23', [Keycode.F23]),
        (0x000000, 'F24', [Keycode.F24]),
        # Encoder button ---
        (0x000000, '', [''])
    ]
}
