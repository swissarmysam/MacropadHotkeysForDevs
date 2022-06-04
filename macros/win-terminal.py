# Author: 2022 swissarmysam

# MACROPAD Hotkeys: Terminal commands

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                      # REQUIRED dict, must be named 'app'
    'name' : 'Terminal Commands', # Application name
    'macros' : [             # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x004000, 'Az List Accs', ['az account list --output table']),
        (0x004000, 'Az Set Sub', ['az account set --subscription "Subscription Name"']),
        (0x004000, 'Az SP RBAC', ['az ad sp create-for-rbac --n "{sp-name}" --sdk-auth --role contributor --scopes /subscriptions/{subscription-id}/resourceGroups/{resource-group} ']),     
        # 2nd row ----------
        (0x202000, 'PS File', ['New-Item -Path . -Name ".file-name" -ItemType "file" -Value "file-content"  ']),
        (0x202000, 'PS Dir', ['New-Item -ItemType "directory" -Path ".\path\dir" ']),
        (0x202000, 'PS Open', ['Invoke-Item -Path ".\path\file.ext" ']),                    
        # 3rd row ----------
        (0x000040, 'Up 1 Dir', ['cd ..', Keycode.ENTER]),
        (0x000040, 'Up 2 Dir', ['cd ..\..', Keycode.ENTER]),
        (0x000040, 'Clear', ['cls']),
        # 4th row ----------
        (0x101010, 'npm install', ['npm install']),   
        (0x101010, 'npm start', ['npm run start']),   
        (0x101010, 'npm build', ['npm run build']), 
        # Encoder button ---
        (0x000000, '', [''])
    ]
}
