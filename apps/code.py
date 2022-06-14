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
    COLOR_CODE,
)


class CodeApp(KeyApp):
    name = "VS Code"

    key_0 = MacroKey(
        "Cmd Pal",
        COLOR_CODE,
        Press(Keycode.CONTROL, Keycode.SHIFT, Keycode.P),
    )

    key_2 = MacroKey(
        "Kbd Ref", # Keyboard Reference
        COLOR_CODE,
        Sequence(
          
                Press(Keycode.CONTROL, Keycode.SHIFT, Keycode.K),
                Wait(0.1),
                Press(Keycode.CONTROL, Keycode.S),    
        ),
        double_tap_command=PreviousAppCommand()
    )

    # Second row
    key_3 = MacroKey(
        "GT {}",
        COLOR_CODE,
        Press(Keycode.CONTROL, Keycode.SHIFT, Keycode.BACKSLASH),
    )
    key_4 = MacroKey(
        "GT Line",
        COLOR_CODE,
        Press(Keycode.CONTROL, Keycode.G),
    )
    key_5 = MacroKey(
        "GT File",
        COLOR_CODE,
        Press(Keycode.CONTROL, Keycode.P),
    )

    # Third row
    key_6 = MacroKey(
        "DUP.", # duplicate line down (one tap), line up (double tap)
        COLOR_CODE,
        Press(Keycode.SHIFT, Keycode.ALT, Keycode.DOWN_ARROW),
        double_tap_command=Press(Keycode.SHIFT, Keycode.ALT, Keycode.UP_ARROW),
    )
    key_7 = MacroKey(
        "SNF|SWF", # save without formatting, save with formatting (double tap)
        COLOR_CODE,
        Sequence(
            Press(Keycode.CONTROL, Keycode.K),
            Wait(0.1),
            Press(Keycode.CONTROL, Keycode.SHIFT, Keycode.S),
        ),
        double_tap_command=Press(Keycode.CONTROL, Keycode.S),
    )
    key_8 = MacroKey(
        "SR", # Select Recurring value
        COLOR_CODE,
        Press(Keycode.CONTROL, Keycode.SHIFT, Keycode.L),
    )

    # Fourth row
    key_9 = MacroKey(
        "<-CP",
        COLOR_CODE,
        Press(Keycode.ALT, Keycode.LEFT_BRACKET),
    )
    key_10= MacroKey(
        "CP Open",
        COLOR_CODE,
        Press(Keycode.CONTROL, Keycode.ENTER),
    )
    key_11 = MacroKey(
        "CP->",
        COLOR_CODE,
        Press(Keycode.ALT, Keycode.RIGHT_BRACKET),
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
