# Author: 2022 swissarmysam

# MACROPAD Hotkeys: General Windows

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                # REQUIRED dict, must be named 'app'
    'name' : 'Windows General', # Application name
    'macros' : [       # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x34d399, 'Cut', [Keycode.CONTROL, Keycode.X]),
        (0x34d399, 'Copy', [Keycode.CONTROL, Keycode.C]),
        (0x34d399, 'Paste', [Keycode.CONTROL, Keycode.V]),
        # 2nd row ----------
        (0x34d399, 'Sel All', [Keycode.CONTROL, Keycode.A]), # Select All
        (0x22d3ee, 'Snip', [Keycode.WINDOW, Keycode.SHIFT, Keycode.S]), # Snip & Sketch
        (0x22d3ee, 'Col Pkr', [Keycode.WINDOWS, Keycode.SHIFT, Keycode.C]), # Color Picker (PowerToys)
        # 3rd row ----------
        (0xfdba74, 'Rename', [Keycode.F2]),
        (0xfdba74, 'Ref.', [Keycode.F5]), # Refresh
        (0xfb7185, 'Hdn Mnu', [Keycode.WINDOWS, Keycode.X]), # Hidden Menu
        # 4th row ----------
        (0xfb7185, 'Task View', [Keycode.WINDOWS, Keycode.TAB]), 
        (0xfb7185, 'Sw <', [Keycode.ALT, Keycode.SHIFT, Keycode.TAB]), # Switch app to Left
        (0xfb7185, 'Sw >', [Keycode.ALT, Keycode.TAB]), # Switch app to Right
        # Encoder button ---
        (0x000000, '', [''])
    ]
}