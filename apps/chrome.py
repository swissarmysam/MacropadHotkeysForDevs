# MACROPAD Hotkeys example: Firefox web browser for Linux

from utils.apps.key import KeyApp, MacroKey
from utils.commands import (
    Keycode,
    MacroCommand,
    Press,
    PreviousAppCommand,
    Sequence,
)
from utils.constants import (
    COLOR_BACK,
    COLOR_CHROME,
    COLOR_CLOSE,
)


class ChromeApp(KeyApp):
    name = "Chrome, Edge"

    # First row
    key_0 = MacroKey(
        "<-Back",
        COLOR_BACK,
        Press(Keycode.ALT, Keycode.LEFT_ARROW),
    )
    key_1 = MacroKey(
        "Fwd->",
        COLOR_CHROME,
        Press(Keycode.ALT, Keycode.RIGHT_ARROW),
    )
    key_2 = MacroKey(
        "New Tab",
        COLOR_CHROME,
        Press(Keycode.CONTROL, Keycode.T),
        double_tap_command=PreviousAppCommand(),
    )

    # Second row
    key_3 = MacroKey(
        "Snap",
        COLOR_CHROME,
        Press(Keycode.CONTROL, Keycode.L),
    )
    key_4 = MacroKey(
        "Ref|HR",
        COLOR_CHROME,
        Press(Keycode.F5),
        double_tap_command=Press(Keycode.CONTROL, Keycode.F5)
    )
    key_5 = MacroKey(
        "Close",
        COLOR_CLOSE,
        Press(Keycode.CONTROL, Keycode.W),
    )

    # Third row
    key_6 = MacroKey(
        "Console|CLS",
        COLOR_CHROME,
        Press(Keycode.CONTROL, Keycode.SHIFT, Keycode.K),
        double_tap_command=Press(Keycode.CONTROL, Keycode.L), # Clear
    )
    
    key_8 = MacroKey(
        "Inspector",
        COLOR_CHROME,
        Press(Keycode.CONTROL, Keycode.SHIFT, Keycode.C),
    )

    # Fourth row
    key_9 = MacroKey(
        "Last Panel",
        COLOR_CHROME,
        Press(Keycode.CONTROL, Keycode.SHIFT, Keycode.I),
    )
    key_11 = MacroKey(
        "Cmd Menu",
        COLOR_CHROME,
        Press(Keycode.CONTROL, Keycode.SHIFT, Keycode.P),
    )

    encoder_button = MacroCommand(
       Sequence(
            Press(Keycode.ALT, Keycode.F4),
            PreviousAppCommand(),
        )
    )
  
    encoder_decrease = MacroCommand(
        Press(Keycode.CONTROL, Keycode.PAGE_UP)
    )
    encoder_increase = MacroCommand(
        Press(Keycode.CONTROL, Keycode.PAGE_DOWN)
    )
