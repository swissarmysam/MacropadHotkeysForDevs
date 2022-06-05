# Author: 2022 swissarmysam

# MACROPAD Hotkeys: Terminal commands

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                      # REQUIRED dict, must be named 'app'
    'name' : 'Terminal Commands', # Application name
    'macros' : [             # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x004000, 'Az List', ['az account list --output table']), # Az account list
        (0x004000, 'Az Set', ['az account set --subscription @Subscription Name@']), # Az account set subscription
        (0x004000, 'Az SP', ['az ad sp create-for-rbac --n @{sp-name}@ --sdk-auth --role contributor --scopes /subscriptions/{subscription-id}/resourceGroups/{resource-group} ']),  # rbac sp create 
        # 2nd row ----------
        (0x202000, 'PS File', ['New-Item -Path . -Name @.file-name@ -ItemType @file@ -Value @file-content@  ']),
        (0x202000, 'PS Dir', ['New-Item -ItemType @directory@ -Path @.', Keycode.CONTROL, Keycode.ALT, Keycode.POUND, 'path', Keycode.CONTROL, Keycode.ALT, Keycode.POUND, 'dir@']),
        (0x202000, 'PS Open', ['Invoke-Item -Path @.',  Keycode.CONTROL, Keycode.ALT, Keycode.POUND, 'path',  Keycode.CONTROL, Keycode.ALT, Keycode.POUND, 'file.ext@']),                    
        # 3rd row ----------
        (0x000040, 'Up 1', ['cd ..', 0.25, Keycode.ENTER]),
        (0x000040, 'Up 2', ['cd ..', Keycode.CONTROL, Keycode.ALT, Keycode.POUND, '..', 0.25, Keycode.ENTER]),
        (0x000040, 'CLS', ['cls']),
        # 4th row ----------
        (0x101010, 'npm I', ['npm install']),   # npm install
        (0x101010, 'npm St', ['npm run start']),   # start
        (0x101010, 'npm Bu', ['npm run build']), # build
        # Encoder button ---
        (0x000000, '', [''])
    ]
}