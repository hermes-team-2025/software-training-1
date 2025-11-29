"""
Simple Calculator Application
"""

from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def add(a, b):
    """Add two numbers."""
    return a + b


def subtract(a, b):
    """Subtract b from a."""
    return a - b


def multiply(a, b):
    """Multiply two numbers."""
    return a * b


def divide(a, b):
    """Divide a by b."""
    return a / b


def power(a, b):
    """Raise a to the power of b."""
    return a ** b


def main():
    """Run calculator demo."""
    print(f"{Fore.CYAN}=== Calculator Demo ==={Style.RESET_ALL}")
    print(f"{Fore.GREEN}5 + 3 = {add(5, 3)}{Style.RESET_ALL}")
    print(f"{Fore.GREEN}5 - 3 = {subtract(5, 3)}{Style.RESET_ALL}")
    print(f"{Fore.GREEN}5 * 3 = {multiply(5, 3)}{Style.RESET_ALL}")
    print(f"{Fore.GREEN}6 / 2 = {divide(6, 2)}{Style.RESET_ALL}")
    print(f"{Fore.GREEN}2 ^ 3 = {power(2, 3)}{Style.RESET_ALL}")
    
    result = add(10, 20)
    print(f"{Fore.GREEN}10 + 20 = {result}{Style.RESET_ALL}")


if __name__ == "__main__":
    main()
