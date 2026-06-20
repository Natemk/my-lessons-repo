'''
fruits = ['apple', 'banana', 'cherry']

fruits[1] = "orange"

print(fruits)


fruits = ['apple', 'banana', 'cherry']

fruits.insert(1, "orange")

print(fruits)


for i in range(11, 0, -2):
    print(i)


Customers = [
    "John",
    "Mary",
    "Peter"
]


for customer in Customers:
    print(
           f"Processing {customer}"
    )


fruits = [
    "Apples",
    "Bananas",
    "Pears"
]

print(len(fruits))



fruits = [
    "Apples",
    "Bananas",
    "Pears"
]

for i in range(len(fruits)):
    print(i, fruits[i])



for pears in range(1):
    for bananas in range(1):
        print("hello", end=" ")

    print()


marks = [70, 85, 92, 68, 88]

total = 0

for mark in marks:
    total += mark

average = total / len(marks)

print(average)



name ="Python"

print(name[2:])



name = "  python  "

print(name.strip())

fruits = "apple banana cherry"

healthy_fruits = fruits.split()

print(healthy_fruits)

'''

words = [
    "Python",
    "is",
    "a",
    "great",
    "language"
]

sentence = " ".join(words)

print(sentence)


