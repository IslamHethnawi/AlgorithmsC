def factorial(n):
    """
    Calculate the factorial of a non-negative integer n.
    :param n: Non-negative integer
    :return: Factorial of n
    """
    if n < 0:
        return "Invalid input. Please enter a non-negative integer."
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result


# Example usage:
number = int(input("Enter a number to calculate its factorial: "))
print(f"The factorial of {number} is {factorial(number)}.")
