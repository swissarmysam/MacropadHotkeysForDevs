# Author: 2022 swissarmysam

# MACROPAD Hotkeys: Chromium-based web browsers for Windows

from adafruit_hid.keycode import Keycode 


app = {                     
    'name' : 'Chromium', # Application name
    'macros' : [             # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x004000, '< Back', [Keycode.ALT, Keycode.LEFT_ARROW]),
        (0x004000, 'Fwd >', [Keycode.ALT, Keycode.RIGHT_ARROW]),
        (0x400000, 'New Tab', [Keycode.CONTROL, Keycode.T]),   
        # 2nd row ----------
        (0x202000, 'Ref.', [Keycode.F5]), # Refresh
        (0x202000, 'Hd. Ref', [Keycode.CONTROL, Keycode.F5]), # Hard refresh
        (0x34d399, 'Snap', Keycode.CONTROL, Keycode.L), # Snap to search bar                
        # 3rd row ----------
        (0x000040, 'Cons.', [Keycode.CONTROL, Keycode.SHIFT, Keycode.K]), # Console
        (0x000040, 'Source', [Keycode.CONTROL, Keycode.P]), # Search source
        (0x000040, 'CLS.', [Keycode.CONTROL, Keycode.L]), # Clear console
        # 4th row ----------
        (0x000040, 'Inps.', [Keycode.CONTROL, Keycode.SHIFT, Keycode.C]), # Inspector
        (0x000040, 'Last P', [Keycode.CONTROL, Keycode.SHIFT, Keycode.I]), # Last Panel
        (0x101010, 'Cmd Menu', [Keycode.CONTROL, Keycode.SHIFT, Keycode.P]), # Command menu
        # Encoder button ---
        (0x000000, '', ['']) 
    ]
}