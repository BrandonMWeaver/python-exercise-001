message = "Python"
print(message)

# String formatting
name = "Brandon Weaver"
print("My name is {}.".format(name))

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
    print(people[i])
    i += 1
