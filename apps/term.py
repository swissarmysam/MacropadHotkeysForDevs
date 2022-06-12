# MACROPAD Hotkeys example: Universal Numpad

from utils.commands import MacroCommand
from utils.apps.key import Key, KeyApp, MacroKey
from utils.commands import (
    Keycode,
    Press,
    PreviousAppCommand,
    Text,
    Sequence,
    Wait,
)
from utils.constants import COLOR_8, COLOR_CODE, COLOR_WARNING


class TermApp(KeyApp):
    name = "Terminal Commands"

    # First row
    key_0 = Key("Az List", COLOR_CODE, Text("az account list --output table"))
    key_1 = Key("Az Set", COLOR_CODE, Text("az account set --subscription 'Subscription Name'"))
    key_2 = Key("Az SP", COLOR_CODE, Text("az ad sp create-for-rbac --n '{sp-name}' --sdk-auth --role contributor --scopes /subscriptions/{subscription-id}/resourceGroups/{resource-group}"), double_tap_command=PreviousAppCommand())

    # Second row
    key_3 = Key("PS File", COLOR_CODE, Text("New-Item -Path . -Name '.file-name' -ItemType 'file' -Value 'file-content'"))
    key_4 = Key("PS Dir", COLOR_CODE, Text("New-Item -ItemType 'directory' -Path 'path-to-dir-inc-name'"))
    key_5 = Key("PS Open", COLOR_CODE, Text("Invoke-Item -Path 'path-to-file-or-dir'"))

    # Third row
    key_6 = MacroKey(
        "Up 1 Dir",
        COLOR_CODE,
        Sequence(
            Text("cd .."),
            Wait(0.25),
            Press(Keycode.ENTER),
        ),
    )

    key_8 = MacroKey(
        "CLS",
        COLOR_CODE,
        Sequence(
            Text("cls"),
            Wait(0.1),
            Press(Keycode.ENTER),
        )
    )

    # Fourth row
    key_9 = Key("npm I", COLOR_CODE, Text("npm install"), double_tap_command=Text("npm install --force"))
    key_10 = Key(
        "npm st",
        COLOR_CODE,
        Text("npm run start"),

    )
    key_11 = Key(
        "npm bu",
        COLOR_CODE,
        Text("npm run build"),

    )

    encoder_button = PreviousAppCommand()
