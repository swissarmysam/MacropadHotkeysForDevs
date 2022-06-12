# MACROPAD Hotkeys example: Firefox web browser for Linux

from utils.commands import Wait
from utils.apps.key import KeyApp, MacroKey
from utils.commands import (
    Keycode,
    MacroCommand,
    Press,
    PreviousAppCommand,
    Sequence,
)
from utils.constants import (
    COLOR_CODE
)


class VsApp(KeyApp):
    name = "Visual Studio"

    # First row
    key_0 = MacroKey(
        "VS Search",
        COLOR_CODE,
        Press(Keycode.CONTROL, Keycode.Q),
    )
    key_2 = MacroKey(
        "Search",
        COLOR_CODE,
        Press(Keycode.CONTROL, Keycode.F),
        double_tap_command=PreviousAppCommand(),
    )

    # Second row
    key_3 = MacroKey(
        "Comments",
        COLOR_CODE,
        Sequence(
            Press(Keycode.CONTROL, Keycode.K),
            Wait(0.1),
            Press(Keycode.CONTROL, Keycode.C),
        ),
        double_tap_command=Sequence(
            Press(Keycode.CONTROL, Keycode.K),
            Wait(0.1),
            Press(Keycode.CONTROL, Keycode.U),
        )
    )

    key_5 = MacroKey(
        "Peek",
        COLOR_CODE,
        Press(Keycode.ALT, Keycode.F12),
    )

    # Third row
    key_6 = MacroKey(
        "Togg BP",
        COLOR_CODE,
        Press(Keycode.F9)
    )
    key_7= MacroKey(
        "Step",#
        COLOR_CODE,
        Press(Keycode.F11)
    )
    key_8 = MacroKey(
        "Del BPs",
        COLOR_CODE,
        Press(Keycode.CONTROL, Keycode.SHIFT, Keycode.F9),
    )

    # Fourth row
    key_9 = MacroKey(
        "Clean",
        COLOR_CODE,
        Press(Keycode.CONTROL, Keycode.ALT, Keycode.C, Keycode.S),
    )
    key_10= MacroKey(
        "Build",
        COLOR_CODE,
        Press(Keycode.CONTROL, Keycode.SHIFT, Keycode.B),
    )
    key_11 = MacroKey(
        "Run",
        COLOR_CODE,
        Press(Keycode.CONTROL, Keycode.F5),
    )

    encoder_button = MacroCommand(
       Sequence(
            Press(Keycode.ALT, Keycode.F4),
            PreviousAppCommand(),
        )
    )
