def add(x = 1, y = 2):
    '''
    this function adds two numbers
    '''
    return x + y

print(add(2, 3))
print(add(y=8, x=3))
print(add())

def addAll(*nums):
    print(nums) # tuple
    return sum(nums)

print(addAll(1, 2, 3, 4, 5, 6))

def addAllValues(**obj):
    total = 0
    for val in obj.values():
        total += val
    return total

print(addAllValues(a=1, b=2, c=3, d=4, e=5, f=6))