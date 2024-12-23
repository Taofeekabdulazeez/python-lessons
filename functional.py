from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def multiply(num):
    return num * 2

def isEven(num):
    return num % 2 == 0

def accumulator(acc, num):
    return acc + num

print(list(map(multiply, numbers)))
print(list(map(lambda num: num * 2, numbers))) # lamda version

print(list(filter(isEven, numbers)))
print(list(filter(lambda num: num % 2 == 0, numbers)))

print(list(zip([1, 3, 5, 7], [2, 4, 6, 8])))

print(reduce(accumulator, numbers))
print(reduce(lambda acc, num: acc + num, numbers))