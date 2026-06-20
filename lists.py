"""
fruit = ["Apple", "Banana", "Pineapple", "Orange"]

print(fruit[3])



fruit = ["Apple", "Banana", "Pineapple", "Orange"]

fruit[1] = "Mango"

print(fruit)

fruit = ["Apple", "Banana", "Pineapple", "Orange"]

fruit.append("Guava")

print(fruit)



fruit = ["Apple", "Banana", "Pineapple", "Orange"]

fruit.remove("Apple")

print(fruit)

# pop() - removes by the index from a list

fruit = ["Apple", "Banana", "Pineapple", "Orange"]

fruit.pop(1)

print(fruit)



#len()

fruit = ["Apple", "Banana", "Pineapple", "Orange"]

print(len(fruit))


#LOOPING THROUGH LISTS:

fruit = ["Apple", "Banana", "Pineapple", "Orange"]

for fruits in fruit:
    print(fruits)


# Mini Project 1: Favourite Movies:

movies =[]

movies.append(input(" Movie 1: "))
movies.append(input(" Movie 2: "))
movies.append(input(" Movie 3: "))

print("\nYour Favourite Movies are:")

for movie in movies:
    print(movie)

"""

# Mini Project: Student Marks System:

marks=[]

for i in range(5):
    mark = float(input("Enter student mark: "))
    marks.append(mark)


for mark in marks:
    print("\nStudent Marks:", mark)

print("\nTotal:", sum(marks))
print("\nAverage: ", sum(marks)/len(marks))
print("\nHighest: ", max(marks))
print("\nLowest:", min(marks))


    


