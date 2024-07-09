import os

def clear_screen():
    # Check if the operating system is Windows
    if os.name == 'nt':
        os.system('cls')
    # For other operating systems (Linux and macOS)
    else:
        os.system('clear')


