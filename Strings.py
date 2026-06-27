'''
Mini Project

Employee Directory

Requirements:

Store 3 employees
Name
Department
Salary

Display:

Name: John
Department: IT
Salary: 80000

Homework:

1. Create a dictionary for a car:

car = {
    "make": "",
    "model": "",
    "year": 0
}

ask:::::::::::print all keys and values

2. Store students inside a list

students = [
    {
        "name": "John",
        "grade": 85
    },

    {
        "name": "Sarah",
        "grade": 90
    }
]

ask::::::::::::::: Print all student names and grades
'''





def main():
    print("Student Grade Program")
    print("--------------------")

    # Store students inside a list of dictionaries
    students = []

    while True:
        name = input("Enter student name (or press Enter to finish): ").strip()
        if not name:
            break

        grade_input = input(f"Enter grade for {name}: ").strip()
        while not grade_input.isdigit():
            grade_input = input("Please enter a valid grade as a number: ").strip()

        students.append({
            "name": name,
            "grade": int(grade_input)
        })

    if not students:
        students = [
            {"name": "John", "grade": 85},
            {"name": "Sarah", "grade": 90}
        ]
        print("\nNo student input provided, using sample students.")

    print("\nStudent names and grades:")
    for student in students:
        print(f"{student['name']}: {student['grade']}")


if __name__ == "__main__":
    main()
