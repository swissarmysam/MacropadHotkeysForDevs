"""App with macros for managing windows and virtual desktops."""

from utils.apps.key import KeyApp, MacroKey
from utils.commands import Keycode, Press, PreviousAppCommand, MacroCommand
from utils.constants import COLOR_2, COLOR_3, COLOR_WINMAN


class ShareXApp(KeyApp):
    name = "ShareX"

    key_0 = MacroKey(
        "Active PNG",
        COLOR_3,
        Press(Keycode.SHIFT, Keycode.PRINT_SCREEN),
    )

    key_2 = MacroKey(
        "Region PNG",
        COLOR_3,
        Press(Keycode.CONTROL, Keycode.PRINT_SCREEN),
        double_tap_command=PreviousAppCommand(),
    )
    
    key_3 = MacroKey(
        "Active GIF",
        COLOR_WINMAN,
        Press(Keycode.CONTROL, Keycode.SHIFT, Keycode.PRINT_SCREEN),
    )

    key_5 = MacroKey(
        "Region GIF",
        COLOR_WINMAN,
        Press(Keycode.CONTROL, Keycode.SHIFT, Keycode.ALT, Keycode.PRINT_SCREEN),
    )

    key_9 = MacroKey(
        "Scroll PNG",
        COLOR_WINMAN,
        Press(Keycode.SHIFT, Keycode.WINDOWS, Keycode.C),
    )

    key_11 = MacroKey(
        "Record",
        COLOR_WINMAN,
        Press(Keycode.CONTROL, Keycode.ALT, Keycode.PRINT_SCREEN),
    )

    encoder_button = PreviousAppCommand()

    encoder_decrease = MacroCommand(
        Press(Keycode.CONTROL, Keycode.PAGE_UP)
    )
    encoder_increase = MacroCommand(
        Press(Keycode.CONTROL, Keycode.PAGE_DOWN)
    )
