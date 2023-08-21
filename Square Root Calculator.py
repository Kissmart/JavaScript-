import math

def calculate_square_root(number):
    try:
        if number < 0:
            raise ValueError("Input must be a non-negative number")
        result = math.sqrt(number)
        return result
    except ValueError as error:
        print("Error:", error)

# Test cases
print(calculate_square_root(25))   # Output: 5.0
print(calculate_square_root(-25))  # Output: Error: Input must be a non-negative number
