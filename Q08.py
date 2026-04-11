# Ask the user for a positive integer
num_input = input("Enter a number: ")
original_num = int(num_input)
number = original_num
digit_sum = 0

# Use a while loop to process each digit
while number > 0:
    # Get the last digit using modulo 10
    digit = number % 10
    # Add digit to the sum
    digit_sum += digit
    # Remove the last digit using floor division
    number = number // 10

# Print the result matching the sample output format
print(f"Sum of digits of {original_num} = {digit_sum}")
