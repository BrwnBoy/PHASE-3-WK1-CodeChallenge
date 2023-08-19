def solve(s):
    # Initialize the maximum value and the current value
    max_val, cur_val = 0, 0
    # Iterate over each character in the string
    for char in s:
        # If the character is a consonant
        if char not in 'aeiou':
            # Add its alphabetic value to the currnet value
            cur_val += ord(char) - 96
            # Update the maximum value
            max_val = max(max_val, cur_val)
        else:
            # Reset the current value
            cur_val = 0
        # Return the maximum value
        return max_val
    
# Testing of the fucntion
print(solve('zodiacs')) # Output: 26
print(solve('strength')) # Output: 19