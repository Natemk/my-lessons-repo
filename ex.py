'''
for i in range(5):
    for j in range(0, i + 1):
        print("*", end=" ")
    print()


grades = []



for i in range(5):
    grade = float(input(f"Enter grade {i+1}: "))
    grades.append(grade)

      
print("Grades:")
for grade in grades:
    print(grade)
                   
   
total = 0
for grade in grades:
    total += grade
print("Total:", float(total))

average = total/len(grades)
print("Average:", float(average))
         
   
highest = max(grades)
print("Highest grade:", (highest))
             
lowest = min(grades)
print("Lowest grade:", (lowest))
   
        
'''

# Create an empty list to store student names
students = []

# Ask the user to enter 5 student names
for i in range(5):
    name = input(f"Enter name of student {i+1}: ").capitalize()
    
    students.append(name)

print('\n' + "Students entered are: "
      + '\n')

# Print the list of students after they have been entered
for student in students:
    
        print(student)
    


# Create an empty list to store the corresponding grades
grades = []
invalid_grade = False

for student in students:
    grade = float(input(f"Enter grade for {student}: "))
    if grade >= 0 and grade <= 100:
        grades.append(grade)
    else:
        print("Invalid grade entered. Please enter a grade between 0 and 100." + '\n')
        invalid_grade = True
        break

    # Print the letter grade for each student as the grade is entered
    if grade >= 90 and grade <= 100:
        print(f"{student} received an A." + '\n')
    elif grade >= 80 and grade < 90:
        print(f"{student} received a B." + '\n')
    elif grade >= 70 and grade < 80:
        print(f"{student} received a C." + '\n')
    elif grade >= 60 and grade < 70:
        print(f"{student} received a D." + '\n')
    else:
        print(f"{student} received an F." + '\n')

if not invalid_grade and len(grades) == len(students):
    # Pair each student with their grade for sorting
    student_grades = list(zip(students, grades))
    student_grades.sort(key=lambda pair: pair[1], reverse=True)

    print("Students and grades in descending order:")
    for i in range(len(student_grades)):
        student, grade = student_grades[i]
        print(f"{student}: {grade}")
    
