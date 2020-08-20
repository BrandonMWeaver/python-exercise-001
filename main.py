message = "Python"
print(message + '\n')

# String formatting
name = "Brandon Weaver"
print("My name is {}.\n".format(name))

# Conditionals
number = 5

if number > 10:
    print("{} is greater than 10.".format(number))
else:
    print("{} is not greater than 10.".format(number))

# Loops
people = ["Jane", "Joe", "John"]

print("\nFor iterator in range:")
for i in range(len(people)):
    print(people[i])

print("\nFor element in array:")
for person in people:
    print(person)

print("\nWhile:")
i = 0
while i < len(people):
    if i == len(people) - 1:
        print(people[i] + '\n')
    else:
        print(people[i])
    i += 1

# Functions
def print_greeting(name = "Brandon Weaver"):
    print("Hello, my name is {}.".format(name))

print_greeting("Jane Doe")
print_greeting()
