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
