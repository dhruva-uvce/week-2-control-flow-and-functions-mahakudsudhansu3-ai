# Q01. Grade Calculator (if-elif-else)

score_input = input("Enter your score: ")

score = int(score_input)

# Logic to determine the grade or validity
if score < 0 or score > 100:
    print("Invalid score")
elif score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")
