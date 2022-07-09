"""App with macros for managing windows and virtual desktops."""

from utils.apps.key import KeyApp, MacroKey
from utils.commands import Keycode, Press, PreviousAppCommand, MacroCommand
from utils.constants import COLOR_2, COLOR_3, COLOR_WINMAN


class WindowManagementApp(KeyApp):
    name = "Windows General"

    key_0 = MacroKey(
        "<-App",
        COLOR_3,
        Press(Keycode.ALT, Keycode.TAB, Keycode.SHIFT),
    )
    key_1 = MacroKey(
        "View",
        COLOR_2,
        Press(Keycode.WINDOWS, Keycode.TAB),
    )
    key_2 = MacroKey(
        "App->",
        COLOR_3,
        Press(Keycode.ALT, Keycode.TAB),
        double_tap_command=PreviousAppCommand(),
    )

    key_3 = MacroKey(
        "Max",
        COLOR_WINMAN,
        Press(Keycode.WINDOWS, Keycode.UP_ARROW),
    )

    key_5 = MacroKey(
        "Min",
        COLOR_WINMAN,
        Press(Keycode.WINDOWS, Keycode.DOWN_ARROW),
    )

    key_6 = MacroKey(
        "Snip Tool",
        COLOR_WINMAN,
        Press(Keycode.WINDOWS, Keycode.SHIFT, Keycode.S),
    )
    key_8 = MacroKey(
        "Color Picker",
        COLOR_WINMAN,
        Press(Keycode.SHIFT, Keycode.WINDOWS, Keycode.C),
    )
    key_9 = MacroKey(
        "Hdn Menu",
        COLOR_WINMAN,
        Press(Keycode.WINDOWS, Keycode.X),
    )

    key_11 = MacroKey(
        "App AOT",
        COLOR_WINMAN,
        Press(Keycode.WINDOWS, Keycode.CONTROL, Keycode.T),
    )

    encoder_button = PreviousAppCommand()

    encoder_decrease = MacroCommand(
        Press(Keycode.CONTROL, Keycode.PAGE_UP)
    )
    encoder_increase = MacroCommand(
        Press(Keycode.CONTROL, Keycode.PAGE_DOWN)
    )
