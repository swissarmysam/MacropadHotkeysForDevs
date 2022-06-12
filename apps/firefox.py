# MACROPAD Hotkeys example: Firefox web browser

from utils.apps.key import KeyApp, MacroKey
from utils.commands import (
    Keycode,
    MacroCommand,
    Press,
    PreviousAppCommand,
    Sequence,
)
from utils.constants import (
    COLOR_3,
    COLOR_7,
    COLOR_9,
    COLOR_BACK,
    COLOR_FIREFOX,
    COLOR_CLOSE,
)


class FirefoxApp(KeyApp):
    name = "Firefox"

    # First row
    key_0 = MacroKey(
        "<-Back",
        COLOR_BACK,
        Press(Keycode.ALT, Keycode.LEFT_ARROW),
    )
    key_1 = MacroKey(
        "Fwd->",
        COLOR_FIREFOX,
        Press(Keycode.ALT, Keycode.RIGHT_ARROW),
    )
    key_2 = MacroKey(
        "New Tab",
        COLOR_FIREFOX,
        Press(Keycode.CONTROL, Keycode.T),
        double_tap_command=PreviousAppCommand(),
    )

    # Second row
    key_3 = MacroKey(
        "Snap",
        COLOR_FIREFOX,
        Press(Keycode.CONTROL, Keycode.L),
    )
    key_4 = MacroKey(
        "Ref|HR",
        COLOR_3,
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
        "Cons.",
        COLOR_7,
        Press(Keycode.CONTROL, Keycode.SHIFT, Keycode.J)
    )
    key_7 = MacroKey(
        "Debug",
        COLOR_FIREFOX,
        Press(Keycode.CONTROL, Keycode.SHIFT, Keycode.F),
    )
    key_8 = MacroKey(
        "Netw.",
        COLOR_9,
        Press(Keycode.CONTROL, Keycode.SHIFT, Keycode.E),
    )

    # Fourth row
    key_9 = MacroKey(
        "Insp.",
        COLOR_FIREFOX,
        Press(Keycode.CONTROL, Keycode.SHIFT, Keycode.C),
    )
    key_10 = MacroKey(
        "Last Panel",
        COLOR_FIREFOX,
        Press(Keycode.CONTROL, Keycode.SHIFT, Keycode.I),
    )
    key_11 = MacroKey(
        "Cmd Menu",
        COLOR_FIREFOX,
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
