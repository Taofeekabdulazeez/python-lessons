def containsDuplicate(arr):
    seen = {}
    for item in arr:
        if item in seen:
            return True
        else:
            seen[item] = item
    return False


print(containsDuplicate([1, 2, 3, 4, 6]))