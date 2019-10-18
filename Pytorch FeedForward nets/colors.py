RED   = "\033[1;31m"  
BLUE  = "\033[1;34m"
CYAN  = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD    = "\033[;1m"
REVERSE = "\033[;7m"

def print_colored_line(color): 
    sys.stdout.write(color)
    print("*="*35)
    sys.stdout.write(colors.RESET)