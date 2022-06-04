# Author: 2022 swissarmysam

# MACROPAD Hotkeys: Firefox web browser for Windows

from adafruit_hid.keycode import Keycode 

app = {                    
    'name' : 'Firefox', # Application name
    'macros' : [             # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x004000, '< Back', [Keycode.ALT, Keycode.LEFT_ARROW]),
        (0x004000, 'Fwd >', [Keycode.ALT, Keycode.RIGHT_ARROW]),
        (0x400000, 'New Tab', [Keycode.CONTROL, Keycode.T]),   
        # 2nd row ----------
        (0x202000, 'Ref.', [Keycode.F5]), # refresh
        (0x202000, 'Hd. Ref', [Keycode.CONTROL, Keycode.F5]), # Hard refresh
        (0x34d399, 'Snap', Keycode.CONTROL, Keycode.L), # Snap to search bar              
        # 3rd row ----------
        (0x000040, 'Netw.', [Keycode.CONTROL, Keycode.SHIFT, Keycode.E]), # network
        (0x000040, 'Cons.', [Keycode.CONTROL, Keycode.SHIFT, Keycode.J]), # console
        (0x000040, 'Debug', [Keycode.CONTROL, Keycode.SHIFT, Keycode.F]), # debug search
        # 4th row ----------
        (0x000040, 'Insp.', [Keycode.CONTROL, Keycode.SHIFT, Keycode.C]), # inspector
        (0x101010, 'Style.', [Keycode.SHIFT, Keycode.F7]), # Style editor
        (0x000040, 'Last P', [Keycode.CONTROL, Keycode.SHIFT, Keycode.I]), # Last Panel
        # Encoder button ---
        (0x000000, '', ['']) 
    ]
}
