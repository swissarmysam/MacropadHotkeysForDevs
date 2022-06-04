# Author: 2022 swissarmysam

# MACROPAD Hotkeys: Visual Studo Code for Windows

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                      # REQUIRED dict, must be named 'app'
    'name' : 'VS Code', # Application name
    'macros' : [             # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x22d3ee, 'Cmd P.', [Keycode.CONTROL, Keycode.SHIFT, Keycode.P]), # Command Palette
        (0x22d3ee, 'S.Cuts', [Keycode.CONTROL, Keycode.ALT, Keycode.K]), # Keyboard Shortcuts
        (0x22d3ee, 'Reveal', [Keycode.SHIFT, Keycode.ALT, Keycode.R]), # Reveal in Finder
        # 2nd row ----------
        (0xfdba74, 'GT File', [Keycode.CONTROL, Keycode.P]), # Go to File
        (0xfdba74, 'GT Line', [Keycode.CONTROL, Keycode.G]), # Go to Line
        (0xfdba74, 'GT ([{}])', [Keycode.SHIFT, Keycode.CONTROL, Keycode.BACKSLASH]),  # Go to Matchig Bracket
        # 3rd row ----------
        (0x000040, 'S.Recur', [Keycode.CONTROL, Keycode.SHIFT, Keycode.L]), # Select Recurring value
        (0x000040, 'Curs.End', [Keycode.SHIFT, Keycode.ALT, Keycode.I]), # Add Cursor to line end
        (0x000040, 'Dup.Line', [Keycode.SHIFT, Keycode.ALT, Keycode.DOWN_ARROW]), # Duplicate Line
        # 4th row ----------
        (0x34d399, 'CP Next', [Keycode.ALT, Keycode.RIGHT_BRACKET]), # CoPilot Next
        (0x34d399, 'CP Prev', [Keycode.ALT, Keycode.LEFT_BRACKET]), # CoPilot Prev
        (0x34d399, 'CP Open', [Keycode.CONTROL, Keycode.ENTER]), # CoPilot Open
        # Encoder button ---
        (0x000000, '', [''])
    ]
}
