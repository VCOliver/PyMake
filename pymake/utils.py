import argparse
from colorama import Fore, Style

def str_to_bool(value):
    """Convert string to boolean."""
    if value.lower() in ['true', '1', 't', 'y', 'yes', 'on']:
        return True
    elif value.lower() in ['false', '0', 'f', 'n', 'no', 'off']:
        return False
    else:
        raise argparse.ArgumentTypeError(f"Invalid boolean value: {value}")
    
VCOLOR = Fore.LIGHTCYAN_EX + Style.BRIGHT
RESET_STYLE = Style.RESET_ALL