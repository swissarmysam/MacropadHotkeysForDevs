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
    COLOR_CODE,
    COLOR_WARNING,
)


class TeamsApp(KeyApp):
    name = "MS Teams"

    # First row
    key_0 = MacroKey(
        "Mute",
        COLOR_CODE,
        Press(Keycode.CONTROL, Keycode.SHIFT, Keycode.M),
    )
    key_2 = MacroKey(
        "Temp Unmute",
        COLOR_CODE,
        Press(Keycode.CONTROL, Keycode.SPACEBAR),
        double_tap_command=PreviousAppCommand(),
    )

    # Second row
    key_3 = MacroKey(
        "Share Screen",
        COLOR_CODE,
        Press(Keycode.CONTROL, Keycode.SHIFT, Keycode.E),
    )
    key_5 = MacroKey(
        "Admit",
        COLOR_CODE,
        Press(Keycode.CONTROL, Keycode.SHIFT, Keycode.O),
    )

    # Third row
    key_6 = MacroKey(
        "Sch. Meet",
        COLOR_CODE,
        Press(Keycode.CONTROL, Keycode.ALT, Keycode.SHIFT, Keycode.N)
    )
    key_8 = MacroKey(
        "Search",
        COLOR_CODE,
        Press(Keycode.CONTROL, Keycode.F),
    )

    # Fourth row
    key_9 = MacroKey(
        "Answer",
        COLOR_CODE,
        Press(Keycode.CONTROL, Keycode.SHIFT, Keycode.S),
    )
    key_11 = MacroKey(
        "End",
        COLOR_WARNING,
        Press(Keycode.CONTROL, Keycode.SHIFT, Keycode.H),
    )

    encoder_button = MacroCommand(
       Sequence(
            Press(Keycode.ALT, Keycode.F4),
            PreviousAppCommand(),
        )
    )
