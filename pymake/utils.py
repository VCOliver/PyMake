import argparse
import subprocess
from colorama import Fore, Style
import shutil

def str_to_bool(value):
    """Convert string to boolean."""
    if value.lower() in ['true', '1', 't', 'y', 'yes', 'on']:
        return True
    elif value.lower() in ['false', '0', 'f', 'n', 'no', 'off']:
        return False
    else:
        raise argparse.ArgumentTypeError(f"Invalid boolean value: {value}")
    
"""Under testing"""
def create_run_shell_command(executable: str):
    """Create the 'run' shell command."""
    with open(".run.sh", "w") as shell:
        shell.write("#!/bin/bash\n")
        shell.write(f"alias run='./build/{executable}'")
        
    subprocess.run(["bash", ".run.sh"], shell=False)
    
VCOLOR = Fore.LIGHTCYAN_EX + Style.BRIGHT
RESET_STYLE = Style.RESET_ALL