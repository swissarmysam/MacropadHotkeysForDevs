# Author: 2022 swissarmysam

# MACROPAD Hotkeys: Visual Studio 2022 for Windows

from adafruit_hid.keycode import Keycode 

app = {                      
    'name' : 'Visual Studio', 
    'macros' : [             
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x22d3ee, 'Search', [Keycode.CONTROL, Keycode.Q]), # Visual Studio Search
        (0x22d3ee, 'GT File', [Keycode.CONTROL, Keycode.F]),  # Go to File
        (0xfdba74, 'Pk Def.', [Keycode.ALT, Keycode.F12]), # Peek definition
        # 2nd row ----------
        (0x22d3ee, 'Qk. Acts', [Keycode.ALT, Keycode.ENTER]),
        (0x22d3ee, 'Sol. Exp', [Keycode.CONTROL, Keycode.ALT, Keycode.L]),  # Open Solution Explorer
        (0x000040, 'Comm.', [Keycode.CONTROL, Keycode.ALT, Keycode.U, Keycode.C]), # Toggle comments - create in shortcuts editor
        # 3rd row ----------
        (0xfb7185, 'Add BP', [Keycode.F9]), # Toggle breakpoint
        (0xfb7185, 'Step', [Keycode.F11]), # step into
        (0xfb7185, 'Del BPs', [Keycode.CONTROL, Keycode.SHIFT, Keycode.F9]), # Delete all breakpoints
        # 4th row ----------
        (0x34d399, 'Clean', [Keycode.CONTROL, Keycode.ALT, Keycode.B, Keycode.C]), # Clean solution - create in shortcuts editor
        (0x34d399, 'Build', [Keycode.CONTROL, Keycode.SHIFT, Keycode.B]), # Build solution
        (0x34d399, 'Run', [Keycode.CONTROL, Keycode.F5]), # Run solution
        # Encoder button ---
        (0x000000, '', [''])
    ]
}