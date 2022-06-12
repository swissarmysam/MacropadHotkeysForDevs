# MACROPAD Hotkeys example: Universal Numpad

from utils.commands import Wait
from utils.apps.key import Key, KeyApp,  MacroKey
from utils.commands import (
    PreviousAppCommand,
    Text,
    Sequence,
    Press,
    Keycode,
)
from utils.constants import COLOR_CODE 


class GitApp(KeyApp):
    name = "Git Commands"

    # First row
    key_0 = Key("Add", COLOR_CODE, Text("git add "), double_tap_command=Text("git add ."))
    key_1 = Key("Commit", COLOR_CODE, Text("git commit -m '"), double_tap_command=Text("git commit -am '"))
    key_2 = Key("Push", COLOR_CODE, Text("git push -u origin "), double_tap_command=PreviousAppCommand())

    # Second row
    key_3 = Key("ChkOut", COLOR_CODE, Text("git checkout "))
    key_4 = Key("New Br", COLOR_CODE, Text("git checkout -b "))
    key_5 = Key("Switch", COLOR_CODE, Text("git switch -c "))

    # Third row
    key_6 = Key("Fetch", COLOR_CODE, Text("git fetch -all"))
    key_7 = Key("Pull", COLOR_CODE, Text("git pull origin "))
    key_8 = Key("Merge", COLOR_CODE, Text("git merge "))

    # Fourth row
    key_9 = Key("Status", COLOR_CODE, Text("git status "))
    key_10 = MacroKey("Sft Rst", COLOR_CODE, Sequence(Text("git reset --soft HEAD"), Wait(0.1), Press(Keycode.SHIFT, Keycode.POUND)))
    key_11 = Key("Hd Rst", COLOR_CODE, Text("git reset --hard origin/"))

    encoder_button = PreviousAppCommand()
