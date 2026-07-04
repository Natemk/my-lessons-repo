"""
file = open("file_handing.txt")

content = file.read()

print(content)
"""
"""
file = open("notes.txt", "w")
file.write("This is a new note.\n")
file.close()
"""

"""
file = open("students.txt", "w")
file.write("John\n")
file.close()
"""
"""
file = open("students.txt", "a")
file.write("\nKenan")
file.close()
"""
"""
file = open("log.txt", "a")
file.write("\nProgram initialized")
file.close

"""
"""
file = open("fruits.txt", "a")
file.write("Orange\n")
file.close()
"""

with open("fruits.txt") as file:

line in file
print(line.strip())