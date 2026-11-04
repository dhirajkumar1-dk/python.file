# take a student name and marks
name = input("Enter student name: ")
marks = []
for i in range(1, 6):
    mark = float(input(f"Enter marks for subject {i}: "))
    marks.append(mark)

# Calculate total and percentage
total = sum(marks)
percentage = total / 5

# Check pass and fail
passed = True
for mark in marks:
    if mark < 40:
        passed = False

# Assign grade

if not passed:
    grade = "fail"
elif percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    garde = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "E"

# Display result

print("\n--- Student Result ---")
print("Name:", name)
print("Total:", total)
print("Percentage:", percentage)
print("Grade:", grade)
print("Result:", "Pass" if passed else "Fail")

