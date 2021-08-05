"""
This script contains clear function for clearing the command line prompt screen
"""

import os

def clear() -> None:
    """Runs `cls` command for linux or runs `clear` command in windows"""
    os.system('cls' if os.name=='nt' else 'clear')
