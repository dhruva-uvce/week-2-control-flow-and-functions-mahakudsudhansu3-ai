# Ask the user for a positive integer n
n = int(input("Enter n: "))

# Loop from 1 to n (inclusive)
for i in range(1, n + 1):
    # Check if multiple of both 3 and 5 first
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    # Check if multiple of 3
    elif i % 3 == 0:
        print("Fizz")
    # Check if multiple of 5
    elif i % 5 == 0:
        print("Buzz")
    # If none of the above, print the number itself
    else:
        print(i)
