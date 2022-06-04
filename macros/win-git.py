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
        (0xfdba74, 'Chk. Out', ['git checkout ']), # Checkout
        (0xfdba74, 'New Br.', ['git checkout -b ']), # New branch
        (0xfdba74, 'Switch', ['git switch -c ']),                    
        # 3rd row ----------
        (0xfb7185, 'Fetch', ['git fetch -all']),
        (0xfb7185, 'Pull', ['git pull origin ']),
        (0xfb7185, 'Merge', ['git merge ']),
        # 4th row ----------
        (0x22d3ee, 'Status', ['git status']), 
        (0x34d399, 'Soft Rst', ['git reset --soft HEAD~']), # Soft reset
        (0x34d399, 'Hd. Rst', ['git reset --hard origin/']), # Hard reset
        # Encoder button ---
        (0x000000, '', [''])
    ]
}
