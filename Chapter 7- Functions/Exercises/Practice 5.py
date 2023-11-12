#Write a Python program that defines a function to check whether a given number is prime.

def check_prime(num):
    """Function to check whether a given number is prime."""
    if num > 1:
        for i in range(2, int(num**0.5) + 1):
            if (num % i) == 0:
                return False
        else:
            return True
    else:
        return False

# Example usage:
number = int(input("Enter a number to check if it's prime: "))
if check_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")

