def exactly_two_positive(a, b, c):
    # Count the number of positive numbers
    count = sum(1 for x in [a, b, c] if x > 0)
    # Return True if exactly two numbers are positive
    return count == 2

# Testing of the function
print(exactly_two_positive(2, 4, -3)) # Output: True
print(exactly_two_positive(-4, 6, 8)) # Output: True
print(exactly_two_positive(4, -6, 9)) # Output: True
print(exactly_two_positive(-4, 6, 0)) # Output: False
print(exactly_two_positive(4, 6, 10)) # Output: False
print(exactly_two_positive(-14, -3, -4)) # Output: False