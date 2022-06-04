# Author: 2022 swissarmysam

# MACROPAD Hotkeys: Git commands

app = {                     
    'name' : 'Git Commands', 
    'macros' : [
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x22d3ee, 'Add', ['git add ']),
        (0x22d3ee, 'Commit', ['git commit -m ']),
        (0x22d3ee, 'Push', ['git push -u origin ']),     
        # 2nd row ----------
        (0xfdba74, 'Checkout', ['git checkout ']),
        (0xfdba74, 'New Branch', ['git checkout -b ']),
        (0xfdba74, 'Switch', ['git switch -c ']),                    
        # 3rd row ----------
        (0xfb7185, 'Fetch', ['git fetch -all']),
        (0xfb7185, 'Pull', ['git pull origin ']),
        (0xfb7185, 'Merge', ['git merge ']),
        # 4th row ----------
        (0x22d3ee, 'Status', ['git status']), 
        (0x34d399, 'Soft Reset', ['git reset --soft HEAD~']),   
        (0x34d399, 'Hard Reset', ['git reset --hard origin/']),   
        # Encoder button ---
        (0x000000, '', [''])
    ]
}
