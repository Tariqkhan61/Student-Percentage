# Write a python program to input student name and marks of 3 subjects.
#  Print name and percentage in output

student_name = input("Enter student name: ")
english_marks = float(input("Enter english marks: "))
math_marks = float(input("Enter math marks: "))
science_marks = float(input("Enter science marks: "))
physics_marks = float(input("Enter physics marks: "))

# Calculate percentage
percentge = (int(english_marks + math_marks + science_marks + physics_marks) / 400) * 100

# Print Result
print(f"Student Name: {student_name} is {percentge}%. Well done!")
