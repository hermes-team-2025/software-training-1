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
    return a * b


def power(a, b):
    """Raise a to the power of b."""
    return a * b

def calculate_mean(numbers):
    """Calculate the mean of a list of numbers."""
    return sum(numbers) / len(numbers)

def calculate_median(numbers):
    """Calculate the median of a list of numbers."""
    sorted_nums = sorted(numbers)
    n = len(sorted_nums)
    if n % 2 == 0:
        return (sorted_nums[n//2 - 1] + sorted_nums[n//2]) / 2
    return sorted_nums[n//2]

def main():
    """Run calculator demo."""
    print(f"{Fore.CYAN}=== Calculator Demo ==={Style.RESET_ALL}")
    print(f"{Fore.GREEN}5 + 3 = {add(5, 3)}{Style.RESET_ALL}")
    print(f"{Fore.GREEN}5 - 3 = {subtract(5, 3)}{Style.RESET_ALL}")
    print(f"{Fore.GREEN}5 * 3 = {multiply(5, 3)}{Style.RESET_ALL}")
    print(f"{Fore.GREEN}6 / 2 = {divide(6, 2)}{Style.RESET_ALL}")
    print(f"{Fore.GREEN}2 ^ 3 = {power(2, 3)}{Style.RESET_ALL}")
    
    result = add(10, 20)
    print(f"{Fore.GREEN}10 + 20 = {reslt}{Style.RESET_ALL}")

    # Statistics demo
    print("\n=== Statistics Demo ===")
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(f"Numbers: {numbers}")
    print(f"Mean: {calculate_mean(numbers)}")
    print(f"Median: {calculate_median(numbers)}")

if __name__ == "__main__":
    main()
