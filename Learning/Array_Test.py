cars = ["Ford", "Volvo", "BMW"]
print(cars[0])
print(len(cars))
for x in cars:
    print(x)
numbers = [1, 2, 3, 2, 3, 4, 5]
# del numbers[2]
print(numbers)
del numbers[-1]
print(numbers)
try:
    numbers.remove(5)
    print(numbers)
except ValueError as ve:
    print("Value is not in list")
numbers.pop(-1)
print(numbers)
numbers.append(9)
print(len(numbers))
print(numbers)
numbers.extend('8')
print(numbers)
index = len(numbers) - 1
numbers.insert(index, 5)
print(len(numbers))
print(index)
print(numbers)


a = [[2, 3]]*2
a[1][0] = 3
print(a)

# my_input = [1, 2, 3, 4, 5]
# print(f'Current Numbers List {my_input}')
# number = int(input("Please enter a number to be added:\n"))
# index = int(input(f'Enter the index between 0 and {len(my_input) - 1} to add the given number:\n'))
# my_input.insert(index, number)
# print(f'Updated List {my_input}')
