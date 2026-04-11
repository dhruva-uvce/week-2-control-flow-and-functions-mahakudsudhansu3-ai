num = int(input("Enter a number: "))
reversed_num = 0

temp_num = num 

while temp_num > 0:
    digit = temp_num % 10             
    reversed_num = reversed_num * 10 + digit
    temp_num //= 10                   

print(f"Reversed: {reversed_num}")
