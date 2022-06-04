# SPDX-FileCopyrightText: 2022 swissarmysam

# MACROPAD Hotkeys: Function Keys Pad

from adafruit_hid.keycode import Keycode

app = {               
    'name' : 'Function Keys', 
    'macros' : [       
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x34d399, 'F1', [Keycode.F1]),
        (0x34d399, 'F2', [Keycode.F2]),
        (0x34d399, 'F3', [Keycode.F3]),
        # 2nd row ----------
        (0x34d399, 'F4', [Keycode.F4]),
        (0x34d399, 'F5', [Keycode.F5]),
        (0x34d399, 'F6', [Keycode.F6]),
        # 3rd row ----------
        (0x34d399, 'F7', [Keycode.F7]),
        (0x34d399, 'F8', [Keycode.F8]),
        (0x34d399, 'F9', [Keycode.F9]),
        # 4th row ----------
        (0x34d399, 'F10', [Keycode.F10]),
        (0x34d399, 'F11', [Keycode.F11]),
        (0x34d399, 'F12', [Keycode.F12]),
        # Encoder button ---
        (0x000000, '', [''])
    ]
}
