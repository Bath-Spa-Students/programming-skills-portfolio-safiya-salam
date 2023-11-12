#Write a Python function that calculates the factorial of a given positive integer using
#recursion.

def factorial(n):
    """Calculate the factorial of a given positive integer using recursion."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Example usage:
number = int(input("enter any number:"))
result = factorial(number)
print(f"The factorial of {number} is: {result}")
