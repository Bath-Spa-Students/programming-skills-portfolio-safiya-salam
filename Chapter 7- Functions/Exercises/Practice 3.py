#Write a Python program that uses a function to check if a given number is prime or not.

def is_prime(number):
    """Check if a given number is prime."""
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

# Get user input
user_input = int(input("Enter a number to check if it's prime: "))

# Check if the number is prime and print the result
if is_prime(user_input):
    print(f"{user_input} is a prime number.")
else:
    print(f"{user_input} is not a prime number.")
