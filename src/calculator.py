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

def calculate_expr(expr_string):
    # string must be in the form "a op b" where op is one of +, -, *, /, ^
    tokens = expr_string.split()
    if len(tokens) != 3:
        raise ValueError("Expression must be in the form 'a op b'")

    a = float(tokens[0])
    op = tokens[1]
    b = float(tokens[2])

    if op == '+':
        return add(a, b)
    elif op == '-':
        return subtract(a, b)
    elif op == '*':
        return multiply(a, b)
    elif op == '/':
        return divide(a, b)
    elif op == '^':
        return power(a, b)
    else:
        raise ValueError(f"Unsupported operator: {op}")

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

    # Statistics demo
    print("\n=== Statistics Demo ===")
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(f"Numbers: {numbers}")
    print(f"Mean: {calculate_mean(numbers)}")
    print(f"Median: {calculate_median(numbers)}")

    # Interactive mode
    print("\n=== Interactive Mode ===")
    print("Calculator is ready for interactive use!")
    print("Type 'help' for available commands.")

    while True:
        input_str = input(">>> ").strip().lower()
        if input_str == 'q':
            print("Exiting calculator. Goodbye!")
            break

        try:
            print(calculate_expr(input_str))
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
