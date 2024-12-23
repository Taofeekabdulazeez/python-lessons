def square_all(obj):
    return {key:value**2 for key,value in obj.items()}


print(square_all({'a': 1, 'b': 2, 'c': 3}))