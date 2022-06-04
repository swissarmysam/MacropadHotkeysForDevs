# Author: 2022 swissarmysam

# MACROPAD Hotkeys: Chromium-based web browsers for Windows

from adafruit_hid.keycode import Keycode 


app = {                     
    'name' : 'Chromium (Chrome, Edge)', # Application name
    'macros' : [             # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x004000, '< Back', [Keycode.ALT, Keycode.LEFT_ARROW]),
        (0x004000, 'Fwd >', [Keycode.ALT, Keycode.RIGHT_ARROW]),
        (0x400000, 'New Tab', [Keycode.CONTROL, Keycode.T]),   
        # 2nd row ----------
        (0x202000, 'Refresh', [Keycode.F5]),
        (0x202000, 'Hard Ref', [Keycode.CONTROL, Keycode.F5]), # Hard refresh
        (0x34d399, 'Search Snap', Keycode.CONTROL, Keycode.L), # Snap to search bar                
        # 3rd row ----------
        (0x000040, 'Console', [Keycode.CONTROL, Keycode.SHIFT, Keycode.K]),
        (0x000040, 'Search Source', [Keycode.CONTROL, Keycode.P]), 
        (0x000040, 'Clear Cons', [Keycode.CONTROL, Keycode.L]), # Clear console
        # 4th row ----------
        (0x000040, 'Inspector', [Keycode.CONTROL, Keycode.SHIFT, Keycode.C]), 
        (0x000040, 'Last Panel', [Keycode.CONTROL, Keycode.SHIFT, Keycode.I]),
        (0x101010, 'Cmd Menu', [Keycode.CONTROL, Keycode.SHIFT, Keycode.P]), # Command menu
        # Encoder button ---
        (0x000000, '', ['']) 
    ]
}