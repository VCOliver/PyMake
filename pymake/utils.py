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

NON_STD_LIBRARIES = {
    "ncurses": "Curses",
    "boost": "Boost",
    "openssl": "OpenSSL",
    "zlib": "ZLIB",
    "libxml2": "LibXML2",
    "libxslt": "LibXSLT",
    "libpng": "LibPNG",
    "libjpeg": "LibJPEG",
    "libtiff": "LibTIFF",
    "libwebp": "LibWebP",
    "libvpx": "LibVPX",
    "libav": "LibAV",
    "libavcodec": "LibAV",
    "libavformat": "LibAV",
    "libavutil": "LibAV",
    "sqlite3": "SQLite3"
}